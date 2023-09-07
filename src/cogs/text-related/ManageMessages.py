from discord.ext import commands

class ManageMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command()
    async def test(self, ctx:commands.Context):
        await ctx.send("Bot is working")

    @commands.command() # Clear 'number' of message(s)
    async def clear(self, ctx:commands.Context, number: int = commands.parameter(default=5)):
        await ctx.channel.purge(limit=number)
        await ctx.send(f"Removed {number} most recent message(s)")

# For making extension
async def setup(bot):
    await bot.add_cog(ManageMessages(bot))