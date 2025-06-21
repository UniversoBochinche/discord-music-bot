import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Discord bot configuration
BOT_PREFIX = '!'

# FFmpeg configuration
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn -ac 2 -ar 48000 -b:a 64k -c:a libopus -application audio -filter:a "aresample=48000" -threads 1'
}