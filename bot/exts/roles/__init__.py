from .roles import Roles
from bot.core.bot import SketchBot


def setup(bot: SketchBot):
    ext = Roles(bot)
    bot.add_cog(ext)