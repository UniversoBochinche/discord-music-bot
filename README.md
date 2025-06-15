# Discord Music Bot

A modular Discord bot focused on playing music in voice channels. Built with discord.py, this bot allows users to play music from various sources directly in Discord voice channels.

## Features

- Join and leave voice channels
- Play music from URLs
- Simple command structure with customizable prefix
- Modular codebase for easy maintenance and extension

## Setup

1. **Clone the repository**
   ```
   git clone https://github.com/UniversoBochinche/discord-music-bot.git
   cd discord-music-bot
   ```

2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   
   Create a `.env` file in the root directory with your Discord token:
   ```
   DISCORD_TOKEN=your_discord_token_here
   ```

4. **Install FFmpeg**
   
   The bot requires FFmpeg for audio processing. Make sure it's installed and available in your PATH.
   - Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH
   - Linux: `sudo apt install ffmpeg`
   - macOS: `brew install ffmpeg`

5. **Run the bot**
   ```
   python main.py
   ```

## Commands

- `!join` - Join the user's current voice channel
- `!leave` - Leave the current voice channel
- `!play_song [url]` - Play audio from the specified URL

## Project Structure

```
discord-music-bot/
├── main.py               # Entry point
├── config.py             # Configuration and environment variables
├── bot/
│   ├── __init__.py       # Bot initialization
│   └── music.py          # Music-related functionality
└── utils/
    └── ytdl_utils.py     # YouTube-DL configuration
```

## Dependencies

- discord.py
- python-dotenv
- yt-dlp
- PyNaCl
- FFmpeg

## Development

The bot is structured modularly to allow for easy extension. New commands and features can be added by creating additional cog files in the bot directory.

## License

This project is available under the MIT License.