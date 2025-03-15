import appModuleHandler
import note
from scriptHandler import script
import ui
import api
from controlTypes import controlTypes
from NVDAObjects.UIA import UIA
class AppModule(appModuleHandler.AppModule):
	@script(
		gesture= "kb:NVDA+shift+p",
		description= "anounces the pich name, duration and oktav"
	)
	def script_anouncePich(self, gesture):
		object = api.getFocusObject()
		noteInfo = note.Note(object.name)
		ui.message(noteInfo.name)
	@script(
		gesture= "kb:NVDA+shift+i",
		description ="anounces measurement and beat information of the pich."
	)
	def script_anounceRythim(self, gesture):
		object = api.getFocusObject()
		noteInfo = note.Note(object.name)
		ui.message(noteInfo.place)
	def event_NVDAObject_init(self, obj):
		if isinstance(obj, UIA) and obj.role == controlTypes.Role.STATICTEXT:
			obj.name = note.Note(obj.name).transformNoteInfo()
