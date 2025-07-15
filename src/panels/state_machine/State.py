class State:
    def get_src_dest_map(self):
        return {}

    def run(self) -> 'State':
        return self

    def get_name(self) -> str:
        return ""