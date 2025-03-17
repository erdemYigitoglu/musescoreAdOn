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
	def changeToDo(self):
		noteMap = {"C": "Do", "D":"Re", "E":"Me", "F":"Fa", "G":"Sol", "A":"La", "B":"Si"}
		return noteMap.get(self._name[0]) + " " + self._name[1:]
