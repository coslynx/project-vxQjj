import discord
from datetime import datetime

class AutomatedMessages:
    def __init__(self, client):
        self.client = client

    async def send_greeting_message(self, member):
        await member.send("Welcome to the server! Enjoy your stay.")

    async def send_farewell_message(self, member):
        await member.send("Goodbye! We hope to see you again soon.")

    async def schedule_message(self, channel_id, message, date_time):
        channel = self.client.get_channel(channel_id)
        if channel:
            await channel.send(message)
            await channel.send(f"Scheduled at: {date_time}")
        else:
            print("Channel not found, message not sent.")

    async def send_reminder(self, member, reminder):
        await member.send(f"Reminder: {reminder}")

    async def send_custom_message(self, member, custom_message):
        await member.send(custom_message)