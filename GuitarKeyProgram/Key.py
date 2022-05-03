class Key:

    def __init__(self,name,notes):
        self.name = name
        self.notes = notes

    def draw(self,WIN):
        for n in self.notes:
            for t in n.tabs:
                t.draw(WIN)