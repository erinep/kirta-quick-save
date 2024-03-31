from krita import (
    Krita,
    Extension,
    InfoObject, 
    InfoObject,
    Selection,
    Filter
)


class QuickScripts(Extension):
    
    def __init__(self, parent):
        super().__init__(parent)


    def setup(self):
        pass


    def CreateDodgeFilterLayer(self, _):
        try:

            activeDoc=Krita.instance().activeDocument()
            activeLayer = activeDoc.activeNode()      

            # define filter properties
            configParameters=InfoObject()
            configParameters.setProperties({
                    'type': 1,
                    'exposure': 0.7
                })
                
            # create filter
            filter=Filter()
            filter.setName('dodge')
            filter.setConfiguration(configParameters)

            # create selection
            selection = Selection()
            selection.selectAll(activeLayer, 255)


            # create filter layer
            filterLayer= activeDoc.createFilterLayer("midtone dodge", filter, selection)

            # add it to document
            activeDoc.rootNode().addChildNode(filterLayer, None)

        except:
            pass              
 

    def createActions(self, window):        

        saveAction = window.createAction("", "lighten image!", "tools")
        saveAction.triggered.connect(self.CreateDodgeFilterLayer)
