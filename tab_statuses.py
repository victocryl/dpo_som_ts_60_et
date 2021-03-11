# Данный модуль содержит атрибуты и методы для работы с вкладкой СТАТУСЫ

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, Qt
import sub

class Statuses:
    def __init__(self, mainwind):
        self.mainwind = mainwind

    def statuses_reading(self):
        ############# УКВ 1 ####################################################################
        # бит Приточный вентилятор 1 включен
        if (self.mainwind.Can_cor.rx_ukv_1_2[0] & sub.BIT0):
            self.mainwind.checkBox_141.setCheckState(Qt.Checked)
            self.mainwind.checkBox_52.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_141.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_52.setCheckState(Qt.Unchecked)
        
        # бит Приточный вентилятор 2 включен
        if (self.mainwind.Can_cor.rx_ukv_1_2[0] & sub.BIT1):
            self.mainwind.checkBox_144.setCheckState(Qt.Checked)
            self.mainwind.checkBox_54.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_144.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_54.setCheckState(Qt.Unchecked)