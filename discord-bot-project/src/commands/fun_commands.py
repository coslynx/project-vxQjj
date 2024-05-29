import discord
import random

class FunCommands:
    def __init__(self, client):
        self.client = client

    async def meme(self, ctx):
        # Logic to fetch and send a random meme
        pass

    async def joke(self, ctx):
        # Logic to generate and send a random joke
        pass

    async def trivia(self, ctx):
        # Logic to create and send a trivia question
        pass

    async def fun_command_handler(self, ctx, command):
        if command == "meme":
            await self.meme(ctx)
        elif command == "joke":
            await self.joke(ctx)
        elif command == "trivia":
            await self.trivia(ctx)
        else:
            await ctx.send("Invalid fun command. Try `meme`, `joke`, or `trivia`.")

# Instantiate FunCommands class with the Discord client
fun_commands = FunCommands(client)