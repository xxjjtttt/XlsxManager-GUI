from PyQt5.QtWidgets import QComboBox, QTextEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton


class ComboBox(QComboBox):
    def __init__(self, items: list):
        super().__init__()
        self.items = items
        self.init_ui()

    def init_ui(self):
        for item in self.items:
            self.addItem(item)

    def get_data(self):
        return self.currentText()


class Label(QLabel):
    def __init__(self, text):
        super().__init__()
        self.label = text
        self.init_ui()

    def init_ui(self):
        self.setText(self.label)


class LineEdit(QLineEdit):
    def __init__(self, text):
        super().__init__()
        self.label = text
        self.init_ui()

    def init_ui(self):
        self.setPlaceholderText(self.label)

    def get_data(self):
        return self.text()


class PushButton(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.init_ui()

    def init_ui(self):
        self.setText(self.text)


class TextEdit(QTextEdit):
    def __init__(self, text):
        super().__init__()
        self.label = text
        self.init_ui()

    def init_ui(self):
        self.setPlaceholderText(self.label)

    def get_data(self):
        return self.toPlainText()
