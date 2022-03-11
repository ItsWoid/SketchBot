import disnake
from disnake.ext import commands

from bot.constants import Colours
from bot.core.db.tickets import Tickets
from bot.core.i18n import Translator

TICKET_DESCRIPTION = (
    "Hello {mention} our staff will be with you soon!"
)

_ = Translator("Tickets", __file__)


class TicketCreateView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @disnake.ui.button(
        label="Create Ticket", style=disnake.ButtonStyle.grey, custom_id="ticket:button:create"
    )
    async def create_ticket(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        print(inter.locale, flush=True)
        await inter.response.send_modal(modal=TicketCreateModal(inter.locale))


class TicketCreateModal(disnake.ui.Modal):
    def __init__(self, locale):
        components = [
            disnake.ui.TextInput(
                label=_("Problem", locale),
                placeholder=_("What seems to be the problem?", locale),
                custom_id="Ticket Topic",
                style=disnake.TextInputStyle.long,
            ),
        ]
        super().__init__(
            title=_("Create Ticket", locale),
            custom_id="ticket:modal:create",
            components=components,
        )

        self.locale = locale
    
    async def callback(self, inter: disnake.ModalInteraction):
        guild = inter.guild
        author = inter.author

        await inter.response.defer(ephemeral=True)

        count = await inter.bot.engine.count(Tickets)
        if count >= 15:
            await inter.edit_original_message(
                "Unfortunately, there is a lot of tickets opened at this point.\n"
                "Would you like to be in a queue instead?\n"
                "We will create a ticket and notify for you when there will be a free space!"
            )

        overwrites = {
            guild.default_role: disnake.PermissionOverwrite(
                view_channel=False,
            ),
            author: disnake.PermissionOverwrite(
                view_channel=True,
                send_messages=True,
                attach_files=True,
            ),
        }
        channel = await inter.channel.category.create_text_channel("ticket", overwrites=overwrites)
        instance = Tickets(channel=channel.id)
        await inter.bot.engine.save(instance)
        embed = disnake.Embed()
        embed.title = "New Ticket"
        embed.description = f"Hello {author.mention} our staff will be with you soon!"
        embed.colour = Colours.pastel_purple
        for key, value in inter.text_values.items():
            embed.add_field(name=key, value=value, inline=False)
        await channel.send(embed=embed)
        await inter.edit_original_message(
            content=_("Successfully created a ticket for you {channel}".format(channel=channel.mention), inter.locale)
        )