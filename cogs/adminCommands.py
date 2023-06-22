import discord
from discord.ext import commands


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def addRole(self, ctx, member: discord.Member, *, role: discord.Role):
        if role == member.roles:
            await ctx.send('Данная роль уже присутсвует')
            return
        else:
            await member.add_roles(role)

    @commands.command()
    async def removeRole(self, ctx, member: discord.Member, *, role: discord.Role):
        await member.remove_roles(role)
        await ctx.send(f"Роль '{role.name}' успешно удалена у пользователя '{member.display_name}'.")


async def setup(bot):
    await bot.add_cog(AdminCommands(bot))
