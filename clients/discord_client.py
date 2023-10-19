import discord
import os
from datetime import datetime

from clients.mongo_client import insert_attendence

ATTENDENCE_CHANNEL = os.getenv('DISCORD_CHANNEL', None);

COFFEE_EMOJI = u"\u2615"
STATUS = ('available', 'unavailable')
STATUS_OFFLINE = 'offline'
STATUS_ONLINE = 'online'

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    desktop_status = message.author.desktop_status
    web_status = message.author.web_status
    # print(f'{username}: {user_message} ({channel})')
    # print(f'{message.author.status}')
    # print(f'{message.author.is_on_mobile()}')

    IS_JUST_ONLINE_IN_MOBILE = (
                message.author.is_on_mobile() and
                STATUS_OFFLINE in str(desktop_status) and 
                STATUS_OFFLINE in str(web_status)
                )

    # Avoid infinite loop self response
    if (message.author == client.user):
        return
    
    if (message.channel.name == ATTENDENCE_CHANNEL):

        if ( user_message.lower() == STATUS[0]):

            # Checking if someone post in mobile device
            if IS_JUST_ONLINE_IN_MOBILE:
                await message.delete()
                return await message.channel.send(f"{message.author.mention} trató de marcar asistencia desde el celular en home office. Se está haciendo wey xd!")

            # insert_attendence(username, datetime.now(), STATUS[0])
            await message.add_reaction(COFFEE_EMOJI)
            return

        elif (user_message.lower() == STATUS[1]):
            # insert_attendence(username, datetime.now(), STATUS[1])
            await message.add_reaction(COFFEE_EMOJI)
            return
