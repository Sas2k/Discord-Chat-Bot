import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
from WebApp import keep_Alive

load_dotenv()

bot = commands.Bot(command_prefix="!")
items = ['rock','paper','scissors']
rules = {'rock':'scissors','scissors':'paper','paper':'rock'}
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()
help = '''##################################
Bot help: Go to the bot command channel
##################################
'''
@bot.command(name="ping")
async def ping(ctx: commands.Context):
  await ctx.send(f"pong! {round(bot.latency * 1000)}ms")
@bot.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    Channel = bot.get_channel('923094490665848882')
    Text = "React to get a roll\n🔪 = imposters\n👨🏽‍💻 = Hecker\n✔ = Verified"
    Moji = await bot.send_message(Channel, Text)
    await bot.add_reaction(Moji, emoji='🔪, 👨🏽‍💻, ✔')

@bot.event
async def on_reaction_add(reaction, user):
  Channel = client.get_channel('923094490665848882')
  if reaction.message.channel.id != Channel:
    return
  if reaction.emoji == "🔪":
    Role = discord.utils.get(user.server.roles, name="imposters")
    await client.add_roles(user, Role)
  if reaction.emoji == "👨🏽‍💻":
    Role = discord.utils.get(user.server.roles, name="Hecker")
    await client.add_roles(user, Role)
  if reaction.emoji == "✔":
    Role = discord.utils.get(user.server.roles, name="Verified")
    await client.add_roles(user, Role)

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
    if message.content == '!rock':
        user_in = 'rock'
        computer_in = random.choice(items)
        if user_in == computer_in:
            await message.channel.send(f'We Drew')
        elif rules[user_in] == computer_in:
            await message.channel.send(f'you won player i choosed {computer_in}')
        else:
            await message.channel.send(f'I Won i chose {computer_in}')
        await message.channel.send(f"player: {user_in}, computer: {computer_in}")
    if message.content == '!paper':
        user_in = 'paper'
        computer_in = random.choice(items)
        if user_in == computer_in:
            await message.channel.send(f'We Drew')
        elif rules[user_in] == computer_in:
            await message.channel.send(f'you won player i choosed {computer_in}')
        else:
            await message.channel.send(f'I Won i chose {computer_in}')
        await message.channel.send(f"player: {user_in}, computer: {computer_in}")
    if message.content == '!scissors':
        user_in = 'scissors'
        computer_in = random.choice(items)
        if user_in == computer_in:
            await message.channel.send(f'We Drew')
        elif rules[user_in] == computer_in:
            await message.channel.send(f'you won player i choosed {computer_in}')
        else:
            await message.channel.send(f'I Won i chose {computer_in}')
        await message.channel.send(f"player: {user_in}, computer: {computer_in}")

keep_Alive()
client.run(TOKEN)