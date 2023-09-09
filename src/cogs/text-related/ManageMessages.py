import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

class ManageMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Listener
    @commands.Cog.listener()
    async def on_message(self, message):
        if(message.author.id != self.bot.user.id): # Bot messages will not be affected
            setattr(self, 'user', message.author)
            if(not message.content.startswith('ta!')):
                await message.add_reaction(os.getenv('CHEER_EMOJI'))

    # Commands
    @commands.command()
    async def test(self, ctx):
        await ctx.send(f"{ctx.message.author} used the test!")
        await ctx.send("Bot is working")

    @commands.command() # Clear 'number' of message(s)
    async def clear(self, ctx, number: int = commands.parameter(default=5)):
        await ctx.channel.purge(limit=number+1)
        await ctx.send(f"Removed {number} most recent message(s)")

# For making extension
async def setup(bot):
    await bot.add_cog(ManageMessages(bot))