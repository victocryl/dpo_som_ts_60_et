# Данный модуль содержит атрибуты и методы для работы с вкладкой ПАРАМЕТРЫ

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, Qt
import sub

class Params:
    def __init__(self, mainwind):
        self.mainwind = mainwind



##########################################################################################################
################## МЕТОДЫ ################################################################################
##########################################################################################################

    def params_reading(self):
        ############# УКВ 1 ####################################################################
        # # бит Нет сети 400 В АС
        # if (self.mainwind.Can_cor.rx_ukv_1_2[2] & sub.BIT5):
        #     self.mainwind.checkBox_149.setCheckState(Qt.Checked)
        # else:
        #     self.mainwind.checkBox_149.setCheckState(Qt.Unchecked)
        pass

        