
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import interface  # конвертированный файл дизайна
import can_init  # модуль инициализации и управления каналом can
import can_corresp  # модуль всей корреспонденции по can

class ExampleApp(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()  # нужно для доступа к переменным, методам и т.д. в файле design.py
        self.setupUi(self)  # нужно для инициализации design.py
        self.setWindowTitle("ДОПОЛНИТЕЛЬНОЕ ПО ДЛЯ ПРОЕКТА СОМ.ТС-60-ЕТ (ЕГИПЕТ)")
        self.common_init()



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









        # self.pushButton.clicked.connect(self.on_button)

    # def on_button(self):
    #     self.label.setText("dfdfg")
    #     print("dfggfdbgfd")