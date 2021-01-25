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
async def save(ctx):
    await ctx.message.attachments[0].save("newcharacter.zip")
                                         
    await ctx.send("adding to database please wait")
    zf = ZipFile('newcharacter.zip', 'r')
    zf.extractall('a')
    zf.extractall('b')
    zf.close()
    shutil.make_archive('a/test', 'zip', 'a')
    await ctx.send("added to database")
    
client.run('NzUyMjUxMDU4OTA2MjAyMTQy.X1U6ZA.cIkHHcZIqAm-Xg3W_3DlOcTuvSA')
