from odmantic import Model


class Infractions(Model):
    user: int

    class Config:
        collection = "infractions"