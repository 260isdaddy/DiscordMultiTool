import discord
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions
import _asyncio

import sys
sys.path.append("C:\\Users\\bmood\\PycharmProjects\\PrivateItems\\")

import SteamInfoPuller
import Flip
from Flip import rsItem
import DiscordBotKey

client = discord.Client()
client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('idk wat dat'))
    print('Bot logging in as {0.user}'.format(client))

############COMMANDS###############################################################
@client.command()
async def ping(ctx):
    await ctx.channel.send("go away idiot (took {}".format(int(client.latency * 1000)) + "ms to flame.)")

@client.command()
async def rsitem(ctx, *item):
    item = (" ".join(item[:]))
    await ctx.channel.send(rsItem(item))


@client.command()
async def kill(ctx, amt):
    if ctx.author.id == 150009383592525826:
        await ctx.channel.purge(limit=int(amt)+1)
        await ctx.channel.send("Killed {}".format(amt) + " messages.")


###### commands end here #######################################################

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

    if message.guild.id == 213868052373045248: #graveyard ####################################################
        #if message.content == 'test':
        #    await message.channel.send(message.guild)

        if "spopy" in message.content.lower():
            # await message.add_reaction(emoji='❓')
            await message.add_reaction(emoji='❓')

        if "anime" in message.content.lower():
            await message.add_reaction(emoji='😡')

        if message.content.startswith('$hello'):
            await message.channel.send('helo dood :D')

        if message.content.startswith('$steam'):
            game_name = message.content[7:]
            await message.channel.send(SteamInfoPuller.steamGameSearch(game_name))

        if message.author.id == 578771603475791893:
            if "dark souls" in message.content.lower():
                await message.add_reaction(emoji='😔')

    if message.guild.id == 213330594749349888: #ninjacord ###################################################
        if message.content.startswith('!spopy7'):
            await message.channel.send('https://gyazo.com/77a9b9d4cc3890b70eed030fa7d51a87')

        if "spopy" in message.content.lower():
            await message.add_reaction(emoji='<:What: 271214076728836096 >')


client.run(DiscordBotKey.private_Key)