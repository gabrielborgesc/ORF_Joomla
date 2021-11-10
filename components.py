class Component:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __lt__(self, other):
        return self.name < other.name
