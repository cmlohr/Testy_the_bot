import os
import discord
import requests
import json
import random
import hello
from datetime import datetime
import pytz




tz_central = pytz.timezone('America/Chicago') 
time_central = datetime.now(tz_central)
print("NY: ", time_central.strftime("%H:%M"))

tz_London = pytz.timezone('Europe/London')
time_London = datetime.now(tz_London)
print("London: ", time_London.strftime("%H:%M"))



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

    if message.content.startswith("$What time is it in London?"):
        await message.channel.send(time_London.strftime("%H:%M"))
    if message.content.startswith("$London time?"):
        await message.channel.send(time_London.strftime("%H:%M"))

    if message.content.startswith("$London time"):
        await message.channel.send(time_London.strftime("%H:%M"))


    if message.content.startswith("$What time is it in New Orleans?"):
        await message.channel.send(time_central.strftime("%H:%M"))

    if message.content.startswith("$What time is it in Chicago?"):
        await message.channel.send(time_central.strftime("%H:%M"))
    
    if message.content.startswith("$What time is it for you Testy?"):
        await message.channel.send(time_central.strftime("%H:%M"))

    if message.content.startswith("$Testy time?"):
        await message.channel.send(time_central.strftime("%H:%M"))
    if message.content.startswith("$Testy time"):
        await message.channel.send(time_central.strftime("%H:%M"))

    if message.content.startswith("$Chicago time?"):
        await message.channel.send(time_central.strftime("%H:%M"))
    if message.content.startswith("$Chicago time"):
        await message.channel.send(time_central.strftime("%H:%M"))

    if message.content.startswith("$New Orleans time?"):
        await message.channel.send(time_central.strftime("%H:%M"))

    if message.content.startswith("$New Orleans time"):
        await message.channel.send(time_central.strftime("%H:%M"))  

    # if message.content.startswith('$'):
    #     await message.channel.send('Hello C')

    if message.content.startswith('$cats?'):
        await message.channel.send('Today I learned this about cats: ' + get_quote())

    if message.content.startswith("$joke"):
        await message.channel.send(get_joke())


client.run(my_secret)
