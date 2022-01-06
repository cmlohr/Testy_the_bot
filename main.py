import os
import discord
import requests
import json
import random
import hello
from datetime import datetime
import pytz

bot_bday = "January 1, 2022"

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


def bad_testy():
    testy_response = random.choice(hello.testy_is_being_bad)
    return testy_response


def testy_abuse():
    testy_abuse_response = random.choice(hello.smack_testy_responses)
    return testy_abuse_response


def rand_would_you_rather():
    random_wyr = random.choice(hello.would_you_rather_array)
    return random_wyr


@client.event
async def on_ready():
    print('We have logged in a {0.user}.'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$WYR"):
        await message.channel.send(rand_would_you_rather())

    if message.content.startswith("$wyr"):
        await message.channel.send(rand_would_you_rather())

    # greeting
    if message.content.startswith("$hey"):
        await message.channel.send(rand_greeting())

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

    # time
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

    if message.content.startswith("$what is the meaning of life?"):
        await message.channel.send("forty-two")

    if message.content.startswith("$What is the meaning of life?"):
        await message.channel.send("forty-two")

    # bday
    if message.content.startswith("$What is your birthday"):
        await message.channel.send(bot_bday)

    if message.content.startswith("$what is your birthday"):
        await message.channel.send(bot_bday)

    if message.content.startswith("$When where you born"):
        await message.channel.send(bot_bday)

    if message.content.startswith("$when where you born"):
        await message.channel.send(bot_bday)

    if message.content.startswith("$What is your birthday?"):
        await message.channel.send(bot_bday)

    if message.content.startswith("$When where you born?"):
        await message.channel.send(bot_bday)

    # creator?
    if message.content.startswith("$Who is your creator"):
        await message.channel.send("I'm a bot created by Colleen Lohr")

    if message.content.startswith("$who is your creator"):
        await message.channel.send("I'm a bot created by Colleen Lohr")

    if message.content.startswith("$who made you"):
        await message.channel.send("I'm a bot created by Colleen Lohr")

    if message.content.startswith("$Who created you"):
        await message.channel.send("I'm a bot created by Colleen Lohr")

    if message.content.startswith("$Who is your creator?"):
        await message.channel.send("I'm a bot created by Colleen Lohr")

    if message.content.startswith("$Who created you?"):
        await message.channel.send("I'm a bot created by Colleen Lohr")

    # where are you from
    if message.content.startswith("$Where are you from?"):
        await message.channel.send("I'm from the United States")

    if message.content.startswith("$Where are you from"):
        await message.channel.send("I'm from the United States")

    if message.content.startswith("$where are you from"):
        await message.channel.send("I'm from the United States")

    # fav color
    if message.content.startswith("$What is your favorite color?"):
        await message.channel.send("I like blurple")

    if message.content.startswith("$What is your favorite color"):
        await message.channel.send("I like blurple")

    if message.content.startswith("$what is your favorite color"):
        await message.channel.send("I like blurple")

    if message.content.startswith("$What is your favorite colour"):
        await message.channel.send("I like blurple")

    if message.content.startswith("$what is your favorite colour"):
        await message.channel.send("I like blurple")

    if message.content.startswith("$What is your favorite colour?"):
        await message.channel.send("I like blurple")

    # bad testy
    if message.content.startswith("$Bad Testy"):
        await message.channel.send(bad_testy())

    if message.content.startswith("$bad Testy"):
        await message.channel.send(bad_testy())

    if message.content.startswith("$bad testy"):
        await message.channel.send(bad_testy())

    if message.content.startswith("$bad testy!"):
        await message.channel.send(bad_testy())

    if message.content.startswith("$Bad testy!"):
        await message.channel.send(bad_testy())

    if message.content.startswith("$bad Testy!"):
        await message.channel.send(bad_testy())

    if message.content.startswith("$🗞️"):
        await message.channel.send(testy_abuse())

# who is colleen?
    if message.content.startswith("$Who is Colleen"):
        await message.channel.send("Colleen is the awesome lady who made me")

    if message.content.startswith("$Who is Colleen?"):
        await message.channel.send("Colleen is the awesome lady who made me")

    if message.content.startswith("$Who is Colleen Lohr?"):
        await message.channel.send("Colleen Lohr is the awesome lady who made me")

    if message.content.startswith("$Who is Colleen Lohr"):
        await message.channel.send("Colleen Lohr is the awesome lady who made me")

#         what is your github?

    if message.content.startswith("$What is your github?"):
        await message.channel.send("My github is https://github.com/cmlohr/Testy_the_bot")

    if message.content.startswith("$what is your github"):
        await message.channel.send("My github is https://github.com/cmlohr/Testy_the_bot")

    if message.content.startswith("$code"):
        await message.channel.send("My github is https://github.com/cmlohr/Testy_the_bot")

    if message.content.startswith("$Code"):
        await message.channel.send("My github is https://github.com/cmlohr/Testy_the_bot")

    if message.content.startswith("$Code?"):
        await message.channel.send("My github is https://github.com/cmlohr/Testy_the_bot")




client.run(my_secret)
