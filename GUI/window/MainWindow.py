from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMenuBar

from GUI.Task.Task.Task import CoreTask
from GUI.data.JsonData import JsonData
from GUI.data.StaticData import StaticData
from GUI.widget.frame.Frame import PropertyDialog, AboutDialog, MaintainDialog, WarningDialog, CompleteDialog
from GUI.widget.frame.Group import MainGroup, ActionGroup
from GUI.widget.single.Single import PushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__(None)
        self.layout = QVBoxLayout()
        self.data = JsonData("")
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("xlsx manager")
        self.setWindowIcon(StaticData().icon)
        self.resize(600, 400)
        self.layout.addWidget(MainGroup())
        self.init_menubar()
        self.setLayout(self.layout)
        self.bind_button()

    def init_menubar(self):
        menubar = QMenuBar()
        file_menu = menubar.addMenu("file")

        open_action = file_menu.addAction("open")
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.on_open)

        open_action = file_menu.addAction("classify")
        open_action.setShortcut("Ctrl+1")
        open_action.triggered.connect(self.on_classify)

        open_action = file_menu.addAction("count")
        open_action.setShortcut("Ctrl+2")
        open_action.triggered.connect(self.on_count)

        save_action = file_menu.addAction("save")
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.on_save)

        about_menu = menubar.addMenu("info")
        about_menu.addAction("update").triggered.connect(self.on_update)
        about_menu.addAction("about me").triggered.connect(self.on_about)
        self.layout.setMenuBar(menubar)

    def bind_button(self):
        buttons = self.findChild(MainGroup).findChild(ActionGroup).findChildren(PushButton)
        buttons[0].clicked.connect(self.on_open)
        buttons[1].clicked.connect(self.on_classify)
        buttons[2].clicked.connect(self.on_count)
        buttons[3].clicked.connect(self.on_save)

    def on_open(self):
        dialog = PropertyDialog()
        if dialog.exec() == dialog.Accepted:
            self.data = JsonData(dialog.selectedFiles()[0])
            print(self.data.get_data())
            self.findChild(MainGroup).put_data(self.data.get_data())

    def on_save(self):
        dialog = PropertyDialog()
        if dialog.exec() == dialog.Accepted:
            self.data.save_data(dialog.selectedFiles()[0], self.findChild(MainGroup).get_data())
            CompleteDialog().exec()


    def on_update(self):
        print("update")
        MaintainDialog().exec()

    def on_about(self):
        AboutDialog().exec()

    def on_classify(self):
        try:
            CoreTask(self.findChild(MainGroup).get_data()).classify()
            CompleteDialog().exec()
        except:
            WarningDialog().exec()

    def on_count(self):
        try:
            CoreTask(self.findChild(MainGroup).get_data()).count()
            CompleteDialog().exec()
        except:
            WarningDialog().exec()
