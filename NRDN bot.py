import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is Ready!!')

@client.event
async def on_message(message):
    headorTails = ['heads', 'tails']
    #Declaring number of messages, as it increments depending on the number of messages purged
    numberofMsg = 0
    randomCoin = random.randint(0,1)
    flipCoin = headorTails[randomCoin]
    
    #
    
    if message.content.lower().startswith('!help'):
        userID = message.author.id
        await client.send_message(message.channel, '```Requested by <@%s> \n!purge \t !say \n!flip ```' % (userID),)
    if message.content.lower().startswith('!purge'):
        if message.author.id == '300999039867158528':
            async for msg in client.logs_from(message.channel):
                await client.delete_message(msg)
                numberofMsg += 1
            await client.send_message(message.channel, 'Deleted %s messages' % (numberofMsg))
            time.sleep(0.5)
            async for lastmsg in client.logs_from(message.channel):
                await client.delete_message(lastmsg)
        else:
            await client.send_message(message.channel, 'You do not have permission')
    if message.content.lower().startswith('!flip'):
        await client.send_message(message.channel, 'Heads or Tails')
        if message.content.lower().startswith('heads'):
            if flipCoin == 'heads':
                await client.send_message(message.channel, 'You have won')
            else:
                await client.send_message(message.channel, 'Sorry,you lose')
        if message.content.lower().startswith('tails'):
            if flipCoin == 'tails':
                await client.send_message(message.channel, 'You have won')
            else:
                await client.send_message(message.channel, 'Sorry,you lose')
            



client.run('TOEKN')
