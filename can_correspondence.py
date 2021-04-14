# Данный модуль содержит все айдишники, списки и методы для обеспечения 
# корреспонгденции по CAN в обе стороны

from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtCore import QTimer

from ctypes import *    # импортируем библиотеку ctypes
import can_init
import sub


class Can_corresp:
    def __init__ (self, mainwind):
        self.mainwind = mainwind
        self.transmit_error   = c_int16(-5)     # для хранения ошибок ф-ии CiTransmit()
        self.read_error       = c_int16(-5)     # для хранения ошибок ф-ии CiRead()
        self.old_cnt1 = 0
        self.new_cnt1 = 0
        self.old_cnt2 = 0
        self.new_cnt2 = 0
        self.ukv1_status = sub.ON
        self.ukv2_status = sub.ON

        # айдишники ДПО
        self.ID_TO_UKV_1 = 0x1C1
        self.ID_TO_UKV_2 = 0x1C3

        # айдишники УКВ 1
        self.ID_UKV_1_1 = 0x263
        self.ID_UKV_1_2 = 0x264
        self.ID_UKV_1_3 = 0x265
        self.ID_UKV_1_4 = 0x266
        self.ID_UKV_1_5 = 0x267

        # айдишники УКВ 2
        self.ID_UKV_2_1 = 0x273
        self.ID_UKV_2_2 = 0x274
        self.ID_UKV_2_3 = 0x275
        self.ID_UKV_2_4 = 0x276
        self.ID_UKV_2_5 = 0x277
        
        # сообщения от ДПО
        self.tx_ukv_1 = [0,0,0,0,0,0,0,0]    # список сообщения для УКВ1 (0x1C1)
        self.tx_ukv_2 = [0,0,0,0,0,0,0,0]    # список сообщения для УКВ2 (0x1C3)

        # сообщения от УКВ 1
        self.rx_ukv_1_1 = [0,0,0,0,0,0,0,0]    # (0x263)
        self.rx_ukv_1_2 = [0,0,0,0,0,0,0,0]    # (0x264)
        self.rx_ukv_1_3 = [0,0,0,0,0,0,0,0]    # (0x265)
        self.rx_ukv_1_4 = [0,0,0,0,0,0,0,0]    # (0x266)
        self.rx_ukv_1_5 = [0,0,0,0,0,0,0,0]    # (0x267)

        # сообщения от УКВ 2
        self.rx_ukv_2_1 = [0,0,0,0,0,0,0,0]    # (0x273)
        self.rx_ukv_2_2 = [0,0,0,0,0,0,0,0]    # (0x274)
        self.rx_ukv_2_3 = [0,0,0,0,0,0,0,0]    # (0x275)
        self.rx_ukv_2_4 = [0,0,0,0,0,0,0,0]    # (0x276)
        self.rx_ukv_2_5 = [0,0,0,0,0,0,0,0]    # (0x277)

        # создаём массив структур сообщний rx (приёмный буфер из 10 элементов)
        self.type_array = Canmsg_t * 10
        self.rx_data = Canmsg_t()
        self.rx_buffer = self.type_array(self.rx_data, self.rx_data, self.rx_data, self.rx_data, self.rx_data, self.rx_data, self.rx_data, self.rx_data, self.rx_data, self.rx_data)



    ##########################################################################################################
    ################## МЕТОДЫ ################################################################################
    ##########################################################################################################
    
    # @brief  Метод отправки посылок через адаптер
    # @param  None
    # @retval None
    def can_tx(self):
        if sub.can_status == sub.ON:    # всё делаем только если адаптер нормально подключен
            self.tx_data = Canmsg_t()           # создаём объект сообщения tx
            self.tx_data.len = 8                # указываем длину сообщения

            # инициализируем его данными посылки self.tx_ukv_1 (это сообщение для УКВ1 с id 0x1C1)
            self.tx_data.id = self.ID_TO_UKV_1  # присваиваем айдишник
            # заполняем данные
            for i in range(len(self.tx_ukv_1)):
                self.tx_data.data[i] = self.tx_ukv_1[i]
            # отправляем данные
            self.transmit_error.value = self.mainwind.Can_init.lib.CiTransmit(self.mainwind.Can_init.chan.value, self.tx_data)

            # инициализируем его данными посылки self.tx_ukv_2 (это сообщение для УКВ2 с id 0x1C3)
            self.tx_data.id = self.ID_TO_UKV_2  # присваиваем айдишник
            # заполняем данные
            for i in range(len(self.tx_ukv_2)):
                self.tx_data.data[i] = self.tx_ukv_2[i]
            # отправляем данные
            self.transmit_error.value = self.mainwind.Can_init.lib.CiTransmit(self.mainwind.Can_init.chan.value, self.tx_data)



    # @brief  Метод получения посылок
    # @param  None
    # @retval None
    def can_rx(self):
        
        if sub.can_status == sub.ON:
            # считываем всю очередь в приёмный буфер
            self.read_error.value = self.mainwind.Can_init.lib.CiRead(self.mainwind.Can_init.chan.value, self.rx_buffer, 10)

            self.rx_parsing(self.rx_buffer[0])
            self.rx_parsing(self.rx_buffer[1])
            self.rx_parsing(self.rx_buffer[2])
            self.rx_parsing(self.rx_buffer[3])
            self.rx_parsing(self.rx_buffer[4])
            self.rx_parsing(self.rx_buffer[5])
            self.rx_parsing(self.rx_buffer[6])
            self.rx_parsing(self.rx_buffer[7])
            self.rx_parsing(self.rx_buffer[8])
            self.rx_parsing(self.rx_buffer[9])

            

            # self.print_all_arrays()


    # @brief  Метод распределения данных согласно id-шникам из заданного элемента буфера
    # @param  src_buf - элемент буфера, из которого читаем данные
    # @retval None
    def rx_parsing(self, src_buf):
        
        if src_buf.id == int(self.ID_UKV_1_1):
            if self.ukv1_status == sub.ON:
                for i in range(len(self.rx_ukv_1_1)):
                    self.rx_ukv_1_1[i] = src_buf.data[i]
            else:
                self.rx_ukv_1_1[0] = 0
                self.rx_ukv_1_1[1] = 0
                self.rx_ukv_1_1[2] = 0
                self.rx_ukv_1_1[3] = 0
                self.rx_ukv_1_1[4] = 0
                self.rx_ukv_1_1[5] = 0
                self.rx_ukv_1_1[6] = 0
                self.rx_ukv_1_1[7] = src_buf.data[7]

        if src_buf.id == int(self.ID_UKV_1_2):
            if self.ukv1_status == sub.ON:
                for i in range(len(self.rx_ukv_1_2)):
                    self.rx_ukv_1_2[i] = src_buf.data[i]
            else:
                for i in range(len(self.rx_ukv_1_2)):
                    self.rx_ukv_1_2[i] = 0
        
        if src_buf.id == int(self.ID_UKV_1_3):
            if self.ukv1_status == sub.ON:
                for i in range(len(self.rx_ukv_1_3)):
                    self.rx_ukv_1_3[i] = src_buf.data[i]
            else:
                for i in range(len(self.rx_ukv_1_3)):
                    self.rx_ukv_1_3[i] = 0

        if src_buf.id == int(self.ID_UKV_1_4):
            if self.ukv1_status == sub.ON:
                for i in range(len(self.rx_ukv_1_4)):
                    self.rx_ukv_1_4[i] = src_buf.data[i]
            else:
                for i in range(len(self.rx_ukv_1_4)):
                    self.rx_ukv_1_4[i] = 0
        
        if src_buf.id == int(self.ID_UKV_1_5):
            if self.ukv1_status == sub.ON:
                for i in range(len(self.rx_ukv_1_5)):
                    self.rx_ukv_1_5[i] = src_buf.data[i]
            else:
                for i in range(len(self.rx_ukv_1_5)):
                    self.rx_ukv_1_5[i] = 0


        if src_buf.id == int(self.ID_UKV_2_1):
            if self.ukv2_status == sub.ON:
                for i in range(len(self.rx_ukv_2_1)):
                    self.rx_ukv_2_1[i] = src_buf.data[i]
            else:
                self.rx_ukv_2_1[0] = 0
                self.rx_ukv_2_1[1] = 0
                self.rx_ukv_2_1[2] = 0
                self.rx_ukv_2_1[3] = 0
                self.rx_ukv_2_1[4] = 0
                self.rx_ukv_2_1[5] = 0
                self.rx_ukv_2_1[6] = 0
                self.rx_ukv_2_1[7] = src_buf.data[7]
        
        if src_buf.id == int(self.ID_UKV_2_2):
            if self.ukv2_status == sub.ON:
                for i in range(len(self.rx_ukv_2_2)):
                    self.rx_ukv_2_2[i] = src_buf.data[i]
            else:
                for i in range(len(self.rx_ukv_2_2)):
                    self.rx_ukv_2_2[i] = 0
        
        if src_buf.id == int(self.ID_UKV_2_3):
            if self.ukv2_status == sub.ON:
                for i in range(len(self.rx_ukv_2_3)):
                    self.rx_ukv_2_3[i] = src_buf.data[i]
            else:
                for i in range(len(self.rx_ukv_2_3)):
                    self.rx_ukv_2_3[i] = 0
        
        if src_buf.id == int(self.ID_UKV_2_4):
            if self.ukv2_status == sub.ON:
                for i in range(len(self.rx_ukv_2_4)):
                    self.rx_ukv_2_4[i] = src_buf.data[i]
            else:
                for i in range(len(self.rx_ukv_2_4)):
                    self.rx_ukv_2_4[i] = 0
        
        if src_buf.id == int(self.ID_UKV_2_5):
            if self.ukv2_status == sub.ON:
                for i in range(len(self.rx_ukv_2_5)):
                    self.rx_ukv_2_5[i] = src_buf.data[i]
            else:
                for i in range(len(self.rx_ukv_2_5)):
                    self.rx_ukv_2_5[i] = 0


    # @brief  Метод слота, реализующий действия по срабатыванию таймера 2 (опред. активной УКВ)
    # @param  None
    # @retval None
    def ukv_active_determine(self):

        if sub.can_status == sub.ON:
            
            self.new_cnt1 = self.rx_ukv_1_1[7]
            if self.new_cnt1 == self.old_cnt1:
                self.mainwind.label_5.setStyleSheet("QLabel{color: rgb(0, 0, 0); }");  # делаем буквы чёрными
                self.ukv1_status = sub.OFF  # изменяем статус УКВ
            else:
                self.mainwind.label_5.setStyleSheet("QLabel{color: rgb(0, 170, 0); }");  # делаем буквы зелёными
                self.ukv1_status = sub.ON
                self.old_cnt1 = self.new_cnt1

            self.new_cnt2 = self.rx_ukv_2_1[7]
            if self.new_cnt2 == self.old_cnt2:
                self.mainwind.label_63.setStyleSheet("QLabel{color: rgb(0, 0, 0); }");  # делаем буквы чёрными
                self.ukv2_status = sub.OFF  # изменяем статус УКВ
            else:
                self.mainwind.label_63.setStyleSheet("QLabel{color: rgb(0, 170, 0); }");  # делаем буквы зелёными
                self.ukv2_status = sub.ON
                self.old_cnt2 = self.new_cnt2




##########################################################################################################
################## ТЕСТЫ #################################################################################
##########################################################################################################

    # @brief  Метод распечатывания всех массивов rx в консоль
    # @param  None
    # @retval None
    def print_all_arrays(self):
        print(f'rx_ukv_1_1: {self.rx_ukv_1_1}')
        # print(f'rx_ukv_1_2: {self.rx_ukv_1_2}')
        # print(f'rx_ukv_1_3: {self.rx_ukv_1_3}')
        # print(f'rx_ukv_1_4: {self.rx_ukv_1_4}')
        # print(f'rx_ukv_1_5: {self.rx_ukv_1_5}')
        print(f'rx_ukv_2_1: {self.rx_ukv_2_1}')
        # print(f'rx_ukv_2_2: {self.rx_ukv_2_2}')
        # print(f'rx_ukv_2_3: {self.rx_ukv_2_3}')
        # print(f'rx_ukv_2_4: {self.rx_ukv_2_4}')
        # print(f'rx_ukv_2_5: {self.rx_ukv_2_5}')
        # print('end of list')


##########################################################################################################
################## ВСПОМОГАТЕЛЬНЫЕ КЛАССЫ ################################################################
##########################################################################################################

# @brief  Класс описывающий структуру canmsg_t при помощи ctypes
# @param  None
# @retval None
class Canmsg_t(Structure):
    _fields_ = [('id', c_uint32),
                ('data', c_uint8 * 8),
                ('len', c_uint8),
                ('flags', c_uint16),
                ('ts', c_uint32)]


