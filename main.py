import os
import asyncio
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


async def load():
    skip_files = ['test.py']
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename not in skip_files:
            await bot.load_extension(f'cogs.{filename[:-3]}')


async def main():
    async with bot:
        await load()
        await bot.start(os.getenv('TOKEN'))


@bot.event
async def on_ready():
    print('bot is ready')


asyncio.run(main())
