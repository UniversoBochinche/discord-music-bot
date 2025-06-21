import discord
import asyncio
import subprocess
from utils.ytdl_utils import ytdl
from config import FFMPEG_OPTIONS

class YoutubeSource(discord.FFmpegOpusAudio):
    def __init__(self, source, *, data):
        super().__init__(source, **FFMPEG_OPTIONS)
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

        return cls(filename, data=data)