from discord.ext import commands
from bot.queue_manager import QueueManager
from bot.youtube_source import YoutubeSource

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queue_manager = QueueManager()

    @commands.command(name='join', help='Join the voice channel')
    async def join(self, ctx):
        if ctx.author.voice:
            await ctx.author.voice.channel.connect()
        else:
            await ctx.send("You're not connected to a voice channel.")

    @commands.command(name='leave', help='Leave the voice channel')
    async def leave(self, ctx):
        vc = ctx.guild.voice_client
        if vc and vc.is_connected():
            await vc.disconnect()
        else:
            await ctx.send("I'm not connected to a voice channel.")

    @commands.command(name='play_song', help='Play a song from a URL')
    async def play(self, ctx, url: str):
        url = url.strip()

        vc = ctx.guild.voice_client

        if not vc:
            if ctx.author.voice:
                vc = await ctx.author.voice.channel.connect()
            else:
                await ctx.send("I'm not connected to a voice channel. Use !join first.")
                return

        try:
            if vc.is_playing() or vc.is_paused():
                await ctx.send("Already playing a song. Adding to queue.")
                self.queue_manager.add_to_queue(ctx.guild.id, url)
                return

            player = await YoutubeSource.from_url(url, loop=self.bot.loop, stream=True)

            async def song_finished(self, ctx):
                vc = ctx.guild.voice_client

                if not vc or not vc.is_connected():
                    self.queue_manager.clear_queue(ctx.guild.id)
                    return

                next_song = self.queue_manager.get_next_item(ctx.guild.id)

                if next_song:
                    await self.play(ctx, next_song)

            vc.play(player, after=lambda e: self.bot.loop.create_task(
                song_finished(self, ctx)
            ))

            await ctx.send(f"**Now playing:** {player.title}")
        except Exception as e:
            await ctx.send(f"Error playing song: {str(e)}")

    @commands.command(name='skip', help='Skip the current song')
    async def skip(self, ctx):
        vc = ctx.guild.voice_client
        if vc and vc.is_playing():
            vc.stop()

            next_song = self.queue_manager.get_next_item(ctx.guild.id)
            if next_song:
                await ctx.send("Skipped the current song.")
                await self.play(ctx, next_song)
            else:
                await ctx.send("No more songs in the queue.")
        else:
            await ctx.send("I'm not playing any song right now.")

    @commands.command(name='pause', help='Pause the current song')
    async def pause(self, ctx):
        vc = ctx.guild.voice_client
        if vc and vc.is_playing():
            vc.pause()
            await ctx.send("Paused the current song.")
        else:
            await ctx.send("I'm not playing any song right now.")

    @commands.command(name='resume', help='Resume the paused song')
    async def resume(self, ctx):
        vc = ctx.guild.voice_client
        if vc and vc.is_paused():
            vc.resume()
            await ctx.send("Resumed the current song.")
        else:
            await ctx.send("I'm not paused right now.")

    @commands.command(name='stop', help='Stop the current song and clear the queue')
    async def stop(self, ctx):
        vc = ctx.guild.voice_client
        if vc and (vc.is_playing() or vc.is_paused()):
            vc.stop()
            self.queue_manager.clear_queue(ctx.guild.id)
            await ctx.send("Stopped the current song and cleared the queue.")
        else:
            await ctx.send("I'm not playing any song right now.")

    @commands.command(name='queue', help='Show the current song queue')
    async def queue(self, ctx):
        guild_id = ctx.guild.id
        queue = self.queue_manager.get_queue(guild_id)

        if not queue:
            await ctx.send("The queue is currently empty.")
            return

        queue_list = "\n".join(f"{i + 1}. {url}" for i, url in enumerate(queue))
        await ctx.send(f"**Current Queue:**\n{queue_list}")

async def setup(bot):
    await bot.add_cog(Commands(bot))