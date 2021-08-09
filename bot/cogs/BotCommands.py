import random

import requests
from discord.ext import commands

import secret


class BotCommands(commands.Cog):

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

        eight_ball_responses = [
            'Yes',
            'No',
            'Yes, if Godzilla wills it.',
            'No... I mean yes... Well... Ask again later',
            'The answer is unclear... Seriously I double checked.',
            'Probably.',
            'Of course.',
            'I HIGHLY doubt it.',
            'Ask yourself this question in the mirror three times, the answer will become clear',
            'You want an answer? OK, here\'s your answer:'
        ]

        if message.content == '99!':
            response = random.choice(brooklyn_99_quotes)
            await message.channel.send(response)
        elif message.content.lower().startswith("!8ball"):
            response = random.choice(eight_ball_responses)
            await message.channel.send(response)
        elif any(word in message.content for word in [' sad', ' depressed', ' unhappy', ' miserable', ' dejected']):
            response = random.choice(sad_responses)
            await message.channel.send(response)
        elif any(word in message.content for word in [' happy', ' hyped', ' excited', ' ecstatic', ' thrilled']):
            response = random.choice(happy_responses)
            await message.channel.send(response)
        elif message.content.lower().startswith("!weather"):
            city = message.content[slice(9, len(message.content))].lower()
            result = await self.get_weather(city)
            await message.channel.send(result)
        elif message.content.lower().startswith("!commands"):
            result = 'Magic 8 Ball: !8ball <Question you would like answered>\n\n Get current weather: !weather <City> ' \
                     '\n\nRandom Brooklyn 99 quotes and GIFs: 99!\n\n Play music in voice channel(User must be in ' \
                     'voice ' \
                     'channel):\n !play <song name>, !stop, !pause, !queue\n\n Random Background Generator: \n ' \
                     '!background1080, !background1080vertical, !background1440, !background1440vertical \n 1080 and ' \
                     '1440 will ' \
                     'generate a 1080p or 1440p background, and vertical means it is made for vertical monitors. '
            await message.channel.send(result)
        elif any(word in message.content for word in ['!background1080', '!background1080vertical',
                                                      '!background1440vertical', '!background1440']):
            backs = message.content
            result = await self.background(backs)
            await message.channel.send(result)

        @commands.Cog.listener()
        async def on_ready(client):
            print(f'{client.user.name} has connected to Discord!')

        @commands.Cog.listener()
        async def on_member_join(member):
            await member.create_dm()
            await member.dm_channel.send(
                f'Hi {member.name}, welcome to my Discord server!'
            )

    @commands.Cog.listener()
    async def get_weather(self, city):

        api_key = secret.api_key
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        complete_url = base_url + "?q=" + city + "&appid=" + api_key
        print(complete_url)
        weather_response = requests.get(complete_url)

        x = weather_response.json()
        if x["cod"] != "404":

            y = x["main"]

            current_temperature = round(y["temp"] - 273.15)

            current_pressure = y["pressure"]

            current_humidity = y["humidity"]

            z = x["weather"]

            weather_description = z[0]["description"]

            current_weather = (" Temperature = " +
                               str(current_temperature) + "°C" +
                               "\n Atmospheric Pressure = " +
                               str(current_pressure) + " hPa" +
                               "\n Humidity = " +
                               str(current_humidity) + "%" +
                               "\n Description = " +
                               str(weather_description))

        else:
            print(" City Not Found ")

        return current_weather

    @commands.Cog.listener()
    async def background(self, backs):

        if backs == '!background1080':
            return "https://source.unsplash.com/random/1920x1080"
        elif backs == '!background1080vertical':
            return "https://source.unsplash.com/random/1080x1920"
        elif backs == '!background1440':
            return "https://source.unsplash.com/random/2560x1440"
        elif backs == '!background1440vertical':
            return "https://source.unsplash.com/random/1440x2560"


def setup(bot):
    bot.add_cog(BotCommands(bot))
