import discord
import asyncio
from discord.ext import commands
from config import BOT_PREFIX

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

from bot.music import setup as setup_music

async def async_setup_bot():
    await setup_music(bot)
    
def setup_bot():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_setup_bot())
    return bot