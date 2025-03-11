class Note():
    def __init__(self, noteInfo):
        properties = noteInfo.split(" , ")
        self._name= properties[0]
        self._place = properties[1]
    @property
    def name(self):
        return self._name
    @property
    def place(self):
        return self._place