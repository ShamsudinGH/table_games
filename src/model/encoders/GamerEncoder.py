import json

from src.model.Gamer import Gamer


class GamerEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Gamer):
            return o.__dict__
        return json.JSONEncoder.default(self, o)