# bot file
import os
from discord.ext import commands

import secret

TOKEN = secret.TOKEN

client = commands.Bot(command_prefix="!")

for filename in os.listdir('bot/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
