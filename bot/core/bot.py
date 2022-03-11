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

        print(type(Bot.db), flush=True)
        client = AsyncIOMotorClient("mongodb+srv://FireLite:l7ecZNau88kjc045@firelite.renik.mongodb.net/SketchBot?retryWrites=true&w=majority")
        self.engine = AIOEngine(motor_client=client, database="SketchBot")

    async def on_ready(self):
        pass