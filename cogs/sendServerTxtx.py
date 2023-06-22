import json
import discord
from discord.ext import commands

with open('data/server-txts/rule.txt', 'r', encoding='utf-8') as file:
    rule = file.read()

with open('data/channelsId.json', 'r') as file:
    array_ch_id = json.load(file)
    channel_id_rule = array_ch_id['RuleChId']


class sendServerTxts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.rule = rule
        self.channelIdRule = channel_id_rule

    @commands.command()
    async def sendRule(self, ctx):
        channel = self.bot.get_channel(self.channelIdRule)
        await channel.send(self.rule)


async def setup(bot):
    await bot.add_cog(sendServerTxts(bot))