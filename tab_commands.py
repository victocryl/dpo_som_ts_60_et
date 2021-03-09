# Данный модуль содержит атрибуты и методы для работы с вкладкой КОМАНДЫ

class Commands:
    def __init__(self, mainwind):

        mainwind.pushButton_4.clicked.connect(self.on_button)

    def on_button(self):
        #self.label.setText("dfdfg")
        print("dfggfdbgfd")

    # @brief  Метод слота при клике чекбокса Включить тестовый режим
    # @param  None
    # @retval None
    def on_checkbox_7(self):
        # считываем состояние чекбокса

        # ветвление если чекед - одно, если анчекед - другое
        # 1) загружаем бит в байт посылки
        # 2) стираем бит из посылки
        pass
