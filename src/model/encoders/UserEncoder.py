import json

from src.model.User import User, Role


class UserEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return o.__dict__
        if isinstance(o, Role):
            return o.value
        return json.JSONEncoder.default(self, o)