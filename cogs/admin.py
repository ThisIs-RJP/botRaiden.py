#!/usr/bin/env python3
"""
    Made by Smoodeazy, RJ, 2023
    Feel free to edit the code as much as you like
"""

import sys, asyncio, functools, itertools, math, random, os, discord, aiohttp, io, json, pickle, string, random
# from datetime import date
# from datetime import datetime
import datetime

# Configuration and Countdown Files
from config import *
from countdown import *
#Other imports
from dotenv import load_dotenv, find_dotenv
from itertools import cycle
from async_timeout import timeout
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
from itertools import cycle

"""
    Admin Commands
"""
file = "cogs/times.txt"

bot = commands.Bot(command_prefix="r!", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)
times = {}
with open(file) as f:
    stuff = f.readlines()

    for t in stuff:
        time, event = t.split(";")
        times[time.strip()] = event.strip()

class AdminCom(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["purge"])
    @commands.has_permissions(kick_members=True)
    async def clear(self, ctx, amount=5, member: discord.Member = None):
        await ctx.channel.purge(limit=amount+1)
        clear = discord.Embed(
            title="Messages cleared"
        )
        await ctx.send(embed=clear)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def say(self, ctx, * , message, amount=1):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(
            title="**Announcment!**",
            description=f"From: {ctx.author.mention}\n\n**{message}**",
            colour=discord.Color.green(),
            timestamp=datetime.datetime.utcnow()
            )

        await ctx.send(embed=embed)

    @commands.command()
    async def specisay(self, ctx, *,message, amount=1):
        await ctx.channel.purge(limit=amount)
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
    
    @commands.command()
    async def addrole(self, ctx, member: discord.Member, role : discord.Role):
        if not ctx.author.guild_permissions.manage_roles:
            await ctx.send(embed=makeEmbed("Error", None, "You don't have the necessary permissions to do this!", "Try again if you have the perms!"))
        else:
            await member.add_roles(role)
            await ctx.send(f"Added the {role} role!")
    
    @commands.command()
    async def removerole(self, ctx, member: discord.Member, role : discord.Role):
        if not ctx.author.guild_permissions.manage_roles:
            await ctx.send(embed=makeEmbed("Error", None, "You don't have the necessary permissions to do this!", "Try again if you have the perms!"))
        else:
            await member.remove_roles(role)
            await ctx.send(f"Removed the {role} role!")
    
    times = {}
    with open(file) as f:
        contents = f.readlines()

        for t in contents:
            t = t.split(";")

            times[t[0].strip()] = t[1].strip()
    
    @commands.command()
    # 2023-07-06 00:01:01 ; birthday
    @commands.has_permissions(kick_members=True) # 
    async def cdAdd(self, ctx, *, message):

        checkFormat = checkThis(message.strip())
        time, event = message.split(";")
        alreadyIn = []

        try:
            if checkFormat[0] == "c":
                # await ctx.send("Event added at " + time[0:])
                with open(file) as f:
                    contents = f.readlines()

                    alreadyIn.append(time + ";" + event)

                    for k in contents:
                        alreadyIn.append(k.strip())
                    
                    f.close()
                
                with open(file, "w") as f:
                    f.write("\n".join(alreadyIn))

                    f.close()

                await ctx.send(embed=makeEmbed("Event added!", False, "Successfully added event **{}** at date **{}**".format(event.strip(), time.strip()), genRandResponse()))
        
        except TypeError:
            await ctx.send(embed=checkFormat)
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def cdFormat(self, ctx):
        await ctx.send(embed=makeEmbed("Countdown Command Format", False, "YEAR:MONTH:DAY HOUR:MIN:SEC ; {event}\nE.G 2023-07-07 15:58:00 ; Time to Game!**", "Run cd!cdAdd and use this format to add an event!"))
        
        # else:
        # time, event = message.split(";")
        # # await ctx.send(message)
        # with open(file) as f:
        #     stuff = f.readlines()
        #     returnContents = []

        #     for t in stuff:
        #         returnContents.append(t.strip())
            
        #     f.close()
        
        # returnContents.append(time + " ; " + event)

        # with open(file, "w") as f:
        #     f.writelines("\n".join(returnContents))
        
        # await ctx.send(f"**{event.capitalize()}** was added at **{time}**!")
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def cdList(self, ctx):
        with open(file) as f:
            stuff = f.readlines()
            returnContents = []

            for t in stuff:
                returnContents.append(t)
            
            f.close()
        
        await ctx.send(embed=makeEmbed("**Countdown List**", False, "\n".join(stuff), "Sounds like a party to me"))
    
    # while True:
        # finished = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

        # @commands.event()
        # async def cdAnnouncement(ctx):


"""
    End of Admin Commands
"""
