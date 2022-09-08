import os

from dotenv import load_dotenv
load_dotenv()

from clients.discord_client import client

TOKEN = os.getenv('BOT_TOKEN', None);

client.run(TOKEN)
