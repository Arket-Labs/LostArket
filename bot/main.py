# -*-coding:utf-8-*-

import discord
import os
import urllib.request
import json
import codecs
import googletrans

from discord.ext import commands
from bs4 import BeautifulSoup
from urllib import parse
from urllib.request import FancyURLopener

client = commands.Bot(command_prefix=".")
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready() :
    await client.change_presence(activity = discord.Activity(type=discord.ActivityType.listening, name="the song of my people"))
    print("LostArket is now online")

@client.command()
async def ping(ctx) :
    await ctx.send(f"Pong with {str(round(client.latency, 2))}")

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@client.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)
    print

@client.command()
async def hello(ctx) :
    await ctx.send(f"hello!")

@client.command()
async def pop(ctx) :
    await ctx.send('https://cdn.discordapp.com/emojis/853465836005621791.gif?v=1')

@client.command()
async def gay(ctx) :
    await ctx.send('https://cdn.discordapp.com/emojis/867499156837498950.gif?v=1')

@client.command()
async def translate(ctx, destLang=None, txt=None) :
    if txt == None or destLang == None:
        await ctx.send(googletrans.LANGUAGES)
    else:
        try:
            translator = googletrans.Translator()
            trans = translator.translate(txt, dest = destLang);
            await ctx.send(trans.text + "\n_" + trans.pronunciation + "_")
        except:
            await ctx.send("Could not translate to '" + destLang + "'")

@client.command()
async def events(ctx) :
    url = "http://m.inven.co.kr/lostark/timer/"
    req = urllib.request.urlopen(url)
    res = req.read()
    soup = BeautifulSoup(res, 'html.parser')
    translator = googletrans.Translator()

    str = "```"
    header = "이제 곧 시작되는 10개의 캘린더입니다.\n"
    trans = translator.translate(header);
    str += trans.text

    tm = soup.find_all('a', class_='info')
    tm = [each_line.get_text().strip() for each_line in tm[:10]]
    en = ""
    english = translator.translate(tm)

    for eng in english:
        for j in eng.text.split('\n'):
            en += j + " - "
        en = en[:len(en) - 2]
        en += "\n"

    str += "\n"
    str += en
    str += "\n"
    str += header
    # Korean text
    for i in tm:
            for j in i.split("\n"):
                    str += j + " - "
            str = str[:len(str) - 2]

            str += "\n"
    str += "```"
    await ctx.send(str)

client.run(token)
