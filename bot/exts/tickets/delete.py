import disnake
from disnake.ext import commands


class TicketDelete(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(
        label="Close", style=disnake.ButtonStyle.red, custom_id="ticket:close"
    )
    async def close_ticket(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        pass