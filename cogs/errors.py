import discord
from discord.ext import commands


class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Такой команды не существует")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Пропущен обязательный аргумент")
        else:
            await ctx.send("Произошла ошибка при выполнении команды")

    @commands.Cog.listener()
    async def on_error(self, event, *args, **kwargs):
        print('Произошла ошибка в событии:', event)
        print('Аргументы:', args)
        print('Ключевые аргументы:', kwargs)


async def setup(bot):
    await bot.add_cog(Errors(bot))