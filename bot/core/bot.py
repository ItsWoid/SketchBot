import disnake
from disnake.ext import commands

from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

from bot.constants import Bot

from bot.exts.tickets.create import TicketCreateView


class SketchBot(commands.InteractionBot):
    def __init__(self):
        intents = disnake.Intents.all()
        super().__init__(
            intents=intents,
        )

        client = AsyncIOMotorClient(Bot.db)
        self.engine = AIOEngine(motor_client=client, database="SketchBot")

    async def on_ready(self):
        pass