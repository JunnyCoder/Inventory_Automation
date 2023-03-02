import ModuleManager as mod_m
import datetime


class Worker:
    def __init__(self, name, company, shift):
        self.manager = mod_m.FileManager
        self.name = name
        self.company = company
        self.shift = shift
        self.is_working = False

    def start_work(self):
        self.is_working = True
        self.manager.excel_edit(self.name)


class WebMaster(mod_m.WebManager):
    def __init__(self):
        super().__init__()


class Supervisor(mod_m.PrefManager):
    def __init__(self):
        super().__init__()


class Director(WebMaster, Supervisor):
    def __init__(self):
        super().__init__()


class MasterDeveloper(Director, mod_m.SuperUser):
    def __init__(self):
        super().__init__()
