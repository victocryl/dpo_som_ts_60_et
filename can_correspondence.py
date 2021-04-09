# Данный модуль содержит все айдишники, списки и методы для обеспечения 
# корреспонгденции по CAN в обе стороны

import can_init

from ctypes import *    # импортируем библиотеку ctypes
import sub


class Can_corresp:
    def __init__ (self, mainwind):
        self.mainwind = mainwind
        self.transmit_error   = c_int16(-5)     # для хранения ошибок ф-ии CiTransmit()
        self.read_error       = c_int16(-5)     # для хранения ошибок ф-ии CiRead()

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
            self.tx_data = Canmsg_t()               # создаём объект сообщения tx
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

            print(f'tx_ukv_1 {self.tx_ukv_1}')



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

            self.print_all_arrays()


    # @brief  Метод распределения данных согласно id-шникам из заданного элемента буфера
    # @param  src_buf - элемент буфера, из которого читаем данные
    # @retval None
    def rx_parsing(self, src_buf):
        
        if src_buf.id == int(self.ID_UKV_1_1):
            for i in range(len(self.rx_ukv_1_1)):
                self.rx_ukv_1_1[i] = src_buf.data[i]
        
        if src_buf.id == int(self.ID_UKV_1_2):
            for i in range(len(self.rx_ukv_1_2)):
                self.rx_ukv_1_2[i] = src_buf.data[i]
        
        if src_buf.id == int(self.ID_UKV_1_3):
            for i in range(len(self.rx_ukv_1_3)):
                self.rx_ukv_1_3[i] = src_buf.data[i]

        if src_buf.id == int(self.ID_UKV_1_4):
            for i in range(len(self.rx_ukv_1_4)):
                self.rx_ukv_1_4[i] = src_buf.data[i]
        
        if src_buf.id == int(self.ID_UKV_1_5):
            for i in range(len(self.rx_ukv_1_5)):
                self.rx_ukv_1_5[i] = src_buf.data[i]
        
        if src_buf.id == int(self.ID_UKV_2_1):
            for i in range(len(self.rx_ukv_2_1)):
                self.rx_ukv_2_1[i] = src_buf.data[i]
        
        if src_buf.id == int(self.ID_UKV_2_2):
            for i in range(len(self.rx_ukv_2_2)):
                self.rx_ukv_2_2[i] = src_buf.data[i]
        
        if src_buf.id == int(self.ID_UKV_2_3):
            for i in range(len(self.rx_ukv_2_3)):
                self.rx_ukv_2_3[i] = src_buf.data[i]
        
        if src_buf.id == int(self.ID_UKV_2_4):
            for i in range(len(self.rx_ukv_2_4)):
                self.rx_ukv_2_4[i] = src_buf.data[i]
        
        if src_buf.id == int(self.ID_UKV_2_5):
            for i in range(len(self.rx_ukv_2_5)):
                self.rx_ukv_2_5[i] = src_buf.data[i]
    

    # @brief  Метод распечатывания всех массивов rx в консоль
    # @param  None
    # @retval None
    def print_all_arrays(self):
        print(f'rx_ukv_1_1: {self.rx_ukv_1_1}')
        print(f'rx_ukv_1_2: {self.rx_ukv_1_2}')
        print(f'rx_ukv_1_3: {self.rx_ukv_1_3}')
        print(f'rx_ukv_1_4: {self.rx_ukv_1_4}')
        print(f'rx_ukv_1_5: {self.rx_ukv_1_5}')
        print(f'rx_ukv_2_1: {self.rx_ukv_2_1}')
        print(f'rx_ukv_2_2: {self.rx_ukv_2_2}')
        print(f'rx_ukv_2_3: {self.rx_ukv_2_3}')
        print(f'rx_ukv_2_4: {self.rx_ukv_2_4}')
        print(f'rx_ukv_2_5: {self.rx_ukv_2_5}')
        print('end of list')




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
