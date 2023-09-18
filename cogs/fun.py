#!/usr/bin/env python3
"""
    Made by Smoodeazy, RJ, 2023
    Feel free to edit the code as much as you like
"""

import sys, asyncio, functools, itertools, math, random, os, discord, aiohttp, io, json, pickle, string, random

# from datetime import date
# from datetime import datetime
import datetime
from config import *
from dotenv import load_dotenv, find_dotenv
from itertools import cycle
from async_timeout import timeout
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
from itertools import cycle

"""
    Admin Commands
"""
bot = commands.Bot(
    command_prefix="r!",
    intents=discord.Intents.all(),
    description=DESCRIPTION,
    help_command=None,
)


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        """
    Fun commands
        """

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(embed=makeEmbed("PONG", False, False, "PONG"))

    @commands.command(aliases=["8ball"])
    async def magicball(self, ctx, *, message=""):
        first = await ctx.send("https://media.tenor.com/eIGjlGMgVZkAAAAM/sml-bowser.gif")
        await asyncio.sleep(3)
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes, definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
            ]

        await first.edit(content=f"||{random.choice(responses)}||\nYou asked ~*{message}*")

    @commands.command()
    async def echo(self, ctx, *, content: str):
        await ctx.send(content)

    @commands.command()
    async def google(self, ctx, *, message):
        await ctx.send(
            embed=makeEmbed(
                f"Heres your link!",
                "https://google.com/search?q={}".format("+".join(message.split())),
                f"You Googled: {message}",
                False,
                "I wonder what you used this command for?",
            )
        )


    @commands.command()
    async def poll(self, ctx, *, message):
        await ctx.channel.purge(limit=1)
        member = ctx.message.author
        userAvatar = member.avatar.url
        msg = await ctx.send(
            embed=makeEmbedThumbNail(
                f"{random.choice(POLL_MESSAGES)}",
                False,
                f"From: {ctx.author.mention}",
                userAvatar,
                f"{message}",
            )
        )
        await msg.add_reaction("⬆️")
        await msg.add_reaction("⬇️")


    @commands.command()
    async def hello(self, ctx):
        emg = discord.Embed(title="TORN TO OBLIVION!")
        emg.set_image(url="https://media.tenor.com/qzqq5KFO1vkAAAAC/raiden-shogun.gif")
        await ctx.send(embed=emg)

    @commands.command()
    async def kiss(self, ctx, arg=""):
        gifGif = random.choice(KISS_LIST)

        if arg == "":
            await ctx.send("You can't really kiss *nothing*, you idiot. What, are you a loner?")
        
        else:
            await ctx.send(embed=gifEmbed("Seems to be a little romance here?", gifGif, f"{ctx.author.mention} kisses {arg}", "Love is in the air tonight..."))

    @commands.command()
    async def hug(self, ctx, arg=""):
        gifGif = random.choice(HUG_LIST)

        if arg == "":
            await ctx.send("You can't really hug *nothing*, you idiot. What, are you a loner?")
        
        else:
            await ctx.send(embed=gifEmbed("At least someones being nice", gifGif, f"{ctx.author.mention} hugs {arg}", "How many hugs are you willing to give?"))

    @commands.command()
    async def kill(self, ctx, arg=""):
        gifGif = random.choice(KILL_LIST)

        if arg == "":
            await ctx.send("You can't really kill *nothing*, you idiot. What, are you an idiot??")
        
        else:
            await ctx.send(embed=gifEmbed("At least someones being nice", gifGif, f"{ctx.author.mention} kills {arg}", "How many hugs are you willing to give?"))

"""
    END Fun commands
"""
