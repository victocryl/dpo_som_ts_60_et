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
        # бит Нет сети 400 В АС
        if (self.mainwind.Can_cor.rx_ukv_1_2[2] & sub.BIT5):
            self.mainwind.checkBox_149.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_149.setCheckState(Qt.Unchecked)
        
        # бит Неисп. приточ. вент. 1
        if (self.mainwind.Can_cor.rx_ukv_1_2[2] & sub.BIT6):
            self.mainwind.checkBox_156.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_156.setCheckState(Qt.Unchecked)
        
        # бит Неисп. приточ. вент. 2
        if (self.mainwind.Can_cor.rx_ukv_1_2[2] & sub.BIT7):
            self.mainwind.checkBox_155.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_155.setCheckState(Qt.Unchecked)
        
        # бит Неисп. засл. наруж. возд.
        if (self.mainwind.Can_cor.rx_ukv_1_2[3] & sub.BIT0):
            self.mainwind.checkBox_164.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_164.setCheckState(Qt.Unchecked)
        
        # бит Неисп. вент. наруж. возд.
        if (self.mainwind.Can_cor.rx_ukv_1_2[3] & sub.BIT1):
            self.mainwind.checkBox_145.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_145.setCheckState(Qt.Unchecked)
        
        # бит Нет сигн. гот. калориф.
        if (self.mainwind.Can_cor.rx_ukv_1_2[3] & sub.BIT3):
            self.mainwind.checkBox_162.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_162.setCheckState(Qt.Unchecked)
        
        # бит Неисп. компрессор 1
        if (self.mainwind.Can_cor.rx_ukv_1_2[3] & sub.BIT4):
            self.mainwind.checkBox_178.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_178.setCheckState(Qt.Unchecked)
        
        # бит Не норм. давл. контура 1
        if (self.mainwind.Can_cor.rx_ukv_1_2[3] & sub.BIT5):
            self.mainwind.checkBox_167.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_167.setCheckState(Qt.Unchecked)
        
        # бит Неисп. компрессор 2
        if (self.mainwind.Can_cor.rx_ukv_1_2[3] & sub.BIT6):
            self.mainwind.checkBox_153.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_153.setCheckState(Qt.Unchecked)
        
        # бит Не норм. давл. контура 2
        if (self.mainwind.Can_cor.rx_ukv_1_2[3] & sub.BIT7):
            self.mainwind.checkBox_154.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_154.setCheckState(Qt.Unchecked)
        
        # бит Неисп. вент. конденс. 1
        if (self.mainwind.Can_cor.rx_ukv_1_2[4] & sub.BIT1):
            self.mainwind.checkBox_168.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_168.setCheckState(Qt.Unchecked)
        
        # бит Неисп. вент. конденс. 2
        if (self.mainwind.Can_cor.rx_ukv_1_2[4] & sub.BIT2):
            self.mainwind.checkBox_166.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_166.setCheckState(Qt.Unchecked)
        
        # бит Неисп. вент. конденс. 3
        if (self.mainwind.Can_cor.rx_ukv_1_2[4] & sub.BIT3):
            self.mainwind.checkBox_147.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_147.setCheckState(Qt.Unchecked)
        
        # бит Засор. фильтр прит. вент.
        if (self.mainwind.Can_cor.rx_ukv_1_2[4] & sub.BIT5):
            self.mainwind.checkBox_151.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_151.setCheckState(Qt.Unchecked)
        
        # бит Засор. ф. вент. нар. возд.
        if (self.mainwind.Can_cor.rx_ukv_1_2[4] & sub.BIT6):
            self.mainwind.checkBox_177.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_177.setCheckState(Qt.Unchecked)
        
        # бит Неисп. д. н. давл. конт. 1
        if (self.mainwind.Can_cor.rx_ukv_1_2[4] & sub.BIT7):
            self.mainwind.checkBox_173.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_173.setCheckState(Qt.Unchecked)
        
        # бит Неисп. д. в. давл. конт. 1
        if (self.mainwind.Can_cor.rx_ukv_1_2[5] & sub.BIT0):
            self.mainwind.checkBox_172.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_172.setCheckState(Qt.Unchecked)
        
        # бит Неисп. д. н. давл. конт. 2
        if (self.mainwind.Can_cor.rx_ukv_1_2[5] & sub.BIT1):
            self.mainwind.checkBox_158.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_158.setCheckState(Qt.Unchecked)
        
        # бит Неисп. д. в. давл. конт. 2
        if (self.mainwind.Can_cor.rx_ukv_1_2[5] & sub.BIT2):
            self.mainwind.checkBox_182.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_182.setCheckState(Qt.Unchecked)
        
        # бит Неисп. датчик СО2
        if (self.mainwind.Can_cor.rx_ukv_1_2[5] & sub.BIT5):
            self.mainwind.checkBox_183.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_183.setCheckState(Qt.Unchecked)
        
        # бит Неисп. дат. темп. салона
        if (self.mainwind.Can_cor.rx_ukv_1_2[5] & sub.BIT6):
            self.mainwind.checkBox_184.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_184.setCheckState(Qt.Unchecked)
        
        # бит Неисп. дат. т. нар. возд.
        if (self.mainwind.Can_cor.rx_ukv_1_2[5] & sub.BIT7):
            self.mainwind.checkBox_181.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_181.setCheckState(Qt.Unchecked)
        
        # бит Неисп. дат. т. прит. возд.
        if (self.mainwind.Can_cor.rx_ukv_1_2[6] & sub.BIT0):
            self.mainwind.checkBox_169.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_169.setCheckState(Qt.Unchecked)
        
        # бит Темп. прит. в. слишк. выс.
        if (self.mainwind.Can_cor.rx_ukv_1_2[6] & sub.BIT4):
            self.mainwind.checkBox_186.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_186.setCheckState(Qt.Unchecked)
        
        # бит Темп. прит. в. слишк. низ.
        if (self.mainwind.Can_cor.rx_ukv_1_2[6] & sub.BIT5):
            self.mainwind.checkBox_157.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_157.setCheckState(Qt.Unchecked)
        
        # бит Слишк. выс. давл. конт. 1
        if (self.mainwind.Can_cor.rx_ukv_1_2[6] & sub.BIT6):
            self.mainwind.checkBox_170.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_170.setCheckState(Qt.Unchecked)
        
        # бит Слишк. выс. давл. конт. 2
        if (self.mainwind.Can_cor.rx_ukv_1_2[6] & sub.BIT7):
            self.mainwind.checkBox_185.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_185.setCheckState(Qt.Unchecked)
        
        # Вкл.реж.огр.мощ. конт. 1
        if (self.mainwind.Can_cor.rx_ukv_1_2[7] & sub.BIT0):
            self.mainwind.checkBox_187.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_187.setCheckState(Qt.Unchecked)
            
        # бит Вкл.реж.огр.мощ. конт. 2
        if (self.mainwind.Can_cor.rx_ukv_1_2[7] & sub.BIT1):
            self.mainwind.checkBox_188.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_188.setCheckState(Qt.Unchecked)


        if ((self.mainwind.Can_cor.rx_ukv_1_2[7] & sub.BIT0) or (self.mainwind.Can_cor.rx_ukv_1_2[7] & sub.BIT1)):
            self.mainwind.label_24.setText('ЕСТЬ')
        else:
            self.mainwind.label_24.setText('НЕТ')
        


        ############# УКВ 2 ####################################################################
        # бит Нет сети 400 В АС
        if (self.mainwind.Can_cor.rx_ukv_2_2[2] & sub.BIT5):
            self.mainwind.checkBox_209.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_209.setCheckState(Qt.Unchecked)
        
        # бит Неисп. приточ. вент. 1
        if (self.mainwind.Can_cor.rx_ukv_2_2[2] & sub.BIT6):
            self.mainwind.checkBox_208.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_208.setCheckState(Qt.Unchecked)
        
        # бит Неисп. приточ. вент. 2
        if (self.mainwind.Can_cor.rx_ukv_2_2[2] & sub.BIT7):
            self.mainwind.checkBox_206.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_206.setCheckState(Qt.Unchecked)
        
        # бит Неисп. засл. наруж. возд.
        if (self.mainwind.Can_cor.rx_ukv_2_2[3] & sub.BIT0):
            self.mainwind.checkBox_210.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_210.setCheckState(Qt.Unchecked)
        
        # бит Неисп. вент. наруж. возд.
        if (self.mainwind.Can_cor.rx_ukv_2_2[3] & sub.BIT1):
            self.mainwind.checkBox_211.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_211.setCheckState(Qt.Unchecked)
        
        # бит Нет сигн. гот. калориф.
        if (self.mainwind.Can_cor.rx_ukv_2_2[3] & sub.BIT3):
            self.mainwind.checkBox_212.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_212.setCheckState(Qt.Unchecked)
        
        # бит Неисп. компрессор 1
        if (self.mainwind.Can_cor.rx_ukv_2_2[3] & sub.BIT4):
            self.mainwind.checkBox_205.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_205.setCheckState(Qt.Unchecked)
        
        # бит Не норм. давл. контура 1
        if (self.mainwind.Can_cor.rx_ukv_2_2[3] & sub.BIT5):
            self.mainwind.checkBox_203.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_203.setCheckState(Qt.Unchecked)
        
        # бит Неисп. компрессор 2
        if (self.mainwind.Can_cor.rx_ukv_2_2[3] & sub.BIT6):
            self.mainwind.checkBox_214.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_214.setCheckState(Qt.Unchecked)
        
        # бит Не норм. давл. контура 2
        if (self.mainwind.Can_cor.rx_ukv_2_2[3] & sub.BIT7):
            self.mainwind.checkBox_202.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_202.setCheckState(Qt.Unchecked)
        
        # бит Неисп. вент. конденс. 1
        if (self.mainwind.Can_cor.rx_ukv_2_2[4] & sub.BIT1):
            self.mainwind.checkBox_207.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_207.setCheckState(Qt.Unchecked)
        
        # бит Неисп. вент. конденс. 2
        if (self.mainwind.Can_cor.rx_ukv_2_2[4] & sub.BIT2):
            self.mainwind.checkBox_204.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_204.setCheckState(Qt.Unchecked)
        
        # бит Неисп. вент. конденс. 3
        if (self.mainwind.Can_cor.rx_ukv_2_2[4] & sub.BIT3):
            self.mainwind.checkBox_213.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_213.setCheckState(Qt.Unchecked)
        
        # бит Засор. фильтр прит. вент.
        if (self.mainwind.Can_cor.rx_ukv_2_2[4] & sub.BIT5):
            self.mainwind.checkBox_215.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_215.setCheckState(Qt.Unchecked)
        
        # бит Засор. ф. вент. нар. возд.
        if (self.mainwind.Can_cor.rx_ukv_2_2[4] & sub.BIT6):
            self.mainwind.checkBox_216.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_216.setCheckState(Qt.Unchecked)
        
        # бит Неисп. д. н. давл. конт. 1
        if (self.mainwind.Can_cor.rx_ukv_2_2[4] & sub.BIT7):
            self.mainwind.checkBox_219.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_219.setCheckState(Qt.Unchecked)
        
        # бит Неисп. д. в. давл. конт. 1
        if (self.mainwind.Can_cor.rx_ukv_2_2[5] & sub.BIT0):
            self.mainwind.checkBox_225.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_225.setCheckState(Qt.Unchecked)
        
        # бит Неисп. д. н. давл. конт. 2
        if (self.mainwind.Can_cor.rx_ukv_2_2[5] & sub.BIT1):
            self.mainwind.checkBox_217.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_217.setCheckState(Qt.Unchecked)
        
        # бит Неисп. д. в. давл. конт. 2
        if (self.mainwind.Can_cor.rx_ukv_2_2[5] & sub.BIT2):
            self.mainwind.checkBox_226.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_226.setCheckState(Qt.Unchecked)
        
        # бит Неисп. датчик СО2
        if (self.mainwind.Can_cor.rx_ukv_2_2[5] & sub.BIT5):
            self.mainwind.checkBox_224.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_224.setCheckState(Qt.Unchecked)
        
        # бит Неисп. дат. темп. салона
        if (self.mainwind.Can_cor.rx_ukv_2_2[5] & sub.BIT6):
            self.mainwind.checkBox_223.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_223.setCheckState(Qt.Unchecked)
        
        # бит Неисп. дат. т. нар. возд.
        if (self.mainwind.Can_cor.rx_ukv_2_2[5] & sub.BIT7):
            self.mainwind.checkBox_218.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_218.setCheckState(Qt.Unchecked)
        
        # бит Неисп. дат. т. прит. возд.
        if (self.mainwind.Can_cor.rx_ukv_2_2[6] & sub.BIT0):
            self.mainwind.checkBox_221.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_221.setCheckState(Qt.Unchecked)
        
        # бит Темп. прит. в. слишк. выс.
        if (self.mainwind.Can_cor.rx_ukv_2_2[6] & sub.BIT4):
            self.mainwind.checkBox_222.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_222.setCheckState(Qt.Unchecked)
        
        # бит Темп. прит. в. слишк. низ.
        if (self.mainwind.Can_cor.rx_ukv_2_2[6] & sub.BIT5):
            self.mainwind.checkBox_230.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_230.setCheckState(Qt.Unchecked)
        
        # бит Слишк. выс. давл. конт. 1
        if (self.mainwind.Can_cor.rx_ukv_2_2[6] & sub.BIT6):
            self.mainwind.checkBox_220.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_220.setCheckState(Qt.Unchecked)
        
        # бит Слишк. выс. давл. конт. 2
        if (self.mainwind.Can_cor.rx_ukv_2_2[6] & sub.BIT7):
            self.mainwind.checkBox_228.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_228.setCheckState(Qt.Unchecked)
        
        # Вкл.реж.огр.мощ. конт. 1
        if (self.mainwind.Can_cor.rx_ukv_2_2[7] & sub.BIT0):
            self.mainwind.checkBox_229.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_229.setCheckState(Qt.Unchecked)
            
        # бит Вкл.реж.огр.мощ. конт. 2
        if (self.mainwind.Can_cor.rx_ukv_2_2[7] & sub.BIT1):
            self.mainwind.checkBox_227.setCheckState(Qt.Checked)
        else:
            self.mainwind.checkBox_227.setCheckState(Qt.Unchecked)
            

        if ((self.mainwind.Can_cor.rx_ukv_2_2[7] & sub.BIT0) or (self.mainwind.Can_cor.rx_ukv_2_2[7] & sub.BIT1)):
            self.mainwind.label_69.setText('ЕСТЬ')
        else:
            self.mainwind.label_69.setText('НЕТ')