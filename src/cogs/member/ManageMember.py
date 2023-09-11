import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

class ManageMember(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Commands for admin
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def sayonara(seft, ctx, user: discord.Member): #kick member
        if ctx.message.author.top_role > user.top_role:
            await user.kick()

# For making extension
async def setup(bot):
    await bot.add_cog(ManageMember(bot))