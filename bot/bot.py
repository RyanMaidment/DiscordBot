# bot file
import os
from discord.ext import commands

TOKEN = 

bot = commands.Bot(command_prefix='!')

for filename in os.listdir('bot/cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)
