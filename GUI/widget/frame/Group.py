from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout

from GUI.widget.loader.Loader import TextLoaderWithButton, TextLoader, TextLoaderBigger, SettingLoader
from GUI.widget.single.Single import PushButton


class DatabaseGroup(QGroupBox):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setTitle("Database")
        database_group_layout = QVBoxLayout()
        database_group_layout.addWidget(TextLoaderWithButton("path", "load"))
        database_group_layout.addWidget(TextLoader("active sheet"))
        self.setLayout(database_group_layout)

    def get_data(self):
        widgets = self.findChildren((TextLoaderWithButton, TextLoader))
        data = []
        for widget in widgets:
            data.append(widget.get_data())
        if type(data[1]) == list:
            return data
        else:
            data[1] = [data[1]]
        return data

    def put_data(self, data_set):
        widgets = self.findChildren((TextLoaderWithButton, TextLoader))
        for widget, data in zip(widgets, data_set):
            widget.put_data(data)


class BaseGroup(QGroupBox):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setTitle("base")
        base_group_layout = QHBoxLayout()
        base_group_layout.addWidget(SettingLoader("enabled", ["true", "false"]))
        base_group_layout.addWidget(SettingLoader("save rubbish", ["true", "false"]))
        self.setLayout(base_group_layout)

    def get_data(self):
        combobox = self.findChildren(SettingLoader)
        data = []
        for combo in combobox:
            data.append(combo.get_data())
        return data

    def put_data(self, data_set):
        combobox = self.findChildren(SettingLoader)
        for combo, data in zip(combobox, data_set):
            combo.put_data(data)


class TargetfileGroup(QGroupBox):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setTitle("Targetfile")
        targetfile_group_layout = QVBoxLayout()
        targetfile_group_layout.addWidget(TextLoaderWithButton("path", "load"))
        targetfile_group_layout.addWidget(TextLoaderBigger("headers"))
        self.setLayout(targetfile_group_layout)

    def get_data(self):
        widgets = self.findChildren((TextLoaderWithButton, TextLoaderBigger))
        data = []
        for widget in widgets:
            data.append(widget.get_data())
        return data

    def put_data(self, data_set):
        widgets = self.findChildren((TextLoaderWithButton, TextLoaderBigger))
        for widget, data in zip(widgets, data_set):
            widget.put_data(data)


class SourcefileGroup(QGroupBox):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setTitle("Sourcefile")
        sourcefile_group_layout = QVBoxLayout()
        sourcefile_group_layout.addWidget(TextLoaderWithButton("path", "load"))
        sourcefile_group_layout.addWidget(SettingLoader("have header", ["true", "false"]))
        sourcefile_group_layout.addWidget(TextLoader("key column"))
        sourcefile_group_layout.addWidget(TextLoader("index column"))
        sourcefile_group_layout.addWidget(TextLoader("active sheet"))
        self.setLayout(sourcefile_group_layout)

    def get_data(self):
        widgets = self.findChildren((TextLoaderWithButton, SettingLoader, TextLoader))
        data = []
        for widget in widgets:
            data.append(widget.get_data())
        if type(data[4]) == list:
            return data
        else:
            data[4] = [data[4]]
        return data

    def put_data(self, data_set):
        widgets = self.findChildren((TextLoaderWithButton, SettingLoader, TextLoader))
        for widget, data in zip(widgets, data_set):
            widget.put_data(data)


class ActionGroup(QGroupBox):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setTitle("action")
        action_group_layout = QVBoxLayout()
        action_group_layout.addWidget(PushButton("open"))

        action_group_layout.addWidget(PushButton("classify"))

        action_group_layout.addWidget(PushButton("count"))

        action_group_layout.addWidget(PushButton("save"))

        self.setLayout(action_group_layout)


class MainGroup(QGroupBox):
    def __init__(self):
        super().__init__()
        self.load_property = pyqtSignal(list)
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout()

        child_group_1 = QGroupBox()
        child_layout_1 = QVBoxLayout()
        child_layout_1.addWidget(BaseGroup())
        child_layout_1.addWidget(DatabaseGroup())
        child_layout_1.addWidget(SourcefileGroup())
        child_group_1.setLayout(child_layout_1)

        child_group_2 = QGroupBox()
        child_layout_2 = QVBoxLayout()
        child_layout_2.addWidget(TargetfileGroup())
        child_layout_2.addWidget(ActionGroup())
        child_group_2.setLayout(child_layout_2)

        main_layout.addWidget(child_group_1)
        main_layout.addWidget(child_group_2)

        self.setLayout(main_layout)

    def get_data(self):
        widgets = self.findChildren((BaseGroup, DatabaseGroup, SourcefileGroup, TargetfileGroup))
        data = []
        for widget in widgets:
            data.append(widget.get_data())
        # data[1][1] = [data[1][1]]
        # data[2][4] = [data[2][4]]
        print(data)
        return data

    def put_data(self, data_set):
        widgets = self.findChildren((BaseGroup, DatabaseGroup, SourcefileGroup, TargetfileGroup))
        for widget, data in zip(widgets, data_set):
            widget.put_data(data)
