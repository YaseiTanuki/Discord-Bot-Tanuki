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
            await ctx.send(f'{user.name} is gone!')
        else:
            await ctx.send("You don't have permission!")

    @commands.command()
    async def you_are_now(seft, ctx, role: discord.Role, user:  discord.Member):
        print(role)
        able_to_set_role = os.getenv('ABLE_TO_SET_ROLE')
        print(able_to_set_role)
        if(role.name in able_to_set_role):
            if discord.utils.get(ctx.guild.roles, name = role.name):
                await user.add_roles(role)
                await ctx.send(f"{user} is now {role}")
            else:
                await ctx.send("Role not exist!")
        else:
            await ctx.send("You don't have permission!")

# For making extension
async def setup(bot):
    await bot.add_cog(ManageMember(bot))