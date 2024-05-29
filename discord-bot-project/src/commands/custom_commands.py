import discord

class CustomCommands:
    def __init__(self, client):
        self.client = client

    async def handle_custom_command(self, message):
        command = message.content[1:].lower()
        if command == 'hello':
            await message.channel.send('Hello! How can I help you today?')
        elif command == 'goodbye':
            await message.channel.send('Goodbye! See you next time.')
        # Add more custom commands here

    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.content.startswith('!'):
            await self.handle_custom_command(message)