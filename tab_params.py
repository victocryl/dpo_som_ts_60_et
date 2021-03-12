# Данный модуль содержит атрибуты и методы для работы с вкладкой ПАРАМЕТРЫ

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, Qt
import sub

class Params:
    def __init__(self, mainwind):
        self.mainwind = mainwind



##########################################################################################################
################## МЕТОДЫ ################################################################################
##########################################################################################################

    # @brief  Метод считывания режимов работы и параметров из посылки rx263/273
    # @param  None
    # @retval None
    def params_reading(self):
        
        # считываем режимы работы
        self.modes_reading()

        # далее читаем параметры
        ############# УКВ 1 ####################################################################

        # температура наружного воздуха
        amb_temp = (self.mainwind.Can_cor.rx_ukv_1_1[1] | (self.mainwind.Can_cor.rx_ukv_1_1[2] << 8)) / 10
        self.mainwind.label_303.setNum(amb_temp)





    # @brief  Метод считывания режимов из посылки rx263/273
    # @param  None
    # @retval None
    def modes_reading(self):

        ############# УКВ 1 ####################################################################
        if (self.mainwind.Can_cor.rx_ukv_1_1[0] & sub.BIT0):
            self.mainwind.label_12.setText('ОТКЛЮЧЕНО')
        elif (self.mainwind.Can_cor.rx_ukv_1_1[0] & sub.BIT1):
            self.mainwind.label_12.setText('АВТОМАТИЧ.')
        elif (self.mainwind.Can_cor.rx_ukv_1_1[0] & sub.BIT2):
            self.mainwind.label_12.setText('ПОДОГРЕВ')
        elif (self.mainwind.Can_cor.rx_ukv_1_1[0] & sub.BIT3):
            self.mainwind.label_12.setText('ОХЛАЖДЕНИЕ')
        elif (self.mainwind.Can_cor.rx_ukv_1_1[0] & sub.BIT4):
            self.mainwind.label_12.setText('ВЕНТИЛЯЦИЯ')
        elif (self.mainwind.Can_cor.rx_ukv_1_1[0] & sub.BIT5):
            self.mainwind.label_12.setText('УСИЛ.ВЕНТИЛ.')
        elif (self.mainwind.Can_cor.rx_ukv_1_1[0] & sub.BIT6):
            self.mainwind.label_12.setText('ПОДГОТОВКА')
        elif (self.mainwind.Can_cor.rx_ukv_1_1[0] & sub.BIT7):
            self.mainwind.label_12.setText('ТЕСТОВЫЙ')
        else:
            self.mainwind.label_12.setText('НЕОПРЕД.')
        
        ############# УКВ 2 ####################################################################
        if (self.mainwind.Can_cor.rx_ukv_2_1[0] & sub.BIT0):
            self.mainwind.label_67.setText('ОТКЛЮЧЕНО')
        elif (self.mainwind.Can_cor.rx_ukv_2_1[0] & sub.BIT1):
            self.mainwind.label_67.setText('АВТОМАТИЧ.')
        elif (self.mainwind.Can_cor.rx_ukv_2_1[0] & sub.BIT2):
            self.mainwind.label_67.setText('ПОДОГРЕВ')
        elif (self.mainwind.Can_cor.rx_ukv_2_1[0] & sub.BIT3):
            self.mainwind.label_67.setText('ОХЛАЖДЕНИЕ')
        elif (self.mainwind.Can_cor.rx_ukv_2_1[0] & sub.BIT4):
            self.mainwind.label_67.setText('ВЕНТИЛЯЦИЯ')
        elif (self.mainwind.Can_cor.rx_ukv_2_1[0] & sub.BIT5):
            self.mainwind.label_67.setText('УСИЛ.ВЕНТИЛ.')
        elif (self.mainwind.Can_cor.rx_ukv_2_1[0] & sub.BIT6):
            self.mainwind.label_67.setText('ПОДГОТОВКА')
        elif (self.mainwind.Can_cor.rx_ukv_2_1[0] & sub.BIT7):
            self.mainwind.label_67.setText('ТЕСТОВЫЙ')
        else:
            self.mainwind.label_67.setText('НЕОПРЕД.')
        