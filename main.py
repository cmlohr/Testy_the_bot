import os
import discord
import requests
import json
import random
import hello
import time

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%H:%M", named_tuple)

print(time_string)


my_secret = os.environ['TOKEN']
client = discord.Client()


def get_quote():
    response = requests.get("https://cat-fact.herokuapp.com/facts")
    this_json = json.loads(response.text)
    random_fact = random.randrange(0, len(this_json))
    print(this_json)
    return this_json[random_fact]['text']

def get_joke():
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    this_joke = json.loads(response.text)
    print(this_joke)
    return this_joke['joke']

    
# def check_hello():
#     is_hello = random.choice(hello.hello_check)
#     print(is_hello)
#     print(type(is_hello))
#     return is_hello

def rand_greeting():
    random_hello = random.choice(hello.greetings)
    return random_hello

def rand_8ball():
    random_8ball = random.choice(hello.predictions_8ball)
    return random_8ball

@client.event
async def on_ready():
    print('We have logged in a {0.user}.'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hey"):
        await message.channel.send(rand_greeting())

    if message.content.startswith("$8ball"):
        await message.channel.send(rand_8ball())

    if message.content.startswith("$hello"):
        await message.channel.send(rand_greeting())

    if message.content.startswith("$Hi"):
        await message.channel.send(rand_greeting())

    if message.content.startswith("$Hey"):
        await message.channel.send(rand_greeting())

    if message.content.startswith("$Hello"):
        await message.channel.send(rand_greeting())

    if message.content.startswith("$hi"):
        await message.channel.send(rand_greeting())

    if message.content.startswith("$hello testy"):
        await message.channel.send(rand_greeting())

    if message.content.startswith("$hello Testy"):
        await message.channel.send(rand_greeting())

    if message.content.startswith("$time"):
        await message.channel.send("It is " + time_string + " here")
    # if message.content.startswith('$'):
    #     await message.channel.send('Hello C')

    if message.content.startswith('$cats?'):
        await message.channel.send('Today I learned this about cats: ' + get_quote())

    if message.content.startswith("$joke"):
        await message.channel.send(get_joke())


client.run(my_secret)
