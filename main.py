import sys
from PyQt5 import QtWidgets
import general

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = general.ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()