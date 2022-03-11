from .tickets import Tickets


def setup(bot):
    ext = Tickets(bot)
    bot.add_cog(ext)