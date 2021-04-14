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
        
        self.modes_retrieving()           # считываем режимы работы
        self.common_info_retrieving()     # считываем общую инфу
        self.params_retrieving_265_275()  # считываем параметры из rx265/275
        self.params_retrieving_266_276()  # считываем параметры из rx266/276
        self.params_retrieving_267_277()  # считываем параметры из rx267/277


    # @brief  Метод считывания режимов из посылки rx263/273
    # @param  None
    # @retval None
    def modes_retrieving(self):

        ############# УКВ 1 ####################################################################
        if (self.mainwind.Can_cor.rx_ukv_1_1[0] & sub.BIT0):
            self.mainwind.label_12.setText('ОТКЛЮЧЕНО')
            self.mainwind.checkBox_6.setCheckState(Qt.Unchecked)
        elif (self.mainwind.Can_cor.rx_ukv_1_1[0] & sub.BIT1):
            self.mainwind.label_12.setText('АВТОМАТИЧ.')
            self.mainwind.checkBox_6.setCheckState(Qt.Unchecked)
        elif (self.mainwind.Can_cor.rx_ukv_1_1[0] & sub.BIT2):
            self.mainwind.label_12.setText('ПОДОГРЕВ')
            self.mainwind.checkBox_6.setCheckState(Qt.Unchecked)
        elif (self.mainwind.Can_cor.rx_ukv_1_1[0] & sub.BIT3):
            self.mainwind.label_12.setText('ОХЛАЖДЕНИЕ')
            self.mainwind.checkBox_6.setCheckState(Qt.Unchecked)
        elif (self.mainwind.Can_cor.rx_ukv_1_1[0] & sub.BIT4):
            self.mainwind.label_12.setText('ВЕНТИЛЯЦИЯ')
            self.mainwind.checkBox_6.setCheckState(Qt.Unchecked)
        elif (self.mainwind.Can_cor.rx_ukv_1_1[0] & sub.BIT5):
            self.mainwind.label_12.setText('УСИЛ.ВЕНТИЛ.')
            self.mainwind.checkBox_6.setCheckState(Qt.Unchecked)
        elif (self.mainwind.Can_cor.rx_ukv_1_1[0] & sub.BIT6):
            self.mainwind.label_12.setText('ПОДГОТОВКА')
            self.mainwind.checkBox_6.setCheckState(Qt.Unchecked)
        elif (self.mainwind.Can_cor.rx_ukv_1_1[0] & sub.BIT7):
            self.mainwind.label_12.setText('ТЕСТОВЫЙ')
            self.mainwind.checkBox_6.setCheckState(Qt.Checked)
        else:
            self.mainwind.label_12.setText('НЕОПРЕД.')
            self.mainwind.checkBox_6.setCheckState(Qt.Unchecked)
        
        ############# УКВ 2 ####################################################################
        if (self.mainwind.Can_cor.rx_ukv_2_1[0] & sub.BIT0):
            self.mainwind.label_67.setText('ОТКЛЮЧЕНО')
            self.mainwind.checkBox_31.setCheckState(Qt.Unchecked)
        elif (self.mainwind.Can_cor.rx_ukv_2_1[0] & sub.BIT1):
            self.mainwind.label_67.setText('АВТОМАТИЧ.')
            self.mainwind.checkBox_31.setCheckState(Qt.Unchecked)
        elif (self.mainwind.Can_cor.rx_ukv_2_1[0] & sub.BIT2):
            self.mainwind.label_67.setText('ПОДОГРЕВ')
            self.mainwind.checkBox_31.setCheckState(Qt.Unchecked)
        elif (self.mainwind.Can_cor.rx_ukv_2_1[0] & sub.BIT3):
            self.mainwind.label_67.setText('ОХЛАЖДЕНИЕ')
            self.mainwind.checkBox_31.setCheckState(Qt.Unchecked)
        elif (self.mainwind.Can_cor.rx_ukv_2_1[0] & sub.BIT4):
            self.mainwind.label_67.setText('ВЕНТИЛЯЦИЯ')
            self.mainwind.checkBox_31.setCheckState(Qt.Unchecked)
        elif (self.mainwind.Can_cor.rx_ukv_2_1[0] & sub.BIT5):
            self.mainwind.label_67.setText('УСИЛ.ВЕНТИЛ.')
            self.mainwind.checkBox_31.setCheckState(Qt.Unchecked)
        elif (self.mainwind.Can_cor.rx_ukv_2_1[0] & sub.BIT6):
            self.mainwind.label_67.setText('ПОДГОТОВКА')
            self.mainwind.checkBox_31.setCheckState(Qt.Unchecked)
        elif (self.mainwind.Can_cor.rx_ukv_2_1[0] & sub.BIT7):
            self.mainwind.label_67.setText('ТЕСТОВЫЙ')
            self.mainwind.checkBox_31.setCheckState(Qt.Checked)
        else:
            self.mainwind.label_67.setText('НЕОПРЕД.')
            self.mainwind.checkBox_31.setCheckState(Qt.Unchecked)


    # @brief  Метод считывания общей информации из посылки rx263/273
    # @param  None
    # @retval None
    def common_info_retrieving(self):
        
        ############# УКВ 1 ####################################################################

        amb_temp_1 = ((self.mainwind.Can_cor.rx_ukv_1_1[1] << 8) | (self.mainwind.Can_cor.rx_ukv_1_1[2])) / 10
        self.mainwind.label_303.setNum(amb_temp_1)
        # температура салона
        sal_temp_1 = ((self.mainwind.Can_cor.rx_ukv_1_1[3] <<8) | (self.mainwind.Can_cor.rx_ukv_1_1[4])) / 10
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
        amb_temp_2 = ((self.mainwind.Can_cor.rx_ukv_2_1[1] << 8) | (self.mainwind.Can_cor.rx_ukv_2_1[2])) / 10
        self.mainwind.label_312.setNum(amb_temp_2)
        # температура салона
        sal_temp_2 = ((self.mainwind.Can_cor.rx_ukv_2_1[3] << 8) | (self.mainwind.Can_cor.rx_ukv_2_1[4])) / 10
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


    # @brief  Метод считывания параметров из rx265/275
    # @param  None
    # @retval None
    def params_retrieving_265_275(self):
        ############ УКВ1, 265 ############################################################
                
        # Скорость приточного вентилятора         
        speed_sup_vent_1 = self.mainwind.Can_cor.rx_ukv_1_3[0]
        self.mainwind.label_99.setNum(speed_sup_vent_1)
        # Скорость вентилятора конденсатора
        speed_cond_vent_1 = self.mainwind.Can_cor.rx_ukv_1_3[1]
        self.mainwind.label_170.setNum(speed_cond_vent_1)
        # Скорость вентилятора наружного воздуха
        speed_amb_vent_1 = self.mainwind.Can_cor.rx_ukv_1_3[2]
        self.mainwind.label_171.setNum(speed_amb_vent_1)
        # Усреднённая температура приточного воздуха
        aver_sup_temp_1 = ((self.mainwind.Can_cor.rx_ukv_1_3[4] << 8) | (self.mainwind.Can_cor.rx_ukv_1_3[5])) / 10
        self.mainwind.label_172.setNum(aver_sup_temp_1)
        # Датчик СО2
        sens_CO2_1 = ((self.mainwind.Can_cor.rx_ukv_1_3[6] << 8) | (self.mainwind.Can_cor.rx_ukv_1_3[7]))
        self.mainwind.label_173.setNum(sens_CO2_1)
    
     ############ УКВ2, 275 ############################################################
        # Скорость приточного вентилятора         
        speed_sup_vent_2 = self.mainwind.Can_cor.rx_ukv_2_3[0]
        self.mainwind.label_274.setNum(speed_sup_vent_2)
        # Скорость вентилятора конденсатора
        speed_cond_vent_2 = self.mainwind.Can_cor.rx_ukv_2_3[1]
        self.mainwind.label_265.setNum(speed_cond_vent_2)
        # Скорость вентилятора наружного воздуха
        speed_amb_vent_2 = self.mainwind.Can_cor.rx_ukv_2_3[2]
        self.mainwind.label_282.setNum(speed_amb_vent_2)
        # Усреднённая температура приточного воздуха
        aver_sup_temp_2 = ((self.mainwind.Can_cor.rx_ukv_2_3[4] << 8) | (self.mainwind.Can_cor.rx_ukv_2_3[5])) / 10
        self.mainwind.label_259.setNum(aver_sup_temp_2)
        # Датчик СО2
        sens_CO2_2 = ((self.mainwind.Can_cor.rx_ukv_2_3[6] << 8) | (self.mainwind.Can_cor.rx_ukv_2_3[7]))
        self.mainwind.label_273.setNum(sens_CO2_2)


    # @brief  Метод считывания параметров из rx266/276
    # @param  None
    # @retval None
    def params_retrieving_266_276(self):
        ############ УКВ1, 266 ############################################################
        # Температура приточного воздуха        
        sup_temp_1 = ((self.mainwind.Can_cor.rx_ukv_1_4[0] << 8) | (self.mainwind.Can_cor.rx_ukv_1_4[1])) / 10
        self.mainwind.label_174.setNum(sup_temp_1)
        # Низкое давление контура 1
        c_1_l_press_1 = self.mainwind.Can_cor.rx_ukv_1_4[4] * 0.05
        self.mainwind.label_175.setNum(c_1_l_press_1)
        # Высокое давление контура 1
        c_1_h_press_1 = self.mainwind.Can_cor.rx_ukv_1_4[5] * 0.15
        self.mainwind.label_176.setNum(c_1_h_press_1)
        # Низкое давление контура 2
        c_1_l_press_1 = self.mainwind.Can_cor.rx_ukv_1_4[6] * 0.05
        self.mainwind.label_177.setNum(c_1_l_press_1)
        # Высокое давление контура 2
        c_1_h_press_1 = self.mainwind.Can_cor.rx_ukv_1_4[7] * 0.15
        self.mainwind.label_178.setNum(c_1_h_press_1)

        ############ УКВ2, 276 ############################################################
        # Температура приточного воздуха        
        sup_temp_2 = ((self.mainwind.Can_cor.rx_ukv_2_4[0] << 8) | (self.mainwind.Can_cor.rx_ukv_2_4[1])) / 10
        self.mainwind.label_289.setNum(sup_temp_2)
        # Низкое давление контура 1
        c_1_l_press_2 = self.mainwind.Can_cor.rx_ukv_2_4[4] * 0.05
        self.mainwind.label_249.setNum(c_1_l_press_2)
        # Высокое давление контура 1
        c_1_h_press_2 = self.mainwind.Can_cor.rx_ukv_2_4[5] * 0.15
        self.mainwind.label_252.setNum(c_1_h_press_2)
        # Низкое давление контура 2
        c_1_l_press_2 = self.mainwind.Can_cor.rx_ukv_2_4[6] * 0.05
        self.mainwind.label_288.setNum(c_1_l_press_2)
        # Высокое давление контура 2
        c_1_h_press_2 = self.mainwind.Can_cor.rx_ukv_2_4[7] * 0.15
        self.mainwind.label_263.setNum(c_1_h_press_2)
    

    # @brief  Метод считывания параметров из rx267/277
    # @param  None
    # @retval None
    def params_retrieving_267_277(self):
        ############ УКВ1, 267 ############################################################
        # PID CO2       
        pid_CO2_1 = self.mainwind.Can_cor.rx_ukv_1_5[0]
        self.mainwind.label_179.setNum(pid_CO2_1)
        # PID отопления
        pid_heat_1 = self.mainwind.Can_cor.rx_ukv_1_5[1]
        self.mainwind.label_180.setNum(pid_heat_1)
        # PID охлаждения
        pid_cool_1 = self.mainwind.Can_cor.rx_ukv_1_5[2]
        self.mainwind.label_181.setNum(pid_cool_1)
        # PID мощности отопления
        pid_pwr_heat_1 = self.mainwind.Can_cor.rx_ukv_1_5[3]
        self.mainwind.label_182.setNum(pid_pwr_heat_1)
        # PID мощности охлаждения
        pid_pwr_cool_1 = self.mainwind.Can_cor.rx_ukv_1_5[4]
        self.mainwind.label_183.setNum(pid_pwr_cool_1)
        # Влажность наружного воздуха
        amb_humid_1 = self.mainwind.Can_cor.rx_ukv_1_5[5]
        self.mainwind.label_184.setNum(amb_humid_1)
        # Влажность воздуха в салоне
        sal_humid_1 = self.mainwind.Can_cor.rx_ukv_1_5[6]
        self.mainwind.label_102.setNum(sal_humid_1)

        ############ УКВ2, 277 ############################################################
        # PID CO2       
        pid_CO2_2 = self.mainwind.Can_cor.rx_ukv_2_5[0]
        self.mainwind.label_271.setNum(pid_CO2_1)
        # PID отопления
        pid_heat_2 = self.mainwind.Can_cor.rx_ukv_2_5[1]
        self.mainwind.label_287.setNum(pid_heat_1)
        # PID охлаждения
        pid_cool_2 = self.mainwind.Can_cor.rx_ukv_2_5[2]
        self.mainwind.label_294.setNum(pid_cool_1)
        # PID мощности отопления
        pid_pwr_heat_2 = self.mainwind.Can_cor.rx_ukv_2_5[3]
        self.mainwind.label_257.setNum(pid_pwr_heat_1)
        # PID мощности охлаждения
        pid_pwr_cool_2 = self.mainwind.Can_cor.rx_ukv_2_5[4]
        self.mainwind.label_291.setNum(pid_pwr_cool_1)
        # Влажность наружного воздуха
        amb_humid_2 = self.mainwind.Can_cor.rx_ukv_2_5[5]
        self.mainwind.label_276.setNum(amb_humid_1)
        # Влажность воздуха в салоне
        sal_humid_2 = self.mainwind.Can_cor.rx_ukv_2_5[6]
        self.mainwind.label_268.setNum(sal_humid_1)








        