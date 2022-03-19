from .utils import Utils
from bot.core.bot import SketchBot


def setup(bot: SketchBot):
    ext = Utils(bot)
    bot.add_cog(ext)