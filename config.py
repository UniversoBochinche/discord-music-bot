import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Discord bot configuration
BOT_PREFIX = '!'

# FFmpeg configuration
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 -probesize 32 -analyzeduration 100000',
    'options': '-vn -b:a 64k -application audio -threads 1 -ac 2 -ar 48000 -c:a libopus'
}