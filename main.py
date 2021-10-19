import discord
from discord.ext import commands
import music
cogs = [music]
client=commands.Bot(command_prefix='!',intents=discord.Intents.all())
for i in range(len(cogs)):
    cogs[i].setup(client)

client.run('NTc0ODA4OTIzNTYzODg0NTQ1.XM-yhg.hN9r6AGAE3bo2XR42jJfbozWBq4')