import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is Ready!!')

@client.event
async def on_message(message):
    headorTails = ['heads', 'tails']
    #Declaring number of messages, as it increments depending on the number of messages purged
    numberofMsg = 0
    randomCoin = random.randint(0,1)
    flipCoin = headorTails[1]
    
    #
    
    if message.content.lower().startswith('.help'):
        userID = message.author.id
        await client.send_message(message.channel, '```Requested by <@%s> .role ```' % (userID))
    if message.content.lower().startswith('.role'):
        await client.send_message(message.channel, '```European \t Asian```')
    if message.content.lower().startswith('.european'):
        roleEuropean = discord.utils.get(message.server.roles, id='502368967189331989')
        await client.add_roles(message.author, roleEuropean)
    if message.content.lower().startswith('.asian'):
        roleAsian = discord.utils.get(message.server.roles, id='502369003650416642')
        await client.add_roles(message.author, roleAsian)
            
    
    
            
            



client.run('NTAyMzY3NDk4OTM5NjYyMzM2.Dqm6DA.41jXtnvc6Xku43kVSedHFw5qVQs')
