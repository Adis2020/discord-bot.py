import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())


async def load():
    skip_files = ['test.py']
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename not in skip_files:
            await bot.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_ready():
    await load()
    print('Bot is ready.')


bot.run('OTg4MzkzNjM2MTA4NTc0NzQw.GcM70T.4PD_N4yOwzTW5tn12LGPGazSedaHiRFENNCZbs')
