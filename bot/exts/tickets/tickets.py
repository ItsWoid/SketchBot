from doctest import debug_script
import disnake
from disnake.ext import commands

from .create import TicketCreateView

from bot.constants import Colours


class Tickets(
    commands.Cog,
):
    def __init__(self, bot):
        self.bot = bot
    
    async def cog_load(self):
        self.bot.add_view(TicketCreateView())

    @commands.Cog.listener()
    async def on_channel_delete(self, channel: disnake.TextChannel):
        ticket = await self.bot.engine.find_one(Tickets, Tickets.channel == channel.id)
        await self.bot.engine.delete(ticket)