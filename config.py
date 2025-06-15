import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Discord bot configuration
BOT_PREFIX = '!'

# FFmpeg configuration
FFMPEG_OPTIONS = {
    'options': '-vn'
}