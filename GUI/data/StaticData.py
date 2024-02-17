from PyQt5.QtGui import QIcon


class StaticData:

    def __init__(self):
        self.icon = QIcon("GUI/static/icon.png")
        self.start = QIcon("GUI/static/start.png")
        self.about = QIcon("GUI/static/about.png")
        self.warning = QIcon("GUI/static/warning.png")
