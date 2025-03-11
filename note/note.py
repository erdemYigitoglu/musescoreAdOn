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
    def transformName(self):
        if self._name[5] == "C":
            return "do" + self._name[6:]
        elif self._name[5] == "D":
            return "re" + self_name[6:]
        elif self._name[5] == "E":
            return "me" + self._name[6:]
        elif self._name[5] == "F":
            return "fa" + self._name[6:]
        elif self._name[5] == "G":
            return "sol" + self._name[6:]
        elif self._name[5] == "A":
            return  "la" + self._name[6:]
        elif self._name[5] == "B":
            return "si" + self._name[6:]