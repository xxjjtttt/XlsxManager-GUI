"""
Author: xxjjtttt
Date: 2024-01-22 17:11:56
LastEditTime: 2024-01-22 23:13:25
LastEditors: xxjjtttt
Description: https://github.com/xxjjtttt
FilePath: \\python\\xlsx master\\Task\\Task.py
屎山代码什么时候重构
"""

# python -m pip install upgrade pip
# pip install openpyxl==3.1.2


from GUI.Task.File.Database import Database
from GUI.Task.File.Sourcefile import Sourcefile
from GUI.Task.File.Targetfile import Targetfile


class CoreTask:
    database: Database
    sourcefile: Sourcefile
    targetfile: Targetfile

    def __init__(self, data) -> None:
        self.data = data

    def init(self) -> None:
        database = self.data[1]
        sourcefile = self.data[2]
        targetfile = self.data[3]
        self.database = Database(database[0], database[1])
        self.sourcefile = Sourcefile(sourcefile[0], sourcefile[2], sourcefile[3], sourcefile[1], sourcefile[4])
        self.targetfile = Targetfile(targetfile[0], sourcefile[2], sourcefile[3], sourcefile[1], targetfile[1])
        self.targetfile.save()

    def close(self) -> None:
        self.database.close()
        self.sourcefile.close()
        self.targetfile.close()

    def classify(self) -> None:
        if self.data[0][0] is False:
            return
        self.init()
        header_list: list = self.sourcefile.get_header_list()
        self.targetfile.set_header(header_list)
        for source_name in self.sourcefile.get_sheetnames():
            self.sourcefile.change_working_sheet(source_name)
            for source_row in range(self.sourcefile.get_max()[0]):
                source = self.sourcefile.get_key_value()
                is_classified = False
                if source == ".":
                    self.sourcefile.next_working_row()
                    continue
                for data_name in self.database.get_sheetnames():
                    self.database.change_working_sheet(data_name)
                    for data_row in range(self.database.get_max()[0]):
                        data_list = self.database.get_data_list()
                        for index, data in enumerate(data_list):
                            if index == 0:
                                continue
                            if data == source:
                                self.targetfile.change_working_sheet(data_list[0])
                                source_list = self.sourcefile.get_source_list()
                                self.targetfile.add_row(source_list)
                                self.sourcefile.next_working_row()
                                is_classified = True
                                break
                        if is_classified:
                            break
                    if is_classified:
                        break
                    else:
                        self.sourcefile.next_working_row()
        self.targetfile.save()
        if self.data[0][1] is True:
            self.sourcefile.throw_rubbish()

    def count(self) -> None:
        if self.data[0][0] is not True:
            return
        self.init()
        sheetname_list = self.targetfile.get_sheetnames()
        for sheetname in sheetname_list:
            self.database.change_working_sheet(sheetname)
            self.targetfile.change_working_sheet(sheetname)
            self.sourcefile.change_working_sheet(sheetname)
            for data_row in range(self.database.get_max()[0]):
                self.sourcefile.reset_working_row()
                data_list = self.database.get_data_list()
                count: int = 0
                for source_row in range(self.sourcefile.get_max()[0]):
                    source = self.sourcefile.get_key_value()
                    if source == ".":
                        self.sourcefile.next_working_row()
                        continue
                    for index, data in enumerate(data_list):
                        if index == 0:
                            continue
                        if data == source:
                            self.sourcefile.tag_row()
                            count += 1
                            break
                    self.sourcefile.next_working_row()
                self.targetfile.add_row([data_list[0], count])
                self.targetfile.save()
        if self.data[0][1] is True:
            self.sourcefile.throw_rubbish()
