import json
import os
import discord
from discord.ext import commands, tasks

with open('data/channelsId.json', 'r') as file:
    array_ch_id = json.load(file)
    channel_id_rule = array_ch_id['RuleChId']





class ServerTxt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.rule = None
        self.channelIdRule = int(channel_id_rule)
        self.rule = open_file.start()

    @commands.command()
    async def sendRule(self, ctx):
        channel = self.bot.get_channel(self.channelIdRule)
        await channel.purge()
        await channel.send(self.rule)


async def setup(bot):
    await bot.add_cog(ServerTxt(bot))
