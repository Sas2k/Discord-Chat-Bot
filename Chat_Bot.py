import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
help = '''##################################
Bot help: Go to the bot command channel
##################################
'''
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    monkeyman_quotes = [
        'I am the monkeyman!!',
        'The Person Who Created Me is not the monkeyman!!',
        'The Person Who Created Me is the monkeyman!!',
        'Everyone is the monkeyman!!',
        'Nobody is the monkey man!!'
    ]
    chessl = [
        'That ain\'t a queens gambit to me',
        'CHECK MATE,CHECK MATE, CHECK MATE!!',
        'Take the QUEEN!!!',
        'Hmmm Go Ask the sir for advice'
    ]
    semi_colon = [
        'semi-colon on the ;oose',
        ';',
        'there is the semi-colon capture it!!',
        'The Semi-colon is no where to be found....;..',
        ''':::::::::::::::::::::::;:::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::
        oh dear where is it?......
        ''',
    ]
    backslash = [
        'on the end of the sentence there is a/',
        'this/that or that/this'
    ]

    if message.content == 'monkeyman!':
        response = random.choice(monkeyman_quotes)
        await message.channel.send(response)
    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')
    if 'chess' in message.content.lower():
        chess = random.choice(chessl)
        await message.channel.send(chess)
    if ';' in message.content.lower():
        sc = random.choice(semi_colon)
        await message.channel.send(sc)
    if '/' in message.content.lower():
        bs = random.choice(backslash)
        await message.channel.send(bs)
    if message.content == 'dice':
        dice = random.randint(1, 6)
        dice = str(dice)
        await message.channel.send(dice)
    if message.content == 'chelp':
        await message.channel.send(help)
client.run('####your bot id goes here####')
