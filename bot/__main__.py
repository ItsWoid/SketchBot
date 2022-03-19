from bot.core.bot import SketchBot
from bot.constants import Bot


bot = SketchBot()
bot.load_extension("bot.exts.tickets")
bot.load_extension("bot.exts.utils")
bot.run(Bot.token)