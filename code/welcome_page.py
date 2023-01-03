import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QCursor, QFontDatabase, QFont
import subprocess
import os


class Welcome_page(QMainWindow):
    def __init__(self):
        super().__init__()
        self.font = None
        self.pushButton5 = None
        self.pushButton4 = None
        self.pushButton3 = None
        self.pushButton2 = None
        self.label = None
        self.pushButton6 = None
        self.pushButton = None
        self.pushButton1 = None
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedWidth(800)
        self.setFixedHeight(800)
        self.pushButton = QPushButton('', self)
        self.pushButton.resize(80, 80)
        self.pushButton.move(20, 20)
        self.pushButton.setIcon(QIcon('../data/Шестеренка.svg'))
        self.pushButton.setIconSize(QSize(50, 50))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.clicked.connect(self.settings)
        self.pushButton.setStyleSheet('border: 0px;')
        self.pushButton1 = QPushButton('', self)
        self.pushButton1.resize(80, 80)
        self.pushButton1.move(700, 20)
        self.pushButton1.setIcon(QIcon('../data/Выход.svg'))
        self.pushButton1.setIconSize(QSize(50, 50))
        self.pushButton1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton1.clicked.connect(self.termination)
        self.pushButton1.setStyleSheet('border: 0px;')
        self.pushButton5 = QPushButton('', self)
        self.pushButton5.move(00, 700)
        self.pushButton5.setIcon(QIcon('../data/Информация.svg'))
        self.pushButton5.clicked.connect(self.info)
        self.pushButton5.setStyleSheet('border: 0px')
        self.pushButton5.setIconSize(QSize(80, 80))
        self.pushButton5.adjustSize()
        id1 = QFontDatabase.addApplicationFont('../data/Шрифт.TTF')
        families = QFontDatabase.applicationFontFamilies(id1)
        self.label = QLabel('MAZE', self)
        self.label.setFont(QFont(families[0], 98))
        self.label.move(205, 100)
        self.label.adjustSize()
        id2 = QFontDatabase.addApplicationFont('../data/Шрифт2.ttf')
        families = QFontDatabase.applicationFontFamilies(id2)
        self.pushButton2 = QPushButton('LEVEL I', self)
        self.pushButton2.resize(350, 60)
        self.pushButton2.setFont(QFont(families[0], 30))
        self.pushButton2.setStyleSheet('border: 1px solid black; border-radius: 5px; text-align: center;')
        self.pushButton2.move(225, 400)
        self.pushButton3 = QPushButton('LEVEL II', self)
        self.pushButton3.resize(350, 60)
        self.pushButton3.setFont(QFont(families[0], 30))
        self.pushButton3.setStyleSheet('border: 1px solid black; border-radius: 5px;')
        self.pushButton3.move(225, 470)
        self.pushButton4 = QPushButton('LEVEL III', self)
        self.pushButton4.resize(350, 60)
        self.pushButton4.setFont(QFont(families[0], 30))
        self.pushButton4.setStyleSheet('border: 1px solid black; border-radius: 5px;')
        self.pushButton4.move(225, 540)
        self.font = self.pushButton2.font()
        self.font.setBold(True)
        self.pushButton2.setFont(self.font)
        self.pushButton3.setFont(self.font)
        self.pushButton4.setFont(self.font)
        self.pushButton2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

    def settings(self):
        pass

    def termination(self):
        try:
            command = 'taskkill /IM Python.exe'
            os.system(command)
        except Exception:
            pass
        self.close()

    def info(self):
        subprocess.Popen(['python', 'information.py'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Welcome_page()
    ex.show()
    sys.exit(app.exec())
