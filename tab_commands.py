# Данный модуль содержит атрибуты и методы для работы с вкладкой КОМАНДЫ

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, Qt
import sub

class Commands:
    def __init__(self, mainwind):
        self.mainwind = mainwind

    # @brief  Метод чтения галочек на вкладке Команды
    # @param  None
    # @retval None
    def commands_reading(self):
        # считываем состояние чекбокса
        
        if self.mainwind.checkBox_7.checkState() == Qt.Checked:
            print("checked")
        else:
            print("unchecked")

