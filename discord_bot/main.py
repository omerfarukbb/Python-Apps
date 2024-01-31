from dotenv import load_dotenv 
from utils import get_response
from discord import Intents, Client
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SURAHS = {}

# Configuration for surahs
text_url = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'surah_names.txt')
with open(text_url, 'r', encoding='utf-16') as file:
    for surah_number in range(1, 115):  # Adjusted the range to include 114
        surah_name = file.readline().strip()  # Read each line separately and strip whitespace
        SURAHS[surah_name.lower()] = surah_number


# Configuration for api
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

# Message functionality
async def send_message(message, user_message):
    if not user_message:
        print('Message was empty!')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    try:
        response = get_response(user_message, SURAHS)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)
        
@client.event
async def on_ready():
    print(f'{client.user} is now running.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)
    
    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)
    
def main():
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()