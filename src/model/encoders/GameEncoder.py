import json

from src.model.Game import Game


class GameEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Game):
            return o.__dict__
        return json.JSONEncoder.default(self, o)