import os
import discord
import requests
import json
import random


def get_quote():
    response = requests.get("https://cat-fact.herokuapp.com/facts")
    this_json = json.loads(response.text)
    random_fact = random.randrange(0, len(this_json))
    print(this_json)
    return this_json[random_fact]['text']

my_secret = os.environ['TOKEN']
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in a {0.user}.'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Yo!')

    if message.content.startswith('$my_name_is_C'):
        await message.channel.send('Hello C')

    if message.content.startswith('$cats?'):
        await message.channel.send(get_quote())


client.run(my_secret)
