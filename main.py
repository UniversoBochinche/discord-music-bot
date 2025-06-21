import logging
logging.getLogger('discord').setLevel(logging.CRITICAL)
logging.getLogger('yt_dlp').setLevel(logging.CRITICAL)

from bot import setup_bot
from config import DISCORD_TOKEN

def main():
    bot = setup_bot()

    @bot.event
    async def on_ready():
        print(f"Bot is ready! Logged in as {bot.user}")

    print("Bot starting...")
    bot.run(DISCORD_TOKEN)

if __name__ == "__main__":
    main()