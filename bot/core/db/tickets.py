from odmantic import Field, Model


class Tickets(Model):
    channel: int

    class Config:
        collection = "tickets"