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
        # считываем состояние чекбоксов и проставляем биты в tx

    ############# УКВ 1 ####################################################################
        # бит тестового режима
        if self.mainwind.checkBox_7.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_1[0] |= sub.BIT0
        else:
            self.mainwind.Can_cor.tx_ukv_1[0] &= ~sub.BIT0

