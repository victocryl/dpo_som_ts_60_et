# Данный модуль содержит атрибуты и методы для работы с вкладкой КОМАНДЫ

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, Qt
import sub

class Commands:
    def __init__(self, mainwind):
        self.mainwind = mainwind

        # коннекты УКВ1
        self.mainwind.pushButton_4.clicked.connect(self.on_button_4)                # скор. прит. вент.
        self.mainwind.lineEdit_3.textChanged.connect(self.on_lineEdit_3_changed)
        self.mainwind.pushButton_3.clicked.connect(self.on_button_3)                # вент. конденсатора
        self.mainwind.lineEdit_2.textChanged.connect(self.on_lineEdit_2_changed)
        self.mainwind.pushButton_2.clicked.connect(self.on_button_2)                # вент. наруж. возд
        self.mainwind.lineEdit.textChanged.connect(self.on_lineEdit_changed)

        # коннекты УКВ2
        self.mainwind.pushButton_8.clicked.connect(self.on_button_8)                # скор. прит. вент.
        self.mainwind.lineEdit_9.textChanged.connect(self.on_lineEdit_9_changed)
        self.mainwind.pushButton_9.clicked.connect(self.on_button_9)                # вент. конденсатора
        self.mainwind.lineEdit_7.textChanged.connect(self.on_lineEdit_7_changed)
        self.mainwind.pushButton_10.clicked.connect(self.on_button_10)              # вент. наруж. возд
        self.mainwind.lineEdit_8.textChanged.connect(self.on_lineEdit_8_changed)






##########################################################################################################
################## МЕТОДЫ ################################################################################
##########################################################################################################

    # @brief  Метод чтения галочек на вкладке Команды
    # @detail Cчитываем состояние чекбоксов и проставляем биты в посылки tx
    # @param  None
    # @retval None
    def commands_reading(self):
    ############# УКВ 1 ####################################################################
        # бит тестового режима
        if self.mainwind.checkBox_7.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_1[0] |= sub.BIT0
            self.mainwind.label_12.setText('ТЕСТОВЫЙ')
        else:
            self.mainwind.Can_cor.tx_ukv_1[0] &= ~sub.BIT0
            self.mainwind.label_12.setText('ОТКЛЮЧЕНО')
        
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

############# УКВ 2 ####################################################################
        # бит тестового режима
        if self.mainwind.checkBox_23.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_2[0] |= sub.BIT0
            self.mainwind.label_67.setText('ТЕСТОВЫЙ')
        else:
            self.mainwind.Can_cor.tx_ukv_2[0] &= ~sub.BIT0
            self.mainwind.label_67.setText('ОТКЛЮЧЕНО')
        
        # бит компрессор 1
        if self.mainwind.checkBox_24.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_2[1] |= sub.BIT0
        else:
            self.mainwind.Can_cor.tx_ukv_2[1] &= ~sub.BIT0
        
        # бит клапан контура 1
        if self.mainwind.checkBox_32.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_2[1] |= sub.BIT1
        else:
            self.mainwind.Can_cor.tx_ukv_2[1] &= ~sub.BIT1
        
        # бит Вкл. рег. произв-ти компр. 1
        if self.mainwind.checkBox_110.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_2[1] |= sub.BIT2
        else:
            self.mainwind.Can_cor.tx_ukv_2[1] &= ~sub.BIT2
        
        # бит Вкл. компрессор 2
        if self.mainwind.checkBox_97.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_2[1] |= sub.BIT4
        else:
            self.mainwind.Can_cor.tx_ukv_2[1] &= ~sub.BIT4
            
        # бит Вкл. клапан контура 2
        if self.mainwind.checkBox_95.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_2[1] |= sub.BIT5
        else:
            self.mainwind.Can_cor.tx_ukv_2[1] &= ~sub.BIT5
            
        # бит Вкл. рег. произв-ти компр. 2
        if self.mainwind.checkBox_94.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_2[1] |= sub.BIT6
        else:
            self.mainwind.Can_cor.tx_ukv_2[1] &= ~sub.BIT6
            
        # бит Включить реверс вент-ров конденсатора
        if self.mainwind.checkBox_40.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_2[1] |= sub.BIT7
        else:
            self.mainwind.Can_cor.tx_ukv_2[1] &= ~sub.BIT7
            
        # бит Включить вентиляторы конденсатора
        if self.mainwind.checkBox_39.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_2[2] |= sub.BIT0
        else:
            self.mainwind.Can_cor.tx_ukv_2[2] &= ~sub.BIT0
            
        # бит Включить калорифер 1
        if self.mainwind.checkBox_114.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_2[2] |= sub.BIT1
        else:
            self.mainwind.Can_cor.tx_ukv_2[2] &= ~sub.BIT1
            
        # бит Включить калорифер 2
        if self.mainwind.checkBox_104.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_2[2] |= sub.BIT2
        else:
            self.mainwind.Can_cor.tx_ukv_2[2] &= ~sub.BIT2
            
        # бит Включить калорифер 3
        if self.mainwind.checkBox_98.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_2[2] |= sub.BIT3
        else:
            self.mainwind.Can_cor.tx_ukv_2[2] &= ~sub.BIT3
            
        # бит Включить приточные вентиляторы
        if self.mainwind.checkBox_96.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_2[2] |= sub.BIT4
        else:
            self.mainwind.Can_cor.tx_ukv_2[2] &= ~sub.BIT4
            
        # бит Включить вентилятор наружного воздуха
        if self.mainwind.checkBox_103.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_2[2] |= sub.BIT5
        else:
            self.mainwind.Can_cor.tx_ukv_2[2] &= ~sub.BIT5
            
        # бит Открыть воздушную заслонку
        if self.mainwind.checkBox_109.checkState() == Qt.Checked:
            self.mainwind.Can_cor.tx_ukv_2[2] |= sub.BIT6
        else:
            self.mainwind.Can_cor.tx_ukv_2[2] &= ~sub.BIT6

##########################################################################################################
################## СЛОТЫ #################################################################################
##########################################################################################################

################### УКВ1 #################################################################################

    # @brief  слот на нажатие кнопки Задать скорость прит. вент.
    # @param  None
    # @retval None
    def on_button_4(self):
        self.str = int(self.mainwind.lineEdit_3.text()) # забираем строку из lineedit И преобр. в int
        if (self.str < 0 or self.str > 100):
            self.mainwind.label_4.setText('НЕПРАВИЛЬНЫЙ ФОРМАТ ВВОДИМОГО ЧИСЛА (0 < число <100)')
            self.mainwind.label_4.setStyleSheet("QLabel{color: rgb(255, 10, 0); }");  # делаем текст красным
        else:
            self.mainwind.Can_cor.tx_ukv_1[4] = self.str
            self.mainwind.label_4.setText('')
            self.mainwind.label_4.setStyleSheet("QLabel{color: rgb(0, 0, 0); }");  # делаем текст чёрным
            self.mainwind.label_15.setText('задано')
            self.mainwind.label_15.setStyleSheet("QLabel{color: rgb(0, 0, 0); }");

    # @brief  слот редактирование lineedit Задать скорость прит. вент.
    # @param  None
    # @retval None
    def on_lineEdit_3_changed(self):
        self.mainwind.label_15.setText('не задано')
        self.mainwind.label_15.setStyleSheet("QLabel{color: rgb(255, 10, 0); }");  # делаем текст красным

    # @brief  слот на нажатие кнопки Задать скорость вент. конденс.
    # @param  None
    # @retval None
    def on_button_3(self):
        self.str = int(self.mainwind.lineEdit_2.text()) # забираем строку из lineedit И преобр. в int
        if (self.str < 0 or self.str > 100):
            self.mainwind.label_4.setText('НЕПРАВИЛЬНЫЙ ФОРМАТ ВВОДИМОГО ЧИСЛА (0 < число <100)')
            self.mainwind.label_4.setStyleSheet("QLabel{color: rgb(255, 10, 0); }");  # делаем текст красным
        else:
            self.mainwind.Can_cor.tx_ukv_1[5] = self.str
            self.mainwind.label_4.setText('')
            self.mainwind.label_4.setStyleSheet("QLabel{color: rgb(0, 0, 0); }");  # делаем текст чёрным
            self.mainwind.label_14.setText('задано')
            self.mainwind.label_14.setStyleSheet("QLabel{color: rgb(0, 0, 0); }");

    # @brief  слот редактирование lineedit Задать скорость вент. конденс.
    # @param  None
    # @retval None
    def on_lineEdit_2_changed(self):
        self.mainwind.label_14.setText('не задано')
        self.mainwind.label_14.setStyleSheet("QLabel{color: rgb(255, 10, 0); }");  # делаем текст красным

    # @brief  слот на нажатие кнопки Задать скорость вент. наруж. воздуха
    # @param  None
    # @retval None
    def on_button_2(self):
        self.str = int(self.mainwind.lineEdit.text()) # забираем строку из lineedit И преобр. в int
        if (self.str < 0 or self.str > 100):
            self.mainwind.label_4.setText('НЕПРАВИЛЬНЫЙ ФОРМАТ ВВОДИМОГО ЧИСЛА (0 < число <100)')
            self.mainwind.label_4.setStyleSheet("QLabel{color: rgb(255, 10, 0); }");  # делаем текст красным
        else:
            self.mainwind.Can_cor.tx_ukv_1[6] = self.str
            self.mainwind.label_4.setText('')
            self.mainwind.label_4.setStyleSheet("QLabel{color: rgb(0, 0, 0); }");  # делаем текст чёрным
            self.mainwind.label_13.setText('задано')
            self.mainwind.label_13.setStyleSheet("QLabel{color: rgb(0, 0, 0); }");

    # @brief  слот редактирование lineedit Задать скорость вент. наруж. воздуха
    # @param  None
    # @retval None
    def on_lineEdit_changed(self):
        self.mainwind.label_13.setText('не задано')
        self.mainwind.label_13.setStyleSheet("QLabel{color: rgb(255, 10, 0); }");  # делаем текст красным

################### УКВ2 #################################################################################

    # @brief  слот на нажатие кнопки Задать скорость прит. вент.
    # @param  None
    # @retval None
    def on_button_8(self):
        self.str = int(self.mainwind.lineEdit_9.text()) # забираем строку из lineedit И преобр. в int
        if (self.str < 0 or self.str > 100):
            self.mainwind.label_4.setText('НЕПРАВИЛЬНЫЙ ФОРМАТ ВВОДИМОГО ЧИСЛА (0 < число <100)')
            self.mainwind.label_4.setStyleSheet("QLabel{color: rgb(255, 10, 0); }");  # делаем текст красным
        else:
            self.mainwind.Can_cor.tx_ukv_2[4] = self.str
            self.mainwind.label_4.setText('')
            self.mainwind.label_4.setStyleSheet("QLabel{color: rgb(0, 0, 0); }");  # делаем текст чёрным
            self.mainwind.label_93.setText('задано')
            self.mainwind.label_93.setStyleSheet("QLabel{color: rgb(0, 0, 0); }");

    # @brief  слот редактирование lineedit Задать скорость прит. вент.
    # @param  None
    # @retval None
    def on_lineEdit_9_changed(self):
        self.mainwind.label_93.setText('не задано')
        self.mainwind.label_93.setStyleSheet("QLabel{color: rgb(255, 10, 0); }");  # делаем текст красным

    # @brief  слот на нажатие кнопки Задать скорость вент. конденс.
    # @param  None
    # @retval None
    def on_button_9(self):
        self.str = int(self.mainwind.lineEdit_7.text()) # забираем строку из lineedit И преобр. в int
        if (self.str < 0 or self.str > 100):
            self.mainwind.label_4.setText('НЕПРАВИЛЬНЫЙ ФОРМАТ ВВОДИМОГО ЧИСЛА (0 < число <100)')
            self.mainwind.label_4.setStyleSheet("QLabel{color: rgb(255, 10, 0); }");  # делаем текст красным
        else:
            self.mainwind.Can_cor.tx_ukv_2[5] = self.str
            self.mainwind.label_4.setText('')
            self.mainwind.label_4.setStyleSheet("QLabel{color: rgb(0, 0, 0); }");  # делаем текст чёрным
            self.mainwind.label_95.setText('задано')
            self.mainwind.label_95.setStyleSheet("QLabel{color: rgb(0, 0, 0); }");

    # @brief  слот редактирование lineedit Задать скорость вент. конденс.
    # @param  None
    # @retval None
    def on_lineEdit_7_changed(self):
        self.mainwind.label_95.setText('не задано')
        self.mainwind.label_95.setStyleSheet("QLabel{color: rgb(255, 10, 0); }");  # делаем текст красным

    # @brief  слот на нажатие кнопки Задать скорость вент. наруж. воздуха
    # @param  None
    # @retval None
    def on_button_10(self):
        self.str = int(self.mainwind.lineEdit_8.text()) # забираем строку из lineedit И преобр. в int
        if (self.str < 0 or self.str > 100):
            self.mainwind.label_4.setText('НЕПРАВИЛЬНЫЙ ФОРМАТ ВВОДИМОГО ЧИСЛА (0 < число <100)')
            self.mainwind.label_4.setStyleSheet("QLabel{color: rgb(255, 10, 0); }");  # делаем текст красным
        else:
            self.mainwind.Can_cor.tx_ukv_2[6] = self.str
            self.mainwind.label_4.setText('')
            self.mainwind.label_4.setStyleSheet("QLabel{color: rgb(0, 0, 0); }");  # делаем текст чёрным
            self.mainwind.label_94.setText('задано')
            self.mainwind.label_94.setStyleSheet("QLabel{color: rgb(0, 0, 0); }");

    # @brief  слот редактирование lineedit Задать скорость вент. наруж. воздуха
    # @param  None
    # @retval None
    def on_lineEdit_8_changed(self):
        self.mainwind.label_94.setText('не задано')
        self.mainwind.label_94.setStyleSheet("QLabel{color: rgb(255, 10, 0); }");  # делаем текст красным
