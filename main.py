import discord
import os
import random
from discord.ext import commands

client = commands.Bot(command_prefix="%", self_bot=True, help_command=None)
f = open("token.txt","r")
token = f.read()
f.close()

toiletlist = ["future","smmono9","standard"]
boxeslist = ["ada-box","ada-cmt","boxquote","boy","c","c-cmt","caml","capgirl","cat","columns","diamonds","dog","f90-box","face","girl","html","ian_jones","important","jstone","mouse","nuke","peek","right","santa","scroll","shell","spring","unicornsay","unicornthink","whirly","xes"]
print(os.popen('echo 92#6163 | toilet -f ' + str(toiletlist[random.randint(0,len(toiletlist)-1)]) + ' | boxes -d ' + str(boxeslist[random.randint(0,len(boxeslist)-1)]) + ' | lolcat').read())

@client.event
async def on_ready ():
    print("Starting selfbot NOW!")

@client.command()
async def e(ctx, *args):
    #await ctx.send('> executing {}'.format(' '.join(args)))
    p = '{}'.format(' '.join(args))
    out = os.popen('cd && ' + p)
    print(out)
    await ctx.send(f"```{out.read()}```")

client.run(token, bot=False
