import discord
import os
from discord.ext import commands
f = open("token.txt","r")

client = commands.Bot(command_prefix="%", self_bot=True, help_command=None)
token = f.read()
f.close()

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
