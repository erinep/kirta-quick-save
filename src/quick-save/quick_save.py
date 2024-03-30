from PyQt5.QtWidgets import QMenu
from krita import (Krita, Extension)

from pathlib import Path
from datetime import date
import os

class QuickSave(Extension):
    
    def __init__(self, parent):
        super().__init__(parent)        
        self.parentDir = os.path.expanduser(os.sep.join(["~","Pictures"]))
        self.dateString = date.today().strftime("%Y-%m-%d")


    def setup(self):
        pass

    def saveNewFileAsDate(self, _):
        try:
            app = Krita.instance()
            doc = app.activeDocument()
            filename = doc.fileName()

            newFile = os.path.join(self.parentDir, f"{self.dateString}.kra")
            index = 1
            
            # find unique file name
            while Path(newFile).is_file():
                newFile = os.path.join(self.parentDir, f"{self.dateString} ({index}).kra")
                index += 1

            doc.saveAs(newFile)

        except:
            pass              
 

    def createActions(self, window):        

        saveAction = window.createAction("quicksave", "Quick Save!", "")
        saveAction.setShortcut("Ctrl+P")
        saveAction.triggered.connect(self.saveNewFileAsDate)

        # add action to main menu bar
        window.qwindow().menuBar().addAction(saveAction)
