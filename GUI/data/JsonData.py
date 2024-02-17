import json

from GUI.widget.frame.Frame import WarningDialog


class JsonData():
    data: dict
    original_data: dict = {
        "task": {
            "enabled": True,
            "save_rubbish": False,
            "file": {
                "database": {
                    "path": "",
                    "active_sheet": []
                },
                "sourcefile": {
                    "path": "",
                    "key_column": -1,
                    "index_column": -1,
                    "have_header": True,
                    "active_sheet": []
                },
                "targetfile": {
                    "path": "",
                    "headers": []
                }
            }
        }
    }

    def __init__(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def get_data(self):
        try:
            file = open(self.path, "r", encoding="utf-8")
            data = json.load(file)
            file.close()
            enabled: bool = bool(data["task"]["enabled"])
            save_rubbish: bool = bool(data["task"]["save_rubbish"])

            database_path: str = str((data["task"]["file"]["database"]["path"]))
            database_active_sheet: list = list((data["task"]["file"]["database"]["active_sheet"]))

            sourcefile_path: str = str(data["task"]["file"]["sourcefile"]["path"])
            have_header: bool = bool(data["task"]["file"]["sourcefile"]["have_header"])
            key_column: int = int(data["task"]["file"]["sourcefile"]["key_column"])
            index_column: int = int(data["task"]["file"]["sourcefile"]["index_column"])
            sourcefile_active_sheet: list = list((data["task"]["file"]["sourcefile"]["active_sheet"]))

            targetfile_path: str = str(data["task"]["file"]["targetfile"]["path"])
            headers: list = list(data["task"]["file"]["targetfile"]["headers"])
            return [[enabled, save_rubbish], [database_path, database_active_sheet],
                    [sourcefile_path, have_header, key_column, index_column, sourcefile_active_sheet],
                    [targetfile_path, headers]]
        except:
            WarningDialog().exec()
            return [[False, False], ["error", []], ["error", False, -1, -1, []], ["error", []]]

    def save_data(self, path, data):
        json_data = {
            "task": {
                "enabled": data[0][0],
                "save_rubbish": data[0][1],
                "file": {
                    "database": {
                        "path": data[1][0],
                        "active_sheet": data[1][1]
                    },
                    "sourcefile": {
                        "path": data[2][0],
                        "key_column": data[2][2],
                        "index_column": data[2][3],
                        "have_header": data[2][1],
                        "active_sheet": data[2][4]
                    },
                    "targetfile": {
                        "path": data[3][0],
                        "headers": data[3][1]
                    }
                }
            }
        }
        with open(path, "w", encoding="utf-8") as file:
            self.original_data.update(json_data)
            json.dump(self.original_data, file)
