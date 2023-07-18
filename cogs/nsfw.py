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
bot = commands.Bot(command_prefix="r!", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)
"""
    NSFW Commands
"""
# https://nhentai.net/search/?q=raiden+shogun&sort=popular-week

class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() # raiden shogun, popular
    async def nhentai(self, ctx, *, mes=None):
        mes = "" if mes == None else mes.split()
        if mes == "":
            await ctx.send(embed=makeEmbedThumbNail("Heres your random hentai link!", "https://nhentai.net/g/{}/".format(random.randint(10000, 999999)), "Most likely this link wont work, so feel free to call this command again to receive a random link!", LINK, genRandResponse()))
    
        elif mes[-1].lower() == "all-time":
            x = mes.pop()
            await ctx.send(embed=makeEmbedThumbNail(LINK_NSFW_REPLY, "https://nhentai.net/search/?q={}&sort=popular".format("+".join(mes)), nsfw_nh_reply(mes, x), LINK, genRandResponse()))
    
        else:
            x = mes.pop()
            await ctx.send(embed=makeEmbedThumbNail(LINK_NSFW_REPLY, "https://nhentai.net/search/?q={}&sort=popular-{}".format("+".join(mes), x), nsfw_nh_reply(mes, "popular-"+x), LINK, genRandResponse()))

"""
    End of NSFW Commands
"""
