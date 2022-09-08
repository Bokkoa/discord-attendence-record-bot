import discord

from datetime import datetime

from clients.mongo_client import insert_attendence

ATTENDENCE_CHANNEL = 'experimental'
COFFEE_EMOJI = u"\u2615"
STATUS = ('available', 'unavailable')

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    # Avoid infinite loop self response
    if (message.author == client.user):
        return
    
    if (message.channel.name == ATTENDENCE_CHANNEL):

        if ( user_message.lower() == STATUS[0]):
            insert_attendence(username, datetime.now(), STATUS[0])
            await message.add_reaction(COFFEE_EMOJI)
            return

        elif (user_message.lower() == STATUS[1]):
            insert_attendence(username, datetime.now(), STATUS[1])
            await message.add_reaction(COFFEE_EMOJI)
            return
