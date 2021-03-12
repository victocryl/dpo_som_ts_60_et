# Данный модуль содержит атрибуты и методы для работы с вкладкой ОЩИБКИ

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, Qt
import sub

class Failuries:
    def __init__(self, mainwind):
        self.mainwind = mainwind



##########################################################################################################
################## МЕТОДЫ ################################################################################
##########################################################################################################

    def failuries_reading(self):
        ############# УКВ 1 ####################################################################
        # бит Приточный вентилятор 1 включен
        # if (self.mainwind.Can_cor.rx_ukv_1_2[0] & sub.BIT0):
        #     self.mainwind.checkBox_141.setCheckState(Qt.Checked)
        #     self.mainwind.checkBox_52.setCheckState(Qt.Checked)
        # else:
        #     self.mainwind.checkBox_141.setCheckState(Qt.Unchecked)
        #     self.mainwind.checkBox_52.setCheckState(Qt.Unchecked)
        pass