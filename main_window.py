
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtCore import QTimer

import interface            # конвертированный файл дизайна
import can_init             # модуль инициализации и управления каналом can
import can_correspondence   # модуль всей корреспонденции по can
import tab_commands         # модуль вкладки Комманды
import tab_statuses         # модуль вкладки Статусы
import tab_failuries        # модуль вкладки Ошибки
import tab_params           # модуль вкладки Параметры


class MainWinowApp(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()  # нужно для доступа к переменным, методам и т.д. в файле design.py
        self.setupUi(self)  # нужно для инициализации design.py

        self.i = 0  # счётчик срабатываний таймера

        # создаём экземпляр класса Can_initialization
        self.Can_init = can_init.Can_initialization(self)
        # создаём экземпляр класса Can_corresp
        self.Can_cor = can_correspondence.Can_corresp(self)
        # создаём экземпляр класса Commands и передаём ему экземпляр класса MainWinowApp (это window в модуле main)
        self.C = tab_commands.Commands(self)
        # создаём экземпляр класса Status и передаём ему экземпляр класса MainWinowApp
        self.S = tab_statuses.Statuses(self)
        # создаём экземпляр класса Failuries и передаём ему экземпляр класса MainWinowApp
        self.F = tab_failuries.Failuries(self)
        # создаём экземпляр класса Params и передаём ему экземпляр класса MainWinowApp
        self.P = tab_params.Params(self)

        self.setWindowTitle("ДОПОЛНИТЕЛЬНОЕ ПО ДЛЯ ПРОЕКТА СОМ.ТС-60-ЕТ (ЕГИПЕТ)")
        self.common_init()      # первичное оформление интерфейса
        self.t = QTimer(self)   # создаём объект таймера и запускаем его
        self.t.start(1000)

        ################ КОННЕКТЫ ################################################################################
        self.t.timeout.connect(self.on_timer)   


    # @brief  Метод первичной инициализации интерфейса
    # @detail  Здесь задаются параметры интерфейса, которые будут отображаться сразу после загрузки приложения
    # @param  None
    # @retval None
    def common_init(self):

        # прописываем нули в лайнэдиты вкладки Команды
        self.lineEdit_3.setText("0")
        self.lineEdit_2.setText("0")
        self.lineEdit.setText("0")
        self.lineEdit_9.setText("0")
        self.lineEdit_7.setText("0")
        self.lineEdit_8.setText("0")

        ######################### тесты ################################################
        #self.init_for_tests()

        

    # @brief  Метод слота, реализующий действия по срабатыванию таймера.
    # @detail  Метод реализует следующие действия:
    # 1) Считываются галочки команд из закладки Комманды и их биты записываются в посылку tx (для обеих УКВ)
    # 2) Считываются параметры из закладки Комманды и их значения записываются в посылку tx (для обеих УКВ)
    # 3) Отправляются посылки tx (для обеих УКВ)
    # 4) Происходит получение входящих посылок в массивы rx (для обеих УКВ)
    # 5) Происходит распределение полученных данных в закладки Команды, Статусы, Ошибки, Параметры (для обеих УКВ)
    # @param  None
    # @retval None
    def on_timer(self):

        # чтение команд и параметров вкладки Команды (УКВ1 и УКВ2) и запись их в массивы tx
        self.C.commands_reading()
        # отправка посылок по CAN
        self.Can_cor.can_tx()
        # получение посылок из CAN
        self.Can_cor.can_rx()
        # получение из rx-массивов статусов систем (УКВ1 и УКВ2) и проставление галочек на вкладке Статусы
        self.S.statuses_reading()
        # получение из rx-массивов ошибок систем (УКВ1 и УКВ2) и проставление галочек на вкладке Ошибки
        self.F.failuries_reading()
        # получение из rx-массивов параметров систем (УКВ1 и УКВ2) и отображение их во вкладке Параметры
        self.P.params_reading()

        # счётчик жизни ДПО
        self.i += 1
        self.label_75.setNum(self.i)
        self.label_79.setNum(self.i)
        

        ################ ТЕСТЫ #####################################################################################
        # print(self.Can_cor.tx_ukv_1)
        # print(self.Can_cor.tx_ukv_2)
        # print(self.Can_cor.rx_ukv_1_2[0])


    def init_for_tests(self):
        # Инициализируем массив id 0x263 УКВ1 (режимы, параметры)
        self.Can_cor.rx_ukv_1_1[0] = 0b00000000
        self.Can_cor.rx_ukv_1_1[1] = 0b01000001
        self.Can_cor.rx_ukv_1_1[2] = 0b00000001
        self.Can_cor.rx_ukv_1_1[3] = 0b11101101
        self.Can_cor.rx_ukv_1_1[4] = 0b00000000
        self.Can_cor.rx_ukv_1_1[5] = 0b00010101
        self.Can_cor.rx_ukv_1_1[6] = 0b01111111
        self.Can_cor.rx_ukv_1_1[7] = 0b00000100
        # Инициализируем массив id 0x273 УКВ2 (режимы, параметры)
        self.Can_cor.rx_ukv_2_1[0] = 0b00000000
        self.Can_cor.rx_ukv_2_1[1] = 0b01000001
        self.Can_cor.rx_ukv_2_1[2] = 0b00000001
        self.Can_cor.rx_ukv_2_1[3] = 0b11101101
        self.Can_cor.rx_ukv_2_1[4] = 0b00000000
        self.Can_cor.rx_ukv_2_1[5] = 0b00010101
        self.Can_cor.rx_ukv_2_1[6] = 0b01111111
        self.Can_cor.rx_ukv_2_1[7] = 0b00000100

        # Инициализируем массив id 0x264 УКВ1 (там все статусы)
        self.Can_cor.rx_ukv_1_2[0] = 0b00000000
        self.Can_cor.rx_ukv_1_2[1] = 0b00000000
        self.Can_cor.rx_ukv_1_2[2] = 0b00000000 # статусы заканчиваются
        self.Can_cor.rx_ukv_1_2[3] = 0b00000000
        self.Can_cor.rx_ukv_1_2[4] = 0b00000000
        self.Can_cor.rx_ukv_1_2[5] = 0b00000000
        self.Can_cor.rx_ukv_1_2[6] = 0b00000000
        self.Can_cor.rx_ukv_1_2[7] = 0b00000000
        # Инициализируем массив id 0x274 УКВ2 (там все статусы)
        self.Can_cor.rx_ukv_2_2[0] = 0b00000000
        self.Can_cor.rx_ukv_2_2[1] = 0b00000000
        self.Can_cor.rx_ukv_2_2[2] = 0b00000000 # статусы заканчиваются
        self.Can_cor.rx_ukv_2_2[3] = 0b00000000
        self.Can_cor.rx_ukv_2_2[4] = 0b00000000
        self.Can_cor.rx_ukv_2_2[5] = 0b00000000
        self.Can_cor.rx_ukv_2_2[6] = 0b00000000
        self.Can_cor.rx_ukv_2_2[7] = 0b00000000

        # Инициализируем массив id 0x265 УКВ1
        self.Can_cor.rx_ukv_1_3[0] = 45
        self.Can_cor.rx_ukv_1_3[1] = 55
        self.Can_cor.rx_ukv_1_3[2] = 65
        self.Can_cor.rx_ukv_1_3[3] = 0
        self.Can_cor.rx_ukv_1_3[4] = 0b11011111
        self.Can_cor.rx_ukv_1_3[5] = 0b00000000
        self.Can_cor.rx_ukv_1_3[6] = 0b01010100
        self.Can_cor.rx_ukv_1_3[7] = 0b00000111
        # Инициализируем массив id 0x275 УКВ2
        self.Can_cor.rx_ukv_2_3[0] = 45
        self.Can_cor.rx_ukv_2_3[1] = 55
        self.Can_cor.rx_ukv_2_3[2] = 65
        self.Can_cor.rx_ukv_2_3[3] = 0
        self.Can_cor.rx_ukv_2_3[4] = 0b11011111
        self.Can_cor.rx_ukv_2_3[5] = 0b00000000
        self.Can_cor.rx_ukv_2_3[6] = 0b01010100
        self.Can_cor.rx_ukv_2_3[7] = 0b00000111

        # Инициализируем массив id 0x266 УКВ1
        self.Can_cor.rx_ukv_1_4[0] = 0b11101100
        self.Can_cor.rx_ukv_1_4[1] = 0b00000000
        self.Can_cor.rx_ukv_1_4[2] = 0
        self.Can_cor.rx_ukv_1_4[3] = 0
        self.Can_cor.rx_ukv_1_4[4] = 0b00000011
        self.Can_cor.rx_ukv_1_4[5] = 0b00000011
        self.Can_cor.rx_ukv_1_4[6] = 0b00000011
        self.Can_cor.rx_ukv_1_4[7] = 0b00000011
        # Инициализируем массив id 0x276 УКВ2
        self.Can_cor.rx_ukv_2_4[0] = 0b11101100
        self.Can_cor.rx_ukv_2_4[1] = 0b00000000
        self.Can_cor.rx_ukv_2_4[2] = 0
        self.Can_cor.rx_ukv_2_4[3] = 0
        self.Can_cor.rx_ukv_2_4[4] = 0b00000011
        self.Can_cor.rx_ukv_2_4[5] = 0b00000011
        self.Can_cor.rx_ukv_2_4[6] = 0b00000011
        self.Can_cor.rx_ukv_2_4[7] = 0b00000011

        # Инициализируем массив id 0x267 УКВ1
        self.Can_cor.rx_ukv_1_5[0] = 15
        self.Can_cor.rx_ukv_1_5[1] = 25
        self.Can_cor.rx_ukv_1_5[2] = 35
        self.Can_cor.rx_ukv_1_5[3] = 45
        self.Can_cor.rx_ukv_1_5[4] = 55
        self.Can_cor.rx_ukv_1_5[5] = 75
        self.Can_cor.rx_ukv_1_5[6] = 85
        self.Can_cor.rx_ukv_1_5[7] = 0
        # Инициализируем массив id 0x277 УКВ2
        self.Can_cor.rx_ukv_2_5[0] = 15
        self.Can_cor.rx_ukv_2_5[1] = 25
        self.Can_cor.rx_ukv_2_5[2] = 35
        self.Can_cor.rx_ukv_2_5[3] = 45
        self.Can_cor.rx_ukv_2_5[4] = 55
        self.Can_cor.rx_ukv_2_5[5] = 75
        self.Can_cor.rx_ukv_2_5[6] = 85
        self.Can_cor.rx_ukv_2_5[7] = 0



