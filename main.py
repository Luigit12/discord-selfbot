import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="%", self_bot=True, help_command=None)
f = open("token.txt","r")
token = f.read()
f.close()

print(os.popen('echo 92#6163 | figlet | boxes -d unicornsay | lolcat').read())

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

client.run(token, bot=False)
