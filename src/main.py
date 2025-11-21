import discord

from src.config import bot_token


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'we have logged in as {client.user}')


@client.event
async def on_message(message):
    print(f"Message received: '{message.content}' from {message.author}")

    if message.author == client.user:
        print("Message is from bot, ignoring")
        return

    if message.content.lower().startswith('hello'):
        print("Sending Hello!! response")
        await message.channel.send('Hello!!')
    else:
        print(f"Message didn't match: '{message.content.lower()}'")


client.run(bot_token)

