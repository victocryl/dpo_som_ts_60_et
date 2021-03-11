# Данный модуль содержит атрибуты и методы для работы с вкладкой СТАТУСЫ

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, Qt
import sub

class Statuses:
    def __init__(self, mainwind):
        self.mainwind = mainwind

    def statuses_reading(self):
        print('xsdsdvs')