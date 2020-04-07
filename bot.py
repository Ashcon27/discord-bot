import os
#from dotenv import load_dotenv

import discord
from discord.ext import commands


#load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.listen()
async def on_ready():
    print('Bot loaded and ready!')

@bot.command(name="hi", help="Says hello")
async def say_hello(ctx):
    await ctx.send(f"Hello {ctx.author.display_name}")
   
@bot.command(name="create", help="basic info for poll")
async def creator(ctx):
    await ctx.send(f"Hi{ctx.author.display_name}. Let's create a poll! Type .title")
          
@client.event
async def on_message(message):
    if message.content.startswith(".title"):
        await client.send_message(message.channel, message.content[6:])
        
bot.run(TOKEN)


