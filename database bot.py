import discord
from discord.ext import commands
from time import sleep
import os
import datetime
import wget
import threading
from zipfile import ZipFile
from pathlib import Path
import shutil

def closefile():
    sleep(300)
    if os.path.exists(finalfilepath):
        os.remove(finalfilepath)
    else:
        pass
    


client = commands.Bot(command_prefix='.')


@client.command() 
async def addcharacter(ctx):
    await ctx.send("adding to database please wait")
    try:
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
    except Exception:
        await ctx.send("something went wrong! this probably means you didn't attach a file or discord api is broken")


@client.command()     
async def addsound(ctx):
    await ctx.send("adding to database please wait")
    try:
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
    except Exception:
        await ctx.send("something went wrong! this probably means you didn't attach a file or discord api is broken")

@client.command()     
async def setip(ctx):
    ip = userInput = ctx.message.content[7:]
    with open("public/serverlist.txt", "w+") as hisc:
        hisc.write(str(ip)+":best bois courthouse")
    await ctx.send("changed ip to "+str(ip))

@client.command()     
async def getchrasset(ctx):
    weburl = ctx.message.content[13:]
    betterweburl = weburl.replace(" ", "%20")
    await ctx.send("http://fierce-push.auto.playit.gg:53368/singlecharacter/"+str(betterweburl))

@client.command()     
async def getsound(ctx):
    sound = ctx.message.content[10:]
    bettersound = sound.replace(" ", "%20")
    await ctx.send("http://fierce-push.auto.playit.gg:53368/singlesound/"+str(bettersound))

@client.command()     
async def downloadcharacter(ctx):
    filepath = ctx.message.content[19:]
    fullfilepath = 'public/singlecharacter/'+str(filepath)
    if os.path.isdir(fullfilepath):
      shutil.make_archive(fullfilepath, 'zip', fullfilepath)
      global finalfilepath
      finalfilepath = str(fullfilepath)+'.zip'
      if Path(fullfilepath).stat().st_size > 7823:
          urlpath = finalfilepath.replace(" ", "_")
          os.rename(finalfilepath,urlpath)
          await ctx.send("http://fierce-push.auto.playit.gg:53368/"+str(urlpath))
          await ctx.send("note: this link will become invalid in 5 minutes")
          delfile = threading.Thread(target=closefile)
          delfile.start()
      else:
          await ctx.send(file=discord.File(str(finalfilepath)))  
          if os.path.exists(finalfilepath):
             os.remove(finalfilepath)
          else:
            pass
    else:
        await ctx.send("sorry, but thats not a character in my database") 

    
client.run('botid')
