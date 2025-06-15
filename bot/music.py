import discord
import asyncio
from discord.ext import commands
from utils.ytdl_utils import ytdl
from config import FFMPEG_OPTIONS

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=True):
        loop = loop or asyncio.get_event_loop()

        def extract_info():
            return ytdl.extract_info(url, download=not stream)
        
        data = await loop.run_in_executor(None, extract_info)

        if not data:
            raise Exception("Failed to fetch video data")
            
        if 'entries' in data:
            data = data['entries'][0]
            
        if stream:
            filename = data['url']
        else:
            filename = ytdl.prepare_filename(data)
        
        audio_source = discord.FFmpegPCMAudio(filename, **FFMPEG_OPTIONS)
        return cls(audio_source, data=data)

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
        vc = ctx.guild.voice_client

        if not vc:
            if ctx.author.voice:
                vc = await ctx.author.voice.channel.connect()
            else:
                await ctx.send("I'm not connected to a voice channel. Use !join first.")
                return

        try:
            async with ctx.typing():
                player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
                
                def after_playing(error):
                    if error:
                        print(f'Playback error: {error}')
                
                vc.play(player, after=after_playing)
                
            await ctx.send(f"**Now playing:** {player.title}")
        except Exception as e:
            await ctx.send(f"Error playing song: {str(e)}")

async def setup(bot):
    await bot.add_cog(Music(bot))