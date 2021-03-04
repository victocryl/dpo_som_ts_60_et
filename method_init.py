
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import interface  # конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        
        super().__init__()  # нужно для доступа к переменным, методам и т.д. в файле design.py
        self.setupUi(self)  # нужно для инициализации design.py
        self.setWindowTitle("ДОПОЛНИТЕЛЬНОЕ ПО ДЛЯ ПРОЕКТА СОМ.ТС-60-ЕТ (ЕГИПЕТ)")












        # self.pushButton.clicked.connect(self.on_button)

    # def on_button(self):
    #     self.label.setText("dfdfg")
    #     print("dfggfdbgfd")