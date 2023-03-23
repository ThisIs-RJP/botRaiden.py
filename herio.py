#!/usr/bin/env python3

import sys
import asyncio
import functools
import itertools
import math
import random
import os
import discord
import youtube_dl
from itertools import cycle
from async_timeout import timeout
from discord.ext import commands
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
import aiohttp
import io
from itertools import cycle
import json
import pickle
import string
import random
from datetime import date
from datetime import datetime

from config import *
from dotenv import load_dotenv


load_dotenv('token.env')
description = "Greetings. I am the Raiden Shogun, the Electro Archon and the supreme ruler of the island nation of Inazuma"
bot = commands.Bot(command_prefix="r!", intents=discord.Intents.all(), description=description)

ids = set()
@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))
    await bot.change_presence(activity=discord. Activity(type=discord.ActivityType.watching, name='over Inazuma...'))
    print(random.choice(START_UP))
    with open("user.txt") as f:
        for id in f:
            ids.add(id.strip())

@bot.event
async def on_message(message):
    number = random.randint(1, 5)
    id = message.author.id
    channel = message.channel
    with open("user.txt", "r+") as f:
        contents = f.read()
        if str(id) in contents and str(id)+"m" not in contents:
            if number == 1:
                await channel.send(random.choice(RAIDEN_SUB_MSG))
        elif str(id) + "m" in contents:
            if number == 5:
                await channel.send(random.choice(RAIDEN_HATE_MSG))
    print(f"{message.guild}/{message.channel}/{message.author.name}> Message: {message.content}")

    await bot.process_commands(message)
     
@bot.command(pass_context=True)
async def register(ctx, *, message):
    if message.lower() == "help":
        await ctx.send(embed=makeEmbed("Register command", False, "Valid inputs: female, girl, woman, male, boy, man", "If input == female, girl, woman, bot will occasionally meow or bark at user"))
    elif message.lower() == "female" or message.lower() == "girl" or message.lower() == "woman":
        id = ctx.message.author.id
        with open("user.txt", "r+") as f:
            contents = f.read()
            if str(id) not in contents:
                print(str(id), file=f)
                await ctx.send("<3")
            else:
                await ctx.send("Hey, you've registered (as a female) already!")

    elif message.lower() == "male" or message.lower() == "boy" or message.lower() == "man":
        id = ctx.message.author.id
        with open("user.txt", "r+") as f:
            contents = f.read()
            if str(id) + "m" not in contents and str(id) not in contents:
                print(str(id) + "m", file=f)
                await ctx.send("</3")
            else:
                await ctx.send("Hey, you've registered (as a male) already!")
        await ctx.send("Hmph")

    else:
        await ctx.send(INVALID_INPUT)

@bot.command()
async def ping(ctx):
    await ctx.send(embed=makeEmbed("PONG", False, False, "PONG"))

@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

@bot.command()
async def google(ctx, *, message):
    # embed = discord.Embed(
    #     title=f"You googled {message}",
    #     color=discord.Color.green()
    # )
    # await ctx.send(embed=embed)
    # await ctx.send("https://google.com/search?q={}".format("+".join(message.split())))

    await ctx.send(embed=makeEmbed(f"Heres your link!", "https://google.com/search?q={}".format("+".join(message.split())), f"You Googled: {message}", False, "I wonder what you used this command for?"))

@bot.command()
async def poll(ctx, *, message):
    await ctx.channel.purge(limit=1)
    member = ctx.message.author
    userAvatar = member.avatar.url

    msg = await ctx.send(embed=makeEmbedThumbNail(f"{random.choice(POLL_MESSAGES)}", False, f"From: {ctx.author.mention}", userAvatar, f"{message}"))
    await msg.add_reaction("⬆️")
    await msg.add_reaction("⬇️")

@bot.command()
async def hello(ctx):
    emg = discord.Embed(
        title = "TORN TO OBLIVION!"
    )
    emg.set_image(url="https://media.tenor.com/qzqq5KFO1vkAAAAC/raiden-shogun.gif")
    await ctx.send(embed=emg)

@bot.command()
@commands.has_permissions(kick_members=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    clear = discord.Embed(
        title="Messages cleared"
    )
    await ctx.send(embed=clear)

@bot.command()
async def specisay(ctx, *,message):
   # await ctx.channel.purge(limit=1)
    x = message.split()
    new = []
    title = []
    loop = 0
    for i in range(len(x)):
        if "]" in x[i]:
            title.append(x[i])    
            loop = i + 1
            while loop < len(x):
                new.append(x[loop])
                loop = loop + 1
            break

        else:
            title.append(x[i])

    embed = discord.Embed(
        title="{}".format((" ".join(title)).translate(str.maketrans('', '', string.punctuation))),
        color=random.choice(COLORS)
    )
    embed.set_footer(text=" ".join(new))
    await ctx.send(embed=embed)


@bot.command()
async def horni(ctx, arg=""):
    imageBonk = "https://i.pinimg.com/originals/50/6e/e2/506ee22b38ada4c5390498809fca404f.jpg"
    if arg == "":
        bonk = discord.Embed(
            title = 'Bonk',
            description = f'{ctx.author.mention} gets bonked'
        )
        bonk.set_image(url=imageBonk)
        await ctx.send(embed=bonk)
    else:
        boky = discord.Embed(
            title = "Bonk",
            description = f'{ctx.author.mention} bonks {arg} for being horni'

        )
        boky.set_image(url=imageBonk)
        await ctx.send(embed=boky)

@bot.command()
@commands.has_permissions(kick_members=True)
async def quit(ctx):
    sys.exit()

@bot.command()
@commands.has_permissions(kick_members=True)
async def say(ctx,*, message, amount=1):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(
        title="Announcment!",
        description=f"From: {ctx.author.mention}",
        colour=discord.Color.green()
        )
    embed.set_footer(text=message)

    await ctx.send(embed=embed)

bot.run(os.getenv("TOKEN"))
