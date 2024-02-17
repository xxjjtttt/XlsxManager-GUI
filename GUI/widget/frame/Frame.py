import webbrowser

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QProgressBar

from GUI.data.StaticData import StaticData


# class ProgressBar(QProgressBar):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()
#
#     def init_ui(self):
#         self.setWindowTitle("loading...")
#         self.setWindowIcon(QIcon("GUI/static/icon.png"))


class WarningDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setIcon(self.Warning)
        self.setWindowTitle("error")
        self.setText("something wrong with your porperties")
        self.setStandardButtons(self.Close)
        self.setWindowIcon(StaticData().warning)


class MaintainDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setIcon(self.Information)
        self.setWindowTitle("nothing happened")
        self.setText("action can't work")
        self.setStandardButtons(self.Close)
        self.setWindowIcon(StaticData().about)

class CompleteDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setIcon(self.Information)
        self.setWindowTitle("task was completed")
        self.setText("plz check your output")
        self.setStandardButtons(self.Close)
        self.setWindowIcon(StaticData().about)


class PropertyDialog(QFileDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("select your porperty")
        self.setWindowIcon(StaticData().icon)
        # self.setDirectory()
        self.setNameFilter("porperty(*.json)")


class FileDialog(QFileDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("select your file")
        self.setWindowIcon(StaticData().icon)
        self.setDirectory("C:")
        self.setNameFilter("workingfile(*.xlsx)")


class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__(None)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("about me")
        self.setIcon(self.Information)
        self.setWindowIcon(StaticData().about)
        self.setText("Go to github and get more information\n"
                     "https://github.com/xxjjtttt")
        self.setStandardButtons(self.Yes | self.No)

        yes_button = self.button(self.Yes)
        yes_button.clicked.connect(self.open_github)

    def open_github(self):
        webbrowser.open("https://github.com/xxjjtttt")

