#!/usr/bin/env python3
"""
    Made by Smoodeazy, RJ, 2023
    Feel free to edit the code as much as you like
"""

import sys, asyncio, functools, itertools, math, random, os, discord, aiohttp, io, json, pickle, string, random

from datetime import date
from datetime import datetime
from config import *
from countdown import *
from cogs.admin import *
from cogs.fun import *
from cogs.wishing import *
from cogs.blackjack import *
from dotenv import load_dotenv, find_dotenv
from itertools import cycle
from async_timeout import timeout
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
from itertools import cycle

bot = commands.Bot(command_prefix="r!", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)

load_dotenv("token.env")

TOKEN = os.getenv("TOKEN")
ids = set()
file = "cogs/times.txt"

@bot.event
async def on_ready():

    await bot.add_cog(AdminCom(bot))
    await bot.add_cog(Fun(bot))

    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))
    await bot.change_presence(activity=discord. Activity(type=discord.ActivityType.watching, name='over Inazuma...'))
    print(random.choice(START_UP))
    with open("user.txt") as f:
        for id in f:
            ids.add(id.strip())

##### 

@bot.event
async def on_message(message):
    print(f"{message.guild}/{message.channel}/{message.author.name}> Message: {message.content}")

    await bot.process_commands(message)

"""
    Dedicated Event commands ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    End of dedicated Event commands
"""

# while True:
#     dates = []
#     with open(file2) as f:
#         filedates = f.readlines()

#         for line in filedates:
#             dates.append(line)
    

#         f.close()

#     with open(file2, "w") as f:
#         f.write("\n".join(dates))
#         f.close()
    
#     today = date.today

#     if today in dates:
#         @bot.event
#         async def dueDue(ctx):
#             await ctx.send
# @bot.event
# async def on_command_error(ctx, error):
#     await ctx.send(embed=makeEmbed("Invalid input!", None, "*Please make sure you're using this command right!*", "Try again after running *r!help*"))


@bot.command()
async def help(ctx, *, mes=None):
    mes = None if mes == None else mes.lower()
    if mes == None:
        returnList = []

        for k in HELPDICT.keys():
            returnList.append(k)

        embed = discord.Embed(
            title="Raiden Command List",
            description="Commands sorted through categories.",
            color=random.choice(COLORS),
            timestamp=datetime.datetime.utcnow()
        )

        embed.add_field(name="Fun", value="**r!help fun** for a list of all commands")
        embed.add_field(name="Admin", value="**r!help admin** for a list of all commands")

        embed.set_footer(text=f"Still making new commands!")

        await ctx.send(embed=embed)

    elif mes.lower() in HELPDICT:
        list = HELPDICT[mes]
        print("This is the contents")
        print(list)
        print()

        await ctx.send(embed=embedFields(list[0], list[2], list[3], genRandResponse())) # Title, 
    
    elif mes.lower() in COMMAND_DICT:
        list =  COMMAND_DICT[mes]
        await ctx.send(embed=embedFields(list[0], list[1], list[2], genRandResponse()))

"""
    Bot Run
"""

@bot.command()
@commands.has_permissions(kick_members=True)
async def quit(ctx):
    sys.exit()

bot.run(TOKEN)
