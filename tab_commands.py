# Данный модуль содержит атрибуты и методы для работы с вкладкой КОМАНДЫ

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, Qt
import sub

class Commands:
    def __init__(self, mainwind):
        self.mainwind = mainwind

    # @brief  Метод чтения галочек на вкладке Команды
    # @detail Cчитываем состояние чекбоксов и проставляем биты в посылки tx
    # @param  None
    # @retval None
    def commands_reading(self):
        
    ############# УКВ 1 ####################################################################
        # бит тестового режима
        if self.mainwind.checkBox_7.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_1[0] |= sub.BIT0
        else:
            self.mainwind.Can_cor.tx_ukv_1[0] &= ~sub.BIT0
        
        # бит компрессор 1
        if self.mainwind.checkBox_8.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_1[1] |= sub.BIT0
        else:
            self.mainwind.Can_cor.tx_ukv_1[1] &= ~sub.BIT0
        
        # бит клапан контура 1
        if self.mainwind.checkBox_25.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_1[1] |= sub.BIT1
        else:
            self.mainwind.Can_cor.tx_ukv_1[1] &= ~sub.BIT1
        
        # бит Вкл. рег. произв-ти компр. 1
        if self.mainwind.checkBox_59.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_1[1] |= sub.BIT2
        else:
            self.mainwind.Can_cor.tx_ukv_1[1] &= ~sub.BIT2
        
        # бит Вкл. компрессор 2
        if self.mainwind.checkBox_61.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_1[1] |= sub.BIT4
        else:
            self.mainwind.Can_cor.tx_ukv_1[1] &= ~sub.BIT4
            
        # бит Вкл. клапан контура 2
        if self.mainwind.checkBox_63.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_1[1] |= sub.BIT5
        else:
            self.mainwind.Can_cor.tx_ukv_1[1] &= ~sub.BIT5
            
        # бит Вкл. рег. произв-ти компр. 2
        if self.mainwind.checkBox_65.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_1[1] |= sub.BIT6
        else:
            self.mainwind.Can_cor.tx_ukv_1[1] &= ~sub.BIT6
            
        # бит Включить реверс вент-ров конденсатора
        if self.mainwind.checkBox_36.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_1[1] |= sub.BIT7
        else:
            self.mainwind.Can_cor.tx_ukv_1[1] &= ~sub.BIT7
            
        # бит Включить вентиляторы конденсатора
        if self.mainwind.checkBox_35.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_1[2] |= sub.BIT0
        else:
            self.mainwind.Can_cor.tx_ukv_1[2] &= ~sub.BIT0
            
        # бит Включить калорифер 1
        if self.mainwind.checkBox_58.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_1[2] |= sub.BIT1
        else:
            self.mainwind.Can_cor.tx_ukv_1[2] &= ~sub.BIT1
            
        # бит Включить калорифер 2
        if self.mainwind.checkBox_67.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_1[2] |= sub.BIT2
        else:
            self.mainwind.Can_cor.tx_ukv_1[2] &= ~sub.BIT2
            
        # бит Включить калорифер 3
        if self.mainwind.checkBox_68.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_1[2] |= sub.BIT3
        else:
            self.mainwind.Can_cor.tx_ukv_1[2] &= ~sub.BIT3
            
        # бит Включить приточные вентиляторы
        if self.mainwind.checkBox_56.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_1[2] |= sub.BIT4
        else:
            self.mainwind.Can_cor.tx_ukv_1[2] &= ~sub.BIT4
            
        # бит Включить вентилятор наружного воздуха
        if self.mainwind.checkBox_57.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_1[2] |= sub.BIT5
        else:
            self.mainwind.Can_cor.tx_ukv_1[2] &= ~sub.BIT5
            
        # бит Открыть воздушную заслонку
        if self.mainwind.checkBox_87.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_1[2] |= sub.BIT6
        else:
            self.mainwind.Can_cor.tx_ukv_1[2] &= ~sub.BIT6

