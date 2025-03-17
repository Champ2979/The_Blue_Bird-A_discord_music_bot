
# I have created the bot and it is fully functional, I have added the comments as 'Confidential' for the internal working of the code cuz 
# I am using it for the business purpose, but if you want to create your own bot , you just need to follow the steps starting it for creating your own bot
# Also I will attach the video file for fully working mechanism of the bot. <Coming Soon>
# Soon i shall add the ReadMe file for the whole process and using the Discord Developers Portel efficiently. For now, just look at the code and
# try to understand it. 
# Thank you
import discord
from discord.ext import commands, tasks
import yt_dlp as youtube_dl
import asyncio
from itertools import cycle
from collections import deque
from datetime import datetime
import discord.ext.commands
from dotenv import load_dotenv
import os
load_dotenv()



#Global variables
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True

autoplay_enabled = False
current_song_start = None
current_song_duration = None

bot = commands.Bot(command_prefix="+", intents=intents)
Status = cycle(['Hi there,this is the music bot The Blue Bird', 'Do Listening music for free', 'Have a great time here'])

queue = deque()
current_song = None

# YouTube downloader options
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': False,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',
    'socket_timeout': 30,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'extractor_args': {
        'youtube': {
            'skip': ['dash', 'hls'],
            'player_skip': ['configs'],
        }
    },
    'postprocessors': [{
        'key': 'SponsorBlock',
        'categories': ['music_offtopic']
    }]
}

ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn -b:a 128k -af "volume=0.5"',
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

def create_embed(title, description, color=discord.Color.blue()):
    return discord.Embed(title=title, description=description, color=color)

@bot.event
async def on_ready():
    change_status.start()
    print("BOT IS ONLINE!!")

@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(Status)))

async def play_next(ctx):
    # Confidential code for the functioning of the bot
                # ))
                
                # Play the next song
            #     await play_next(ctx)
            #     return
            
            # c
# o
# n
# f
# i
# d
# e
# n
# t
# i
# a
# l

@bot.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("You need to be in a voice channel to use this command!")
        return
    await ctx.author.voice.channel.connect()
    await ctx.send("Connected to the voice channel!")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Left the voice channel.")
    else:
        await ctx.send("I'm not connected to any voice channel.")
@bot.command()
async def stop(ctx):
    # Confidential

@bot.command()
async def resume(ctx):
#   Confidential

@bot.command()
async def play(ctx, *, search: str):
    # Ensure the bot is connected to a voice channel
    if not ctx.voice_client:
        if ctx.author.voice:
            await ctx.author.voice.channel.connect()
            await ctx.send(f"🔊 Joined {ctx.author.voice.channel} to play music!")
        else:
            await ctx.send("You need to be in a voice channel first. Use +join.")
            return

    # Confidential
    # Confidential
    # Confidential
    # Confidential
    # Confidential
    # Confidential
    # Confidential

        # Start playing if not already playing or paused
        if not ctx.voice_client.is_playing() and not ctx.voice_client.is_paused():
            await play_next(ctx)

    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

@bot.command()
async def autoplay(ctx):
#     Currently working on this line of the code 

@bot.command()
async def skip(ctx):
    # Confidential Code

@bot.command()
async def clear(ctx):
    queue.clear()
    await ctx.send("🧹 The queue has been cleared!")

@bot.command(aliases=['np', 'nowplaying'])
async def current(ctx):
    # COnfidential
    # Format time display
    def format_time(seconds):
        if not seconds: return "Live"
        mins, secs = divmod(seconds, 60)
        return f"{mins}:{secs:02d}"
    
    # Confidential
    await ctx.send(embed=embed)

# Run the bot using the token from the .env file
bot.run(os.getenv('DISCORD_BOT_TOKEN'))

