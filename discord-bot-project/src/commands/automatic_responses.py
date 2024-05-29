import discord
from discord.ext import commands

class AutomaticResponses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if message.content.lower() == 'hello':
            await message.channel.send('Hi there!')
        elif message.content.lower() == 'how are you?':
            await message.channel.send('I am a bot, I do not have feelings.')
        # Add more automatic responses here

def setup(bot):
    bot.add_cog(AutomaticResponses(bot))