import disnake
from disnake.ext import commands

from .avatar import Avatar
from .roles import Roles, RolesView


class Utils(
    Avatar,
    Roles,
    commands.Cog,
):
    def __init__(self, bot):
        self.bot = bot
    
    async def cog_load(self):
        self.bot.add_view(RolesView())