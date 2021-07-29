import random

import discord
from discord.ext import commands


    class BotCommands(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
            self._last_member = None

    @commands.Cog.listener()
    async def on_message(self, message):

        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            'Cool. Cool cool cool cool cool cool cool, \n'
            'no doubt no doubt no doubt no doubt.',
            'If I die, turn my tweets into a book.',
            'Title of your sex tape.',
            'Jake, piece of advice: just give up. It’s the Boyle way. It’s why our family crest is a white flag.',
            'https://media.giphy.com/media/KAKgpCLJDnzeU/giphy.gif'
            'https://media.giphy.com/media/3o7btPYdF4ZHHgMfGU/giphy.gif'
            'https://media.giphy.com/media/WtUcYhTcrtVWwiD7bG/giphy.gif'
            'https://media.giphy.com/media/3oxHQJ7mvPjceguBna/giphy.gif'
            'https://media.giphy.com/media/3o7abCSdg4TkLA6V1K/giphy.gif'
        ]

        sad_responses = [
            'Everything is going to be aright :)',
            'https://media.giphy.com/media/W1GG6RYUcWxoHl3jV9/giphy.gif',
            'https://media.giphy.com/media/SQHZfImZYdz8AwUCMr/giphy.gif',
            'https://media.giphy.com/media/ayQ99hp01HFN6/giphy.gif'
        ]

        happy_responses = [
            'LETS GOOOO!',
            'https://media.giphy.com/media/GcO6KBd1C16F2/giphy.gif',
            'https://media.giphy.com/media/xT5LMHxhOfscxPfIfm/giphy.gif',
            'https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif',
            'https://cdn.discordapp.com/emojis/821935095355146291.gif?size=64'
        ]

        if message.content == '99!':
            response = random.choice(brooklyn_99_quotes)
            await message.channel.send(response)
        elif any(word in message.content for word in ['sad', 'depressed', 'unhappy', 'miserable', 'dejected']):
            response = random.choice(sad_responses)
            await message.channel.send(response)
        elif any(word in message.content for word in ['happy', 'hyped', 'excited', 'ecstatic', 'thrilled']):
            response = random.choice(happy_responses)
            await message.channel.send(response)

        await self.bot.process_commands(message)

        @commands.Cog.listener()
        async def on_ready(client):
            print(f'{client.user.name} has connected to Discord!')

        @commands.Cog.listener()
        async def on_member_join(member):
            await member.create_dm()
            await member.dm_channel.send(
                f'Hi {member.name}, welcome to my Discord server!'
            )


def setup(bot):
    bot.add_cog(BotCommands(bot))
