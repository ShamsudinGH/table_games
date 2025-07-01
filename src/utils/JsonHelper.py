import json

class JsonHelper:
    def read_list_from_json(self, json_file_path, entity):
        with open(json_file_path, encoding='UTF-8') as json_file:
            data = json.load(json_file)
            return [entity(**fields) for fields in data]

    def update_json(self, json_file_path, data, entity_encoder):
        with open(json_file_path, "w", encoding='UTF-8') as json_file:
            json.dump(data, json_file, indent=4, cls=entity_encoder)
            return None