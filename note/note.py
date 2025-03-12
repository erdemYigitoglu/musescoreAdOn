class Note():
    def __init__(self, noteInfo):
        properties = noteInfo.split(" , ")
        self._name= properties[0][5:]
        self._place = properties[1]
    @property
    def name(self):
        return self._name
    @property
    def place(self):
        return self._place
    def transformName(self):
        if self._name[0] == "C":
            return "do" + self._name[6:]
        elif self._name[0] == "D":
            return "re" + self_name[6:]
        elif self._name[0] == "E":
            return "me" + self._name[6:]
        elif self._name[0] == "F":
            return "fa" + self._name[6:]
        elif self._name[0] == "G":
            return "sol" + self._name[6:]
        elif self._name[0] == "A":
            return  "la" + self._name[6:]
        elif self._name[0] == "B":
            return "si" + self._name[6:]