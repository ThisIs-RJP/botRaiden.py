import os, discord

from discord.ext import commands, tasks
from outputs import *
import datetime

class FunCom(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def quote(self, ctx, *, message):
        await ctx.channel.purge(limit=1)
        message = message.split("[]")
        print(message)
        embed = discord.Embed(
            title="**Another added quote!**, *uh oh*",
            description=f"From: {message[0]}\n\n**{" ".join(m for m in message[1:])}**",
            colour=discord.Color.green(),
            timestamp=datetime.datetime.utcnow()
            )
        embed.set_footer(text=f"See r!help quote for more details")
        await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, arg=""):
        gifGif = random.choice(KISS_LIST)

        if arg == "":
            await ctx.send("You can't really kiss *nothing*, you idiot. What, are you a loner?")
        
        else:
            await ctx.send(embed=gifEmbed("Seems to be a little romance here?", gifGif, f"{ctx.author.mention} kisses {arg}", "Love is in the air tonight..."))
    