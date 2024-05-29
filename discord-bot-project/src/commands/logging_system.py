import discord

class LoggingSystem:
    def __init__(self, client):
        self.client = client

    async def log_activity(self, message):
        channel = discord.utils.get(message.guild.text_channels, name='bot-logs')
        if channel:
            await channel.send(f'{message.author} performed the following activity: {message.content}')
        else:
            print('Error: Bot logs channel not found')

    async def log_interaction(self, user, action):
        channel = discord.utils.get(user.guild.text_channels, name='bot-logs')
        if channel:
            await channel.send(f'{user} {action}')
        else:
            print('Error: Bot logs channel not found')