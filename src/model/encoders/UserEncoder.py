import json

from src.model.User import User


class UserEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return o.__dict__
        return json.JSONEncoder.default(self, o)