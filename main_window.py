
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtCore import QTimer

import interface            # конвертированный файл дизайна
import can_init             # модуль инициализации и управления каналом can
import can_correspondence   # модуль всей корреспонденции по can
import tab_commands         # модуль вкладки Комманды
import tab_statuses         # модуль вкладки Статусы
import tab_failuries        # модуль вкладки Ошибки


class MainWinowApp(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()  # нужно для доступа к переменным, методам и т.д. в файле design.py
        self.setupUi(self)  # нужно для инициализации design.py

        self.i = 0  # счётчик срабатываний таймера

        # создаём экземпляр класса Can_corresp
        self.Can_cor = can_correspondence.Can_corresp()
        # создаём экземпляр класса Commands и передаём ему экземпляр класса MainWinowApp (это window в модуле main)
        self.C = tab_commands.Commands(self)
        # создаём экземпляр класса Status и передаём ему экземпляр класса MainWinowApp
        self.S = tab_statuses.Statuses(self)
        # создаём экземпляр класса Failuries и передаём ему экземпляр класса MainWinowApp
        self.F = tab_failuries.Failuries(self)

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

        # Инициализируем массив id 0x264 УКВ1 (там все статусы)
        self.Can_cor.rx_ukv_1_2[0] = 0b00000000
        self.Can_cor.rx_ukv_1_2[1] = 0b00000000
        self.Can_cor.rx_ukv_1_2[2] = 0b00001000 # статусы заканчиваются
        self.Can_cor.rx_ukv_1_2[3] = 0b00000000
        self.Can_cor.rx_ukv_1_2[4] = 0b00000000
        self.Can_cor.rx_ukv_1_2[5] = 0b00000000
        self.Can_cor.rx_ukv_1_2[6] = 0b00000000
        self.Can_cor.rx_ukv_1_2[7] = 0b00000000

        # Инициализируем массив id 0x274 УКВ2 (там все статусы)
        self.Can_cor.rx_ukv_2_2[0] = 0b00000000
        self.Can_cor.rx_ukv_2_2[1] = 0b00000000
        self.Can_cor.rx_ukv_2_2[2] = 0b00001000 # статусы заканчиваются
        self.Can_cor.rx_ukv_2_2[3] = 0b00000000
        self.Can_cor.rx_ukv_2_2[4] = 0b00000000
        self.Can_cor.rx_ukv_2_2[5] = 0b00000000
        self.Can_cor.rx_ukv_2_2[6] = 0b00000000
        self.Can_cor.rx_ukv_2_2[7] = 0b00000000





    # # @brief  Метод, реализующий действия по срабатыванию таймера.
    # # @detail  Метод реализует следующие действия:
    # # 1) Считываются галочки команд из закладки Комманды и их биты записываются в посылку tx (для обеих УКВ)
    # # 2) Считываются параметры из закладки Комманды и их значения записываются в посылку tx (для обеих УКВ)
    # # 3) Отправляются посылки tx (для обеих УКВ)
    # # 4) Происходит получение входящих посылок в массивы rx (для обеих УКВ)
    # # 5) Происходит распределение полученных данных в закладки Команды, Статусы, Ошибки, Параметры (для обеих УКВ)
    # # @param  None
    # # @retval None
    def on_timer(self):

        # счётчик жизни
        self.i += 1
        self.Can_cor.tx_ukv_1[7] = self.i
        self.Can_cor.tx_ukv_2[7] = self.i
        self.label_75.setNum(self.i)
        self.label_79.setNum(self.i)

        # чтение команд и параметров вкладки Команды (УКВ1 и УКВ2) и запись их в массивы tx
        self.C.commands_reading()
        # получение из rx-массивов статусов систем (УКВ1 и УКВ2) и проставление галочек на вкладке Статусы
        self.S.statuses_reading()
        # получение из rx-массивов ошибок систем (УКВ1 и УКВ2) и проставление галочек на вкладке Ошибки
        self.F.failuries_reading()

        ################ ТЕСТЫ #####################################################################################
        # print(self.Can_cor.tx_ukv_1)
        # print(self.Can_cor.tx_ukv_2)
        # print(self.Can_cor.rx_ukv_1_2[0])

