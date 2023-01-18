import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import Qt, QSize, QUrl
from PyQt5.QtGui import QIcon, QCursor, QFontDatabase, QFont
import pygame
import subprocess
import os
import sqlite3


class Welcome_page(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pushButton8 = None
        self.families = None
        self.result = None
        self.filename = None
        self.player = None
        self.font = None
        self.pushButton5 = None
        self.pushButton4 = None
        self.pushButton3 = None
        self.pushButton2 = None
        self.label = None
        self.pushButton = None
        self.pushButton1 = None
        self.label1 = QLabel('', self)
        self.flag = 0
        self.initUI()
        self.level_check()
        pygame.init()
        self.player = pygame.mixer.Sound('../data/music.wav')
        self.player.play()
        self.level_check()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedWidth(800)
        self.setFixedHeight(800)
        self.pushButton = QPushButton('', self)
        self.pushButton.resize(80, 80)
        self.pushButton.move(20, 20)
        self.pushButton.setIcon(QIcon('../data/звук_on.svg'))
        self.pushButton.setIconSize(QSize(50, 50))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.clicked.connect(self.musicPlayer)
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
        self.families = QFontDatabase.applicationFontFamilies(id2)
        self.pushButton2 = QPushButton('LEVEL I', self)
        self.pushButton2.resize(350, 60)
        self.pushButton2.setFont(QFont(self.families[0], 30))
        self.pushButton2.setStyleSheet('border: 1px solid black; border-radius: 5px; text-align: center;')
        self.pushButton2.move(225, 400)
        self.pushButton2.clicked.connect(self.level_1)
        self.pushButton3 = QPushButton('LEVEL II', self)
        self.pushButton3.resize(350, 60)
        self.pushButton3.setFont(QFont(self.families[0], 30))
        self.pushButton3.move(225, 470)
        self.pushButton3.setStyleSheet('border: 1px solid black; border-radius: 5px; color: black;')
        self.pushButton3.clicked.connect(self.level_2)
        self.pushButton4 = QPushButton('LEVEL III', self)
        self.pushButton4.resize(350, 60)
        self.pushButton4.setFont(QFont(self.families[0], 30))
        self.pushButton4.move(225, 540)
        self.pushButton4.setStyleSheet('border: 1px solid black; border-radius: 5px; color: black;')
        self.pushButton4.clicked.connect(self.level_3)
        self.pushButton8 = QPushButton('', self)
        self.pushButton8.resize(80, 80)
        self.pushButton8.move(700, 700)
        self.pushButton8.setIcon(QIcon('../data/reload.svg'))
        self.pushButton8.setIconSize(QSize(50, 50))
        self.pushButton8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton8.setStyleSheet('border: 0px;')
        self.pushButton8.clicked.connect(self.level_check)
        self.font = self.pushButton2.font()
        self.font.setBold(True)
        self.pushButton2.setFont(self.font)
        self.pushButton3.setFont(self.font)
        self.pushButton4.setFont(self.font)
        self.pushButton2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

    def level_1(self):
        self.flag = 1
        self.musicPlayer()
        subprocess.Popen(['python', 'level_1.py'])

    def level_2(self):
        self.flag = 1
        self.musicPlayer()
        subprocess.Popen(['python', 'level_2.py'])

    def level_3(self):
        self.flag = 1
        self.musicPlayer()
        subprocess.Popen(['python', 'level_3.py'])

    def musicPlayer(self):
        if self.flag == 1:
            self.flag = 0
            self.player.set_volume(0)
            self.pushButton.setIcon(QIcon('../data/звук_off.svg'))
        else:
            self.flag = 1
            self.player.set_volume(0.1)
            self.pushButton.setIcon(QIcon('../data/звук_on.svg'))

    def level_check(self):
        con = sqlite3.connect('../database/Coins.db')
        cur = con.cursor()
        self.result = [i[0] for i in cur.execute('SELECT value FROM levels').fetchall()]
        if self.result[0] == 0:
            self.pushButton3.setEnabled(False)
        else:
            self.pushButton3.setEnabled(True)
            self.pushButton3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        if self.result[1] == 0:
            self.pushButton4.setEnabled(False)
        else:
            self.pushButton4.setEnabled(True)
            self.pushButton4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

    @staticmethod
    def settings():
        subprocess.Popen(['python', 'settings.py'])

    def termination(self):
        try:
            command = 'taskkill /IM Python.exe'
            os.system(command)
        except Exception:
            pass
        self.close()

    @staticmethod
    def info():
        subprocess.Popen(['python', 'information.py'])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Welcome_page()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
