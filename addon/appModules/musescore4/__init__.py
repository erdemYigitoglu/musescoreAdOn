import appModuleHandler
from .note import Note
from scriptHandler import script
import ui
import api
import controlTypes
from NVDAObjects.UIA import UIA
class AppModule(appModuleHandler.AppModule):
	@script(
		gesture= "kb:NVDA+shift+p",
		description= "anounces the pitch name, duration and octave"
	)
	def script_anouncePitch(self, gesture):
		object = api.getFocusObject()
		noteInfo = Note(object.name)
		ui.message(noteInfo.name)
	@script(
		gesture= "kb:NVDA+shift+i",
		description ="anounces measurement and beat information of the pitch."
	)
	def script_anounceRhythm(self, gesture):
		object = api.getFocusObject()
		noteInfo = Note(object.name)
		ui.message(noteInfo.place)
	def event_NVDAObject_init(self, obj):
		if isinstance(obj, UIA) and obj.role == controlTypes.Role.STATICTEXT:
			obj.name = Note(obj.name).changeToDo() + " , " + Note(obj.name).place
