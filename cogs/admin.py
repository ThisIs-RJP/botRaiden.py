import os, discord

from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
from outputs import *
import datetime
import string

### Importing my cogs
class AdminCom(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["purge"])
    @commands.has_permissions(kick_members=True)
    async def clear(self, ctx, amount=5):
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
        embed.set_author(name=ctx.author.name)
        await ctx.send(embed=embed)

