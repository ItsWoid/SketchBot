import disnake
from disnake.ext import commands

from bot.constants import Colours


class Avatar:

    @commands.slash_command(name="avatar")
    async def avatar(
        self,
        inter: disnake.GuildCommandInteraction,
    ):
        pass

    @avatar.sub_command(name="user", description="Gets a users main avatar")
    async def avatar_command(
        self,
        inter: disnake.GuildCommandInteraction,
        user: disnake.User = commands.Param(
            desc="User to fetch avatar from",
        ),
    ):
        embed = disnake.Embed()
        embed.set_author(name=f"{user.name}'s avatar")
        embed.set_thumbnail(url=user.avatar.url)
        await inter.response.send_message(embed=embed)
    
    @avatar.sub_command(name="guild", description="Gets a users guild avatar")
    async def avatar_guild(
        self,
        inter: disnake.GuildCommandInteraction,
        user: disnake.User = commands.Param(
            desc="User to fetch avatar from",
        ),
    ):
        guild_avatar = user.guild_avatar_url
        embed = disnake.Embed()
        if guild_avatar is None:
            embed.description = f"{user} does not have a server avatar."
            embed.color = Colours.soft_red
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
            embed.set_author(name=f"{user.name}'s guild avatar")
            embed.set_thumbnail(url=user.guild_avatar.url)
            await inter.response.send_message(embed=embed)
    
    @avatar.sub_command(name="display", description="Displays a user avatar")
    async def display_avatar(
        self,
        inter: disnake.GuildCommandInteraction,
        user: disnake.User = commands.Param(
            desc="User to fetch avatar from",
        ),
    ):
        embed = disnake.Embed()
        embed.set_thumbnail(url=user.display_avatar.url)
        await inter.response.send_message(embed=embed)