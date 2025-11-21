import discord
import os
import asyncio
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
bot_token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

current_timers = {}
@bot.command('pomo')
async def pomo(ctx, action: str, length: int):
    if action == 'start':
        # check existing timer
        if ctx.author in current_timers.keys():
            ctx.send(f'you already have an existing timer, {ctx.author}.')
        else:
            # start timer
            await ctx.send('starting timer... 🍅')
            current_timers[ctx.author] =  length  # timer length will be parameterised
            await asyncio.sleep(length)
            await ctx.send('timer is up!')




# @client.event
# async def on_ready():
#     print(f'we have logged in as {client.user}')
#
#
# @client.event
# async def on_message(message):
#     print(f"Message received: '{message.content}' from {message.author}")
#
#     if message.author == client.user:
#         print("Message is from bot, ignoring")
#         return
#
#     if message.content.lower().startswith('hello'):
#         print("Sending Hello!! response")
#         await message.channel.send('Hello!!')
#     else:
#         print(f"Message didn't match: '{message.content.lower()}'")


bot.run(bot_token)

