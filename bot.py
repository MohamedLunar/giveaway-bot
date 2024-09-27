import discord
from discord.ext import commands
import asyncio
import random

# Define intents
intents = discord.Intents.default()
intents.messages = True  # Enable message content intent
intents.message_content = True  # For message content access in guilds
intents.reactions = True
intents.guilds = True

# Initialize the bot with the new prefix
bot = commands.Bot(command_prefix='g', intents=intents)

@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.watching, name="Made By MohamedLunar")
    await bot.change_presence(activity=activity)
    print(f'Logged in as {bot.user} successfully')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
           await ctx.send("I don't have enough permissions to run this command!")
    elif isinstance(error, commands.BotMissingPermissions):
           await ctx.send("I am missing some permissions in this server!")
    else:
           await ctx.send(f"An error occurred: {error}")

@bot.command(name='!help')
async def help(ctx):
    embed = discord.Embed(title="Giveaway Help Menu", description=f'```g!start <duration> <prize>```', color=0x00FF00)
    await ctx.send(embed=embed)

@bot.command(name='!start')
async def start_giveaway(ctx, duration: int, *, prize: str):
    embed = discord.Embed(title='ðŸŽ‰ Giveaway ðŸŽ‰', description=f'Prize: {prize}', color=0x00ff00)
    embed.add_field(name='Hosted by:', value=ctx.author.mention)
    embed.add_field(name='Ends in:', value=f'{duration} seconds')
    embed.set_footer(text='React with ðŸŽ‰ to enter!')
    giveaway_message = await ctx.send(embed=embed)
    await giveaway_message.add_reaction('ðŸŽ‰')
    
    await asyncio.sleep(duration)
    
    giveaway_message = await ctx.channel.fetch_message(giveaway_message.id)
    users = [user async for user in giveaway_message.reactions[0].users()]
    users.remove(bot.user)  # Remove bot from the list
    
    if len(users) > 0:
        winner = random.choice(users)
        await ctx.send(f'ðŸŽ‰ Congratulations {winner.mention}, you won the **{prize}**!')
    else:
        await ctx.send('ðŸŽ‰ No one participated in the giveaway.')

# Remember to replace 'YOUR_BOT_TOKEN' with your bot's token
token = os.getenv("TOKEN")
bot.run(token)