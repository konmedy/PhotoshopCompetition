import re
import shutil
import time

import discord
from discord.ext import commands
import asyncio
import logging
import random
import http

from pip._vendor import requests

bot = commands.Bot(command_prefix="!")
submitted1time = []
submitted2times = []
submitted3times = []
competition = True


bot.remove_command('help')

@bot.event
async def on_ready():
    print('hi {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Streaming(name="ROBLOX Sadge", url="https://twitch.tv/mrpillow5"))

@bot.command()
async def open(ctx):
    owner = await bot.fetch_user(user_id=459773410285846558)
    rock = await bot.fetch_user(user_id=168731800963645440)
    if ctx.author == owner or ctx.author == rock:
        embedVoteOpenedReturnMsg = discord.Embed(title="OK", description="The Photoshop Competiton has been opened!.",
                                        color=0x00ff00)
        await ctx.channel.send(embed=embedVoteOpenedReturnMsg)
        global competition
        competition = True
    else:
        embedNotOwner = discord.Embed(title="Not Bot Developer", description="Only Konmedy can open the competition since he's, you know, the bot developer.", color=0xff0000)
        await ctx.channel.send(embed=embedNotOwner)
        return

@bot.command()
async def close(ctx, areyousure: str = "not sure"):
    owner = await bot.fetch_user(user_id=459773410285846558)
    rock = await bot.fetch_user(user_id=168731800963645440)
    if ctx.author == owner or ctx.author == rock:
        if areyousure == "not sure":
            embedAreYouSure = discord.Embed(title="Are you sure?",
                                          description="Are you sure you want to close the submissions?\n\nTo confirm, do: **!close yes**",
                                          color=0x00ff00)
            await ctx.channel.send(embed=embedAreYouSure)
        elif areyousure.lower() == "yes":
            embedVotesClosed = discord.Embed(title="OK",
                                          description="OK. The votes have been closed. Thank you to all of the participants!",
                                          color=0x00ff00)
            await ctx.channel.send(embed=embedVotesClosed)
            competition = False
        else:
            embedAreYouSure = discord.Embed(title="Are you sure?",
                                          description="Are you sure you want to close the submissions?\n\nTo confirm, do: **!close yes**",
                                          color=0x00ff00)
            await ctx.channel.send(embed=embedAreYouSure)
    else:
        embedNotOwner = discord.Embed(title="Not Bot Developer", description="Only Konmedy can close the submissions since he's, you know, the bot developer.", color=0xff0000)
        await ctx.channel.send(embed=embedNotOwner)
        return

@bot.command()
async def instructions(ctx):
    print("useless command, thrown out until purpose found.")

@bot.event
async def on_message(message):
    submissionchannel = bot.get_channel(781178207436275773)
    if message.author == bot.user:
        return
    if competition == True:
        if message.channel.id == 781177387143659610:
            if message.attachments:
                if message.author.id not in submitted1time:
                    embedSubmission = discord.Embed(title=f"Submission", description=f"Author: ||{message.author}|| (1/3)\nThis person still can submit 2 entries.\n", color=0x00ff00)
                    f = await message.attachments[0].to_file()
                    embedSubmission.set_image(url=f"attachment://{f.filename}")
                    await submissionchannel.send(file=f, embed=embedSubmission)
                    await message.delete()
                    submitted1time.append(message.author.id)
                    return
                if message.author.id not in submitted2times:
                    embedSubmission = discord.Embed(title=f"Submission", description=f"Author: ||{message.author}|| (2/3)\nThis person still can submit 1 more entries.\n", color=0x00ff00)
                    f = await message.attachments[0].to_file()
                    embedSubmission.set_image(url=f"attachment://{f.filename}")
                    await submissionchannel.send(file=f, embed=embedSubmission)
                    await message.delete()
                    submitted2times.append(message.author.id)
                    return
                if message.author.id not in submitted3times:
                    embedSubmission = discord.Embed(title=f"Submission", description=f"Author: ||{message.author}|| (3/3)\n**This person can't submit any entries anymore.**\n", color=0x00ff00)
                    f = await message.attachments[0].to_file()
                    embedSubmission.set_image(url=f"attachment://{f.filename}")
                    await submissionchannel.send(file=f, embed=embedSubmission)
                    await message.delete()
                    submitted3times.append(message.author.id)
                    return
                else:
                    embed3 = discord.Embed(title=f"No more entries!", description=f"You've already submitted 3 entries. **You can't submit any more entries.**", color=0xff0000)
                    try:
                        await message.author.send(embed=embed3)
                    except:
                        pass
                    await message.delete()
            else:
                embedAttachmentsOnly = discord.Embed(title="Error",
                                                     description="Your submission has to be an attachment. The bot doesn't support URL's, but maybe in the future, when Konmedy becomes a decent programmer...\n\nAlso make sure that you don't add any text to the message.",
                                                     color=0xff0000)
                try:
                    await message.author.send(embed=embedAttachmentsOnly)
                except:
                    pass
                await message.delete()
    else:
        if message.channel.id == 781177387143659610:
            await message.delete()
            embedNotOpen = discord.Embed(title=f"Not open yet!",
                                   description=f"The Photoshop Competition entries aren't open yet.",
                                   color=0xff0000)
            await message.author.send(embed=embedNotOpen)
    await bot.process_commands(message)
bot.run("put token here")
