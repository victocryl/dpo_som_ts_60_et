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
        
        self.modes_reading()    # считываем режимы работы
        self.common_info_reading()  # считываем общую инфу


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


    # @brief  Метод считывания общей информации из посылки rx263/273
    # @param  None
    # @retval None
    def common_info_reading(self):
        
        ############# УКВ 1 ####################################################################
        # температура наружного воздуха
        amb_temp_1 = (self.mainwind.Can_cor.rx_ukv_1_1[1] | (self.mainwind.Can_cor.rx_ukv_1_1[2] << 8)) / 10
        self.mainwind.label_303.setNum(amb_temp_1)
        # температура салона
        sal_temp_1 = (self.mainwind.Can_cor.rx_ukv_1_1[3] | (self.mainwind.Can_cor.rx_ukv_1_1[4] << 8)) / 10
        self.mainwind.label_302.setNum(sal_temp_1)
        # уставка температуры
        ust_temp_1 = (self.mainwind.Can_cor.rx_ukv_1_1[5] * 0.5 + 12)
        self.mainwind.label_301.setNum(ust_temp_1)
        # версия ПО
        soft_ver_1 = self.mainwind.Can_cor.rx_ukv_1_1[6]
        self.mainwind.label_7.setNum(soft_ver_1)
        # счётчик жизни УКВ
        life_cnt_1 = self.mainwind.Can_cor.rx_ukv_1_1[7]
        self.mainwind.label_75.setNum(life_cnt_1)

        ############# УКВ 2 ####################################################################
        # температура наружного воздуха
        amb_temp_2 = (self.mainwind.Can_cor.rx_ukv_2_1[1] | (self.mainwind.Can_cor.rx_ukv_2_1[2] << 8)) / 10
        self.mainwind.label_312.setNum(amb_temp_2)
        # температура салона
        sal_temp_2 = (self.mainwind.Can_cor.rx_ukv_2_1[3] | (self.mainwind.Can_cor.rx_ukv_2_1[4] << 8)) / 10
        self.mainwind.label_311.setNum(sal_temp_2)
        # уставка температуры
        ust_temp_2 = (self.mainwind.Can_cor.rx_ukv_2_1[5] * 0.5 + 12)
        self.mainwind.label_310.setNum(ust_temp_2)
        # версия ПО
        soft_ver_2 = self.mainwind.Can_cor.rx_ukv_2_1[6]
        self.mainwind.label_65.setNum(soft_ver_2)
        # счётчик жизни УКВ
        life_cnt_2 = self.mainwind.Can_cor.rx_ukv_2_1[7]
        self.mainwind.label_79.setNum(life_cnt_2)

        