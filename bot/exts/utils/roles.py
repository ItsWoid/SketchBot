from dataclasses import dataclass

import disnake
from disnake.ext import commands

from bot.constants import Roles


@dataclass(frozen=True)
class AssignableRole:

    role_id: int


ROLES = {
    "doggo_daily": 943131658935238687,
    "sneak_peaks": 943132022308753468,
    "mobile": 943132298553991178,
    "controller": 943132666528690226,
    "keyboard": 943132790587818035
}

ASSIGNABLE_ROLES = (
    AssignableRole(Roles.doggo_daily),
    AssignableRole(Roles.sneak_peaks),
    AssignableRole(Roles.mobile),
    AssignableRole(Roles.controller),
    AssignableRole(Roles.keyboard),
)


class RolesView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @disnake.ui.select(
        placeholder="Select an option",
        custom_id="roles_select",
        min_values=0,
        max_values=5,
        options=[
            disnake.SelectOption(
                label="Doggo Daily",
                description="Get pings for funny dog shenanigans",
                emoji="🐕",
                value="doggo_daily",
            ),
            disnake.SelectOption(
                label="Sneak Peaks",
                description="Get notified when a sneak peak is posted",
                emoji="👀",
                value="sneak_peaks",
            ),
            disnake.SelectOption(
                label="Mobile",
                description="Get pings exclusive to mobile users",
                emoji="📱",
                value="mobile",
            ),
            disnake.SelectOption(
                label="Controller",
                description="Get pings exclusive to controller users",
                emoji="🎮",
                value="controller",
            ),
            disnake.SelectOption(
                label="Keyboard",
                description="Get pings exclusive to keyboard users",
                emoji="⌨️",
                value="keyboard",
            ),
        ]
    )
    async def select_menu(self, select: disnake.ui.Select, inter: disnake.MessageInteraction):
        author = inter.author

        add_roles = [disnake.Object(id=ROLES[i]) for i in select.values]
        rm_roles = [disnake.Object(id=ROLES[key]) for key, value in ROLES.items()]
        await author.remove_roles(*rm_roles)
        await author.add_roles(*add_roles)
        await inter.response.defer()

#class Roles:
#
#    async def cog_load(self):
#        """await self.bot.wait_until_ready()
#        channel = self.bot.get_channel(790248778895589419)
#        message = await channel.fetch_message(951112219926605854)
#        embed = disnake.Embed()
#        embed.title = "Select your roles"
#        embed.description = (
#            "Select any of the following roles to get exclusive pings about any of the following:\n\n"
#            "🐕 Doggo Daily\n"
#            "👀 Sneak Peaks\n"
#            "📱 Mobile\n"
#            "🎮 Controller\n"
#            "⌨️ Keyboard"
#        )
#        embed.color = 0x8f16fc
#        await message.edit(embed=embed, view=RolesView())"""
#        self.bot.add_view(RolesView())