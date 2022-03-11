import disnake
from disnake.ext import commands


class Infractions:

    @commands.slash_command(
        name="warn",
        description="Warn a user in the server"
    )
    async def warn_command(
        self,
        inter: disnake.GuildCommandInteraction,
        user: disnake.User = commands.Param(
            desc="Target user",
        ),
        reason: str = commands.Param(
            desc="Reason of the warn",
        ),
    ):
        pass