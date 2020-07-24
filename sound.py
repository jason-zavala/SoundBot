import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get
import time

client = commands.Bot(command_prefix='.')
user = discord.Client()


@client.event
async def on_ready():
    print('...Online')


@client.command()
async def summon(ctx):
    await ctx.send('What is thy bidding my Master?')


@client.command()
async def commands(ctx):
    msg = \
        "COMMANDS: \n" \
        "> .sob  - Son of a bitch! \n" \
        "> .dad  - Yeah Dad? \n" \
        "> .sp   - Lets do this one last time! \n" \
        "> .b    - YO, papa bitch! \n" \
        "> .bye  - SO LONG GAY BOYS \n"
    await ctx.send(msg)


@client.command()
async def sob(ctx):
    path = 'sounds/sob.mp3'
    await play_sound(ctx, path)


@client.command()
async def dad(ctx):
    path = 'sounds/dad.mp3'
    await play_sound(ctx, path)


@client.command()
async def sp(ctx):
    path = 'sounds/sp.mp3'
    await play_sound(ctx, path)


@client.command()
async def b(ctx):
    path = 'sounds/b.mp3'
    await play_sound(ctx, path)


@client.command()
async def bye(ctx):
    path = 'sounds/bye.mp3'
    await play_sound(ctx, path)


@client.command()
async def dunk(ctx):
    path = 'sounds/dunkey.mp3'
    await play_sound(ctx, path)
    time.sleep(9)


@client.command()
async def genji(ctx):
    path = 'sounds/genji.mp3'
    await play_sound(ctx, path)


@client.command()
async def trump(ctx):
    path = 'sounds/trump.mp3'
    await play_sound(ctx, path)


@client.command()
async def dumb(ctx):
    path = 'sounds/dumb.mp3'
    await play_sound(ctx, path)


@client.command()
async def kill(ctx):
    path = 'sounds/kill.mp3'
    await play_sound(ctx, path)


@client.command()
async def announce(ctx):
    path = 'sounds/announce.mp3'
    await play_sound(ctx, path)


@client.command()
async def dc(ctx):
    await ctx.guild.voice_client.disconnect()


@client.command()
async def test(ctx, *, arg):
    await ctx.send(arg)


async def play_sound(ctx, path):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio(path)
    voice.play(source)
    return
    # await dc(ctx)

CLIENT_SECRET = ''
client.run(CLIENT_SECRET)
