# Данный модуль содержит атрибуты и методы для работы с вкладкой СТАТУСЫ

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, Qt
import sub

class Statuses:
    def __init__(self, mainwind):
        self.mainwind = mainwind



##########################################################################################################
################## МЕТОДЫ ################################################################################
##########################################################################################################

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
        
        # бит Воздушная заслонка открыта
        if (self.mainwind.Can_cor.rx_ukv_1_2[0] & sub.BIT2):
            self.mainwind.checkBox_148.setCheckState(Qt.Checked)
            self.mainwind.checkBox_88.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_148.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_88.setCheckState(Qt.Unchecked)

        # бит Вентилятор наружного воздуха включен
        if (self.mainwind.Can_cor.rx_ukv_1_2[0] & sub.BIT3):
            self.mainwind.checkBox_161.setCheckState(Qt.Checked)
            self.mainwind.checkBox_55.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_161.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_55.setCheckState(Qt.Unchecked)
        
        # бит Калорифер 1 включен
        if (self.mainwind.Can_cor.rx_ukv_1_2[0] & sub.BIT5):
            self.mainwind.checkBox_143.setCheckState(Qt.Checked)
            self.mainwind.checkBox_84.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_143.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_84.setCheckState(Qt.Unchecked)
        
        # бит Калорифер 2 включен
        if (self.mainwind.Can_cor.rx_ukv_1_2[0] & sub.BIT6):
            self.mainwind.checkBox_159.setCheckState(Qt.Checked)
            self.mainwind.checkBox_85.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_159.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_85.setCheckState(Qt.Unchecked)
        
        # бит Калорифер 3 включен
        if (self.mainwind.Can_cor.rx_ukv_1_2[0] & sub.BIT7):
            self.mainwind.checkBox_175.setCheckState(Qt.Checked)
            self.mainwind.checkBox_86.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_175.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_86.setCheckState(Qt.Unchecked)
        
        # бит Клапан 1-го контура включен
        if (self.mainwind.Can_cor.rx_ukv_1_2[1] & sub.BIT1):
            self.mainwind.checkBox_163.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_163.setCheckState(Qt.Unchecked)
        
        # бит Компрессор 1 включен
        if (self.mainwind.Can_cor.rx_ukv_1_2[1] & sub.BIT2):
            self.mainwind.checkBox_152.setCheckState(Qt.Checked)
            self.mainwind.checkBox_5.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_152.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_5.setCheckState(Qt.Unchecked)
        
        # бит Байпас контура 1 включен
        if (self.mainwind.Can_cor.rx_ukv_1_2[1] & sub.BIT3):
            self.mainwind.checkBox_142.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_142.setCheckState(Qt.Unchecked)
        
        # бит Регулировка произв. компрессора 1 включена
        if (self.mainwind.Can_cor.rx_ukv_1_2[1] & sub.BIT5):
            self.mainwind.checkBox_160.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_160.setCheckState(Qt.Unchecked)
        
        # бит Компрессор 2 включен
        if (self.mainwind.Can_cor.rx_ukv_1_2[1] & sub.BIT6):
            self.mainwind.checkBox_165.setCheckState(Qt.Checked)
            self.mainwind.checkBox_62.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_165.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_62.setCheckState(Qt.Unchecked)
        
        # бит Регулировка произв. компрессора 2 включена
        if (self.mainwind.Can_cor.rx_ukv_1_2[1] & sub.BIT7):
            self.mainwind.checkBox_146.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_146.setCheckState(Qt.Unchecked)
        
        # бит Вентилятор конденсатора 1 включен
        if (self.mainwind.Can_cor.rx_ukv_1_2[2] & sub.BIT1):
            self.mainwind.checkBox_150.setCheckState(Qt.Checked)
            self.mainwind.checkBox_2.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_150.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_2.setCheckState(Qt.Unchecked)
        
        # бит Вентилятор конденсатора 2 включен
        if (self.mainwind.Can_cor.rx_ukv_1_2[2] & sub.BIT2):
            self.mainwind.checkBox_174.setCheckState(Qt.Checked)
            self.mainwind.checkBox_3.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_174.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_3.setCheckState(Qt.Unchecked)
        
        # бит Вентилятор конденсатора 3 включен
        if (self.mainwind.Can_cor.rx_ukv_1_2[2] & sub.BIT3):
            self.mainwind.checkBox_176.setCheckState(Qt.Checked)
            self.mainwind.checkBox_4.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_176.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_4.setCheckState(Qt.Unchecked)
        
        ############# УКВ 2 ####################################################################
        # бит Приточный вентилятор 1 включен
        if (self.mainwind.Can_cor.rx_ukv_2_2[0] & sub.BIT0):
            self.mainwind.checkBox_193.setCheckState(Qt.Checked)
            self.mainwind.checkBox_106.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_193.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_106.setCheckState(Qt.Unchecked)
        
        # бит Приточный вентилятор 2 включен
        if (self.mainwind.Can_cor.rx_ukv_2_2[0] & sub.BIT1):
            self.mainwind.checkBox_200.setCheckState(Qt.Checked)
            self.mainwind.checkBox_107.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_200.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_107.setCheckState(Qt.Unchecked)
        
        # бит Воздушная заслонка открыта
        if (self.mainwind.Can_cor.rx_ukv_2_2[0] & sub.BIT2):
            self.mainwind.checkBox_195.setCheckState(Qt.Checked)
            self.mainwind.checkBox_102.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_195.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_102.setCheckState(Qt.Unchecked)

        # бит Вентилятор наружного воздуха включен
        if (self.mainwind.Can_cor.rx_ukv_2_2[0] & sub.BIT3):
            self.mainwind.checkBox_196.setCheckState(Qt.Checked)
            self.mainwind.checkBox_108.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_196.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_108.setCheckState(Qt.Unchecked)
        
        # бит Калорифер 1 включен
        if (self.mainwind.Can_cor.rx_ukv_2_2[0] & sub.BIT5):
            self.mainwind.checkBox_171.setCheckState(Qt.Checked)
            self.mainwind.checkBox_113.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_171.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_113.setCheckState(Qt.Unchecked)
        
        # бит Калорифер 2 включен
        if (self.mainwind.Can_cor.rx_ukv_2_2[0] & sub.BIT6):
            self.mainwind.checkBox_192.setCheckState(Qt.Checked)
            self.mainwind.checkBox_99.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_192.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_99.setCheckState(Qt.Unchecked)
        
        # бит Калорифер 3 включен
        if (self.mainwind.Can_cor.rx_ukv_2_2[0] & sub.BIT7):
            self.mainwind.checkBox_199.setCheckState(Qt.Checked)
            self.mainwind.checkBox_105.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_199.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_105.setCheckState(Qt.Unchecked)
        
        # бит Клапан 1-го контура включен
        if (self.mainwind.Can_cor.rx_ukv_2_2[1] & sub.BIT1):
            self.mainwind.checkBox_197.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_197.setCheckState(Qt.Unchecked)
        
        # бит Компрессор 1 включен
        if (self.mainwind.Can_cor.rx_ukv_2_2[1] & sub.BIT2):
            self.mainwind.checkBox_190.setCheckState(Qt.Checked)
            self.mainwind.checkBox_42.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_190.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_42.setCheckState(Qt.Unchecked)
        
        # бит Байпас контура 1 включен
        if (self.mainwind.Can_cor.rx_ukv_2_2[1] & sub.BIT3):
            self.mainwind.checkBox_194.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_194.setCheckState(Qt.Unchecked)
        
        # бит Регулировка произв. компрессора 1 включена
        if (self.mainwind.Can_cor.rx_ukv_2_2[1] & sub.BIT5):
            self.mainwind.checkBox_198.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_198.setCheckState(Qt.Unchecked)
        
        # бит Компрессор 2 включен
        if (self.mainwind.Can_cor.rx_ukv_2_2[1] & sub.BIT6):
            self.mainwind.checkBox_179.setCheckState(Qt.Checked)
            self.mainwind.checkBox_101.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_179.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_101.setCheckState(Qt.Unchecked)
        
        # бит Регулировка произв. компрессора 2 включена
        if (self.mainwind.Can_cor.rx_ukv_2_2[1] & sub.BIT7):
            self.mainwind.checkBox_180.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_180.setCheckState(Qt.Unchecked)
        
        # бит Вентилятор конденсатора 1 включен
        if (self.mainwind.Can_cor.rx_ukv_2_2[2] & sub.BIT1):
            self.mainwind.checkBox_191.setCheckState(Qt.Checked)
            self.mainwind.checkBox_28.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_191.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_28.setCheckState(Qt.Unchecked)
        
        # бит Вентилятор конденсатора 2 включен
        if (self.mainwind.Can_cor.rx_ukv_2_2[2] & sub.BIT2):
            self.mainwind.checkBox_189.setCheckState(Qt.Checked)
            self.mainwind.checkBox_29.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_189.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_29.setCheckState(Qt.Unchecked)
        
        # бит Вентилятор конденсатора 3 включен
        if (self.mainwind.Can_cor.rx_ukv_2_2[2] & sub.BIT3):
            self.mainwind.checkBox_201.setCheckState(Qt.Checked)
            self.mainwind.checkBox_30.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_201.setCheckState(Qt.Unchecked)
            self.mainwind.checkBox_30.setCheckState(Qt.Unchecked)