from PyQt5.QtWidgets import QGroupBox, QHBoxLayout

from GUI.widget.single.Single import Label, LineEdit, PushButton, TextEdit, ComboBox


class TextLoader(QGroupBox):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.init_ui()

    def init_ui(self):
        text_loader_layout = QHBoxLayout()
        text_loader_layout.addWidget(Label(self.text))
        text_loader_layout.addWidget(LineEdit(self.text))
        self.setLayout(text_loader_layout)

    def get_data(self):
        edit = self.findChild(LineEdit)
        if len(edit.get_data()) != 1:
            return [int(num) for num in edit.get_data().split(",")]
        else:
            return int(edit.get_data())

    def put_data(self, data):
        edit = self.findChild(LineEdit)
        if type(data) != list:
            edit.setText(str(data))
        else:
            li = [str(i) for i in data]
            temp = ",".join(li)
            edit.setText(temp)


class TextLoaderWithButton(QGroupBox):
    def __init__(self, text1, text2):
        super().__init__()
        self.text1 = text1
        self.text2 = text2
        self.init_ui()

    def init_ui(self):
        file_path_loader_layout = QHBoxLayout()
        file_path_loader_layout.addWidget(Label(self.text1))
        file_path_loader_layout.addWidget(LineEdit(self.text1))
        file_path_loader_layout.addWidget(PushButton(self.text2))
        self.setLayout(file_path_loader_layout)

        self.findChild(PushButton).clicked.connect(self.on_load)

    def get_data(self):
        edit = self.findChild(LineEdit)
        return edit.get_data()

    def on_load(self):
        edit = self.findChild(LineEdit)
        from GUI.widget.frame.Frame import FileDialog
        dialog = FileDialog()
        if dialog.exec() == FileDialog.Accepted:
            edit.setText(dialog.selectedFiles()[0])

    def put_data(self, data):
        edit = self.findChild(LineEdit)
        # print(data,type(data))
        edit.setText(str(data))


class TextLoaderBigger(QGroupBox):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.init_ui()

    def init_ui(self):
        text_loader_layout = QHBoxLayout()
        text_loader_layout.addWidget(Label(self.text))
        text_loader_layout.addWidget(TextEdit(self.text))
        self.setLayout(text_loader_layout)

    def get_data(self):
        edit = self.findChild(TextEdit)
        return edit.get_data().split(",\n")

    def put_data(self, data):
        edit = self.findChild(TextEdit)
        if type(data) != list:
            edit.setText(str(data))
        else:
            li = [str(i) for i in data]
            temp = ",\n".join(li)
            edit.setText(temp)


class SettingLoader(QGroupBox):
    def __init__(self, text, items):
        super().__init__()
        self.text = text
        self.items = items
        self.init_ui()

    def init_ui(self):
        setting_loader_layout = QHBoxLayout()
        setting_loader_layout.addWidget(Label(self.text))
        setting_loader_layout.addWidget(ComboBox(self.items))
        self.setLayout(setting_loader_layout)

    def get_data(self):
        widget = self.findChild(ComboBox)
        if widget.get_data() == "true":
            return True
        else:
            return False

    def put_data(self, data):
        widget = self.findChild(ComboBox)
        if not data:
            widget.setCurrentIndex(1)
