import discord
import asyncio
from discord.ext import commands
from config import BOT_PREFIX

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

from bot.commands import setup as setup_commands

async def async_setup_bot():
    await setup_commands(bot)
    
def setup_bot():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_setup_bot())
    return bot