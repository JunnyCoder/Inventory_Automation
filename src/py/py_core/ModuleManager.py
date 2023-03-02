'''
Created by Junho Kim
Latest edit : Mar 01 2023
'''
import datetime
from ..py_modules.mgmt import xlsx_mgmt #, inventory_mgmt, preferences_mgmt, web_mgmt


class BasicManager:
    '''다중 모듈 관리 공통 필요 정의 영역'''
    def __init__(self):
        location_dict = ''
        pass

    @staticmethod
    def __master_excel_read(fn):
        xlsx_mgmt.excel_mgmt(fn, 'read')

    @staticmethod
    def __master_excel_edit(fn, cols_dic, sheet_number=0, header=1, index=0):
        xlsx_mgmt.excel_mgmt(fn, 'edit')

    @staticmethod
    def __master_excel_create(fn):
        xlsx_mgmt.excel_mgmt(fn, 'write')


class FileManager(BasicManager):
    def __init__(self):
        self.logs_dir = {
            'file_log': '../../../logs/file_log.xlsx'
        }  # 엑셀 읽어 오는 방식으로 변경할 것

    def excel_read(self, name, fn, access_type, reason=''):
        self.__master_excel_read(fn)
        self.__file_access_log(name, fn, access_type, reason)

    def excel_edit(self, name, fn, access_type, reason=''):
        self.__master_excel_read(fn)
        self.__file_access_log(name, fn, access_type, reason)

    def excel_create(self, name, fn, access_type, reason=''):
        self.__master_excel_read(fn)
        self.__file_access_log(name, fn, access_type, reason)

    def __file_access_log(self, name, fn, access_type, reason):
        self.__master_excel_edit(self.logs_dir['file_log'], {'time': datetime.datetime,
                                                             'File_name': fn,
                                                             'Executed_mod': access_type,
                                                             'Reason': reason,
                                                             'Operated by': name})


class PrefManager(FileManager):
    def __init__(self):
        super().__init__()


class WebManager(FileManager):
    def __init__(self):
        super().__init__()


class SuperUser(FileManager):
    def __init__(self):
        super().__init__()