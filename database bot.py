import discord
from discord.ext import commands
from time import sleep
import os
import datetime
import wget
from zipfile import ZipFile
import shutil


client = commands.Bot(command_prefix='.')


@client.command() 
async def addcharacter(ctx):
    await ctx.send("adding to database please wait")
    await ctx.message.attachments[0].save("newcharacter.zip")
                                         
    zf = ZipFile('newcharacter.zip', 'r')
    zf.extractall('public/singlecharacter')
    zf.close()
    if os.path.exists("newcharacter.zip"):
        os.remove("newcharacter.zip")
    else:
        pass
    if os.path.exists("public/characters.zip"):
        os.remove("public/characters.zip")
    else:
        pass
    shutil.make_archive('public/characters', 'zip', 'public/singlecharacter')
    await ctx.send("added to database")


@client.command()     
async def addsound(ctx):
    await ctx.send("adding to database please wait")
    await ctx.message.attachments[0].save("newsound.zip")
                                         
    zf = ZipFile('newsound.zip', 'r')
    zf.extractall('public/singlesound')
    zf.close()
    if os.path.exists("newsound.zip"):
        os.remove("newsound.zip")
    else:
        pass
    if os.path.exists("public/sounds.zip"):
        os.remove("public/sounds.zip")
    else:
        pass
    shutil.make_archive('public/sounds', 'zip', 'public/singlesound')
    await ctx.send("added to database")

@client.command()     
async def setip(ctx):
    ip = userInput = ctx.message.content[7:]
    with open("public/serverlist.txt", "w+") as hisc:
        hisc.write(str(ip)+":best bois courthouse")
    await ctx.send("changed ip to "+str(ip))
    
client.run('botid')
