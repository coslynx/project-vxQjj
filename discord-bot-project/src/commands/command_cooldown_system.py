import discord
from discord.ext import commands
from discord.ext.commands import BucketType, cooldown

class CommandCooldownSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Command Cooldown System is ready.')

    @commands.command()
    @cooldown(1, 60, BucketType.user)
    async def example_command(self, ctx):
        await ctx.send('This is an example command with a cooldown of 60 seconds.')

def setup(bot):
    bot.add_cog(CommandCooldownSystem(bot))