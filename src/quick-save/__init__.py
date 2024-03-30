from .quick_save import QuickSave

Krita.instance().addExtension(QuickSave(Krita.instance()))
