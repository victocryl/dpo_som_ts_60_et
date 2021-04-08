# в данном модуле происходит инициализация канала CAN и управление им (подключение/отключение)

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from ctypes import *    # импортируем библиотеку ctypes
import sub

class Can_initialization:
    def __init__(self, mainwind):
        self.mainwind = mainwind

        ############# переменные CAN ###################################################################################
        self.init_error       = c_int16(-5)     # для хранения ошибок инициализации
        self.board_info_error = c_int16(-5)     # для хранения ошибок ф-ии CiBoardInfo()
        self.chan_open_error  = c_int16(-5)     # для хранения ошибок ф-ии CiOpen()
        self.start_error      = c_int16(-5)     # для хранения ошибок ф-ии CiStart()
        # задаём номер открываемого канала и формат кадра для всех методов инициализации
        self.chan = c_uint8(0)   # задаём номер открываемого канала
        self.flags = c_uint8(0x2 | 0x4)  # задаём формат кадра (по умолчанию, если 0, то 11 битный формат)

        ############# инициализация библиотеки Chai (это нужно делать один раз) ########################################
        # self.lib = cdll.chai                        # создаём объект библиотеки chai
        self.lib = CDLL(r"chai.dll")    # D:\PY_projects\dpo_som_ts_60_et\lib\
        self.init_error.value = self.lib.CiInit()   # вызываем ф-ию инициализации либы

        # коннект на кнопку Подключиться
        self.mainwind.pushButton.clicked.connect(self.on_button)


    # @brief  Метод подключения устройства
    # @param  None
    # @retval 0 - если подключение успешно, 1 - если не успешно
    def device_connect(self):
        ############# вызов ф-ии CiBoardInfo() - информация о девайсе ###################################################
        self.board_data = Сanboard_t()  # создаём объект структуры canboard_t
        self.board_data.brdnum = 0      # задаём номер платы, о которой хотим получить инфо

        self.board_info_error.value = self.lib.CiBoardInfo(self.board_data) # вызов ф-ии CiBoardInfo()
        # print(self.board_data.brdnum)
        # print(self.board_data.hwver)
        # print(self.board_data.chip[0])
        # print(self.board_data.name)
        # print(self.board_data.manufact)
        # print(f"self.board_info_error после: {self.board_info_error.value}")     # после ...

        ############# вызов ф-ии CiOpen() - открытие канала ###################################################
        self.chan_open_error.value = self.lib.CiOpen(self.chan.value, self.flags.value)     # открываем канал

        # проверяем, подключен ли девайс
        if self.chan_open_error.value == 0:
            ############# конфигурирование канала ##################################################################
            self.lib.CiRcQueResize(self.chan.value, 10)         # задаём размер приёмной очереди
            self.lib.CiSetBaud(self.chan.value, 0x01, 0x1c)     # задаём скорость 250 кбит/с
            ############# запуск канала CiStart() ##################################################################
            # входящий параметр self.chan определён ранее
            self.start_error.value = self.lib.CiStart(self.chan.value)     # запускаем канал
            return 0
        else:
            return 1

    # @brief  Метод отключения устройства
    # @param  None
    # @retval None
    def device_disconnect(self):
        self.lib.CiStop(self.chan.value)    # останавливаем канал CiStop()
        self.lib.CiClose(self.chan.value)   # закрываем канал CiClose()

        
    
    
    
    ##########################################################################################################
    ################## СЛОТЫ #################################################################################
    ##########################################################################################################
    
    # @brief  Слот нажатия на кнопку Подключиться
    # @param  None
    # @retval None
    def on_button(self):
        if sub.can_status == sub.OFF:
            if self.device_connect() == 0:  # если девайс нормально подключен
                self.mainwind.pushButton.setText('отключиться x')
                self.mainwind.label_4.setText('адаптер "Марафон" подключен')
                self.mainwind.label_4.setStyleSheet("QLabel{color: rgb(0, 0, 0); }");  # делаем текст чёрным
                sub.can_status = sub.ON
            else:
                self.mainwind.label_4.setText('АДАПТЕР НЕ ПОДКЛЮЧЕН ИЛИ НЕ ТОГО ТИПА')
                self.mainwind.label_4.setStyleSheet("QLabel{color: rgb(255, 10, 0); }");  # делаем текст красным
        else:
            self.device_disconnect()
            self.mainwind.pushButton.setText('подключиться ->')
            self.mainwind.label_4.setText('адаптер отключен')
            self.mainwind.label_4.setStyleSheet("QLabel{color: rgb(0, 0, 0); }");  # делаем текст чёрным
            sub.can_status = sub.OFF



##########################################################################################################
################## ВСПОМОГАТЕЛЬНЫЕ КЛАССЫ ################################################################
##########################################################################################################

# @brief  Класс описывающий структуру сanboard_t при помощи ctypes
# @param  None
# @retval None
class Сanboard_t(Structure):
    _fields_ = [('brdnum', c_uint8),
                ('hwver', c_uint32),
                ('chip', c_int16 * 4),
                ('name', c_char * 64),
                ('manufact', c_char * 64)]
