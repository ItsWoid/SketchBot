from bot.core.bot import SketchBot
from bot.constants import Bot


bot = SketchBot()
bot.load_extension("bot.exts.tickets")
bot.load_extension("bot.exts.roles")
bot.run(Bot.token)