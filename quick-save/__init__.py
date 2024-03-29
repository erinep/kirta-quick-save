from PyQt5.QtWidgets import QAction

from krita import Krita
from pathlib import Path
from datetime import date
import os

parentDir = os.path.expanduser(os.sep.join(["~","Pictures"]))
dateString = date.today().strftime("%Y-%m-%d")

def saveNewFileAsDate():
    
    try:
        app = Krita.instance()
        doc = app.activeDocument()
        filename =doc.fileName()

        newFile = os.path.join(parentDir, f"{dateString}.kra")
        index = 1
        
        # find unique file name
        while Path(newFile).is_file():
            newFile = os.path.join(parentDir, f"{dateString} ({index}).kra")
            index += 1

        doc.saveAs(newFile)

    except:
        pass

        
saveAction = QAction(f"Quick Save!")
saveAction.setShortcut("Ctrl+P")
saveAction.triggered.connect(saveNewFileAsDate)

main_menu = Krita.instance().activeWindow().qwindow().menuBar()
main_menu.addAction(saveAction)