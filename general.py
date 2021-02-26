
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import interface  # Это наш конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        # self.pushButton.clicked.connect(self.on_button)

    # def on_button(self):
    #     self.label.setText("dfdfg")
    #     print("dfggfdbgfd")