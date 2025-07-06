from dotenv import load_dotenv
import os
import sys

# Get the directory where the executable is located
if getattr(sys, 'frozen', False):
    app_dir = os.path.dirname(sys.executable)
else:
    app_dir = os.path.dirname(os.path.abspath(__file__))

# Point to the .env file next to the executable
dotenv_path = os.path.join(app_dir, ".env")
load_dotenv(dotenv_path)
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Discord bot configuration
BOT_PREFIX = '!'

# FFmpeg configuration
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 -probesize 32 -analyzeduration 0',
    'options': '-vn -b:a 64k -application audio -threads 1'
}