import appModuleHandler
import note
from scriptHandler import script
import ui
import api
class AppModule(appModuleHandler.AppModule):
    @script(
        gesture= "kb:NVDA+shift+p",
        description= "anounces the pich name, duration and oktav"
    )
    def script_anouncePich(self, gesture):
        object = api.getFocusObject()
        note= Note(object.name)
        ui.message(note.name)