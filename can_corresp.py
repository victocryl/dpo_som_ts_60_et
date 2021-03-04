
class Can_corresp:
    def __init__ (self):

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
        self.to_ukv_1 = [0,0,0,0,0,0,0,0]    # список сообщения для УКВ1 (0x1C1)
        self.to_ukv_2 = [0,0,0,0,0,0,0,0]    # список сообщения для УКВ2 (0x1C3)

        # сообщения от УКВ 1
        self.from_ukv_1_1 = [0,0,0,0,0,0,0,0]    # (0x263)
        self.from_ukv_1_2 = [0,0,0,0,0,0,0,0]    # (0x264)
        self.from_ukv_1_3 = [0,0,0,0,0,0,0,0]    # (0x265)
        self.from_ukv_1_4 = [0,0,0,0,0,0,0,0]    # (0x266)
        self.from_ukv_1_5 = [0,0,0,0,0,0,0,0]    # (0x267)

        # сообщения от УКВ 2
        self.from_ukv_2_1 = [0,0,0,0,0,0,0,0]    # (0x273)
        self.from_ukv_2_2 = [0,0,0,0,0,0,0,0]    # (0x274)
        self.from_ukv_2_3 = [0,0,0,0,0,0,0,0]    # (0x275)
        self.from_ukv_2_4 = [0,0,0,0,0,0,0,0]    # (0x276)
        self.from_ukv_2_5 = [0,0,0,0,0,0,0,0]    # (0x277)
