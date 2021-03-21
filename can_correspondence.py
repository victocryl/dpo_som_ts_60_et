# Данный модуль содержит все айдишники, списки и методы для обеспечения 
# корреспонгденции по CAN в обе стороны

import can_init

from ctypes import *    # импортируем библиотеку ctypes
import sub


class Can_corresp:
    def __init__ (self, mainwind):
        self.mainwind = mainwind
        self.transmit_error   = c_int16(-5)     # для хранения ошибок ф-ии CiTransmit()

        # айдишники ДПО
        self.ID_TO_UKV_1 = 0x1C1
        self.ID_TO_UKV_2 = 0x1C3

        # айдишники УКВ 1
        self.ID_FROM_UKV_1_1 = 0x263
        self.ID_FROM_UKV_1_2 = 0x264
        self.ID_FROM_UKV_1_3 = 0x265
        self.ID_FROM_UKV_1_4 = 0x266
        self.ID_FROM_UKV_1_5 = 0x267

        # айдишники УКВ 2
        self.ID_FROM_UKV_2_1 = 0x273
        self.ID_FROM_UKV_2_2 = 0x274
        self.ID_FROM_UKV_2_3 = 0x275
        self.ID_FROM_UKV_2_4 = 0x276
        self.ID_FROM_UKV_2_5 = 0x277
        
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
    

    ##########################################################################################################
    ################## МЕТОДЫ ################################################################################
    ##########################################################################################################
    
    # @brief  Метод отправки посылок через адаптер
    # @detail  Здесь задаются параметры интерфейса, которые будут отображаться сразу после загрузки приложения
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
