from bot.core.bot import SketchBot
from bot.constants import Bot


bot = SketchBot()
bot.load_extension("bot.exts.tickets")
bot.load_extension("bot.exts.roles")
print(Bot.token, flush=True)
bot.run("ODMwNDk0OTgwMjYxOTM3MjIy.YHHguQ.bUXymHPvlG80G2OE2NoeqchZ4I4")