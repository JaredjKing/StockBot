from ast import ExceptHandler
import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response, file=discord.File(r'/Users/jaredking/Stock_bot/stock_plot.png'))
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = os.environ.get('bot_key')
    intent = discord.Intents.default()
    intent.members = True
    intent.message_content = True
    client = discord.Client(intents=intent)

    @client.event 
    async def on_ready():
        print(f'{client.user}is now running!')


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said:'{user_message}' ({channel})")
        
        if user_message[0] == '$':
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)

