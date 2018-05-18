import logging
import config
import discord

client = discord.Client()

# Set up logging, code snippet below is from discord.py documentation
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@client.event
async def on_ready():
    print('Connected ' + client.user.name + '!')

@client.event
async def on_message(message):
    text = message.content
    if text.startswith('-delete '):
        # Delete past n number of messages by the user
        # Example:
        # -delete 7
        num_msgs = int(text[8:])
        async for msg in client.logs_from(message.channel, limit=num_msgs):
            if msg.author == client.user:
                await client.delete_message(msg)
    elif text.startswith('-edit '):
        # Edit the last message by the user with new text
        # Example:
        # -edit replace it with this
        new_content = text[6:]
        counter = 0
        async for msg in client.logs_from(message.channel, limit=2):
            counter += 1
            if counter == 2:
                await client.edit_message(msg, new_content)
        await client.delete_message(message)

@client.event
async def on_message_delete(message):
    if message.author == client.user:
        print('Deleted:\n\t' + message.content)

@client.event
async def on_message_edit(before, after):
    if after.author == client.user:
        print('Edited:\n\tBefore: ' + before.content +
              '\n\tAfter: ' + after.content)

client.run(config.TOKEN, bot=False)
