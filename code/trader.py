import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QFont
import sqlite3


class Trader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label4 = QLabel('', self)
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        self.setStyleSheet('background-color: light grey;')
        self.pushButton = QPushButton('', self)
        self.pushButton.setIcon(QIcon('../data/Крестик.svg'))
        self.pushButton.setIconSize(QSize(20, 20))
        self.pushButton.adjustSize()
        self.pushButton.move(270, 0)
        self.pushButton.setStyleSheet('border: 0px;')
        self.pushButton.clicked.connect(self.terminate)
        self.pushButton1 = QPushButton('', self)
        self.pushButton1.setIcon(QIcon('../data/Оружие.svg'))
        self.pushButton1.setIconSize(QSize(60, 60))
        self.pushButton1.adjustSize()
        self.pushButton1.move(50, 70)
        self.pushButton1.clicked.connect(self.weapon)
        self.pushButton2 = QPushButton('', self)
        self.pushButton2.setIcon(QIcon('../data/new_skin.svg'))
        self.pushButton2.setIconSize(QSize(60, 60))
        self.pushButton2.adjustSize()
        self.pushButton2.move(180, 70)
        self.pushButton2.clicked.connect(self.skin)
        self.pushButton3 = QPushButton('', self)
        self.pushButton3.setIcon(QIcon('../data/heart.svg'))
        self.pushButton3.setIconSize(QSize(60, 60))
        self.pushButton3.adjustSize()
        self.pushButton3.move(50, 180)
        self.pushButton3.clicked.connect(self.hearts)
        self.con = sqlite3.connect('../database/Coins.db')
        self.cur = self.con.cursor()
        self.balance = self.cur.execute('SELECT Coins FROM coins').fetchone()[0]
        self.label = QLabel(f'Баланс: {self.balance}', self)
        self.label.setFont(QFont('Arial', 13))
        self.label.move(10, 10)
        self.pushButton4 = QPushButton('', self)
        self.pushButton4.setIcon(QIcon('../data/coin.svg'))
        self.pushButton4.setIconSize(QSize(30, 30))
        self.pushButton4.setStyleSheet('border: 0px;')
        self.pushButton4.adjustSize()
        self.pushButton4.move(85, 10)
        self.label1 = QLabel('3', self)
        self.label1.adjustSize()
        self.label1.move(75, 150)
        self.label2 = QLabel('4', self)
        self.label2.adjustSize()
        self.label2.move(200, 150)
        self.label3 = QLabel('1', self)
        self.label3.adjustSize()
        self.label3.move(75, 260)
        self.pushButton5 = QPushButton('', self)
        self.pushButton5.setIcon(QIcon('../data/coin.svg'))
        self.pushButton5.setIconSize(QSize(20, 20))
        self.pushButton5.setStyleSheet('border: 0px;')
        self.pushButton5.adjustSize()
        self.pushButton5.move(80, 147)
        self.pushButton6 = QPushButton('', self)
        self.pushButton6.setIcon(QIcon('../data/coin.svg'))
        self.pushButton6.setIconSize(QSize(20, 20))
        self.pushButton6.setStyleSheet('border: 0px;')
        self.pushButton6.adjustSize()
        self.pushButton6.move(205, 147)
        self.pushButton7 = QPushButton('', self)
        self.pushButton7.setIcon(QIcon('../data/coin.svg'))
        self.pushButton7.setIconSize(QSize(20, 20))
        self.pushButton7.setStyleSheet('border: 0px;')
        self.pushButton7.adjustSize()
        self.pushButton7.move(80, 257)
        self.label4.setFont((QFont('Arial', 10)))
        self.label4.move(150, 210)

    def weapon(self):
        if self.balance < 3:
            self.label4.setText('Недостаточно монет')
            self.label4.adjustSize()
        else:
            self.balance -= 3
            self.label.setText(f'Баланс: {self.balance}')
            self.cur.execute('UPDATE coins SET Coins = ?', (self.balance,))
            self.label4.setText('Нож успешно куплен')
            self.label4.adjustSize()
            self.cur.execute('UPDATE coins SET Weapon = 1')
            self.con.commit()

    def skin(self):
        if self.balance < 4:
            self.label4.setText('Недостаточно монет')
            self.label4.adjustSize()
        else:
            self.balance -= 4
            self.label.setText(f'Баланс: {self.balance}')
            self.cur.execute('UPDATE coins SET Coins = ?', (self.balance,))
            self.label4.setText('Скин успешно куплен')
            self.label4.adjustSize()
            self.cur.execute('UPDATE coins SET Skin = 1')
            self.con.commit()

    def hearts(self):
        self.con = sqlite3.connect('../database/Coins.db')
        self.cur = self.con.cursor()
        if self.cur.execute('SELECT Hearts FROM coins').fetchone()[0] == 2:
            self.label4.setText('Достигнуто макс.\n  число сердец')
            self.label4.adjustSize()
        else:
            if self.balance < 1:
                self.label4.setText('Недостаточно монет')
                self.label4.adjustSize()
            else:
                self.balance -= 1
                self.label.setText(f'Баланс: {self.balance}')
                self.cur.execute('UPDATE coins SET Coins = ?', (self.balance,))
                self.label4.setText('Сердце успешно\n  куплено')
                self.label4.adjustSize()
                self.cur.execute('UPDATE coins SET Hearts = 2')
                self.con.commit()

    def terminate(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Trader()
    ex.show()
    sys.exit(app.exec())