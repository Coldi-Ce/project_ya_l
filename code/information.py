import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QCursor, QFontDatabase, QFont


class Information(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label6 = None
        self.label5 = QLabel('Как играть', self)
        self.label4 = QLabel('', self)
        self.label3 = QLabel('Особенности игры', self)
        self.label2 = QLabel('', self)
        self.label = QLabel('Об игре', self)
        self.pushButton = QPushButton('', self)
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet('border: 2px solid black')
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        self.pushButton.resize(40, 40)
        self.pushButton.move(450, 10)
        self.pushButton.setIcon(QIcon('../data/Крестик.svg'))
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.setStyleSheet('border: 0px;')
        self.pushButton.clicked.connect(self.termination)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        id1 = QFontDatabase.addApplicationFont('../data/Шрифт3.ttf')
        families = QFontDatabase.applicationFontFamilies(id1)
        self.label.setFont(QFont(families[0], 20))
        self.label.adjustSize()
        font = self.label.font()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet('border: 0px;')
        self.label.move(20, 20)
        self.label2.setText(
            'Заблудший путник попал в лабиринт, наполненный опасностями. На пути его '
            'поджидает множество монстров. Однако, путник не единственный человек в '
            'лабиринте. На своем пути ему попадется загадочный торговец, который '
            'поможет путнику, продавая оружие и одежду за монеты, которые тот найдет '
            'в лабиринте.'
        )
        self.label2.resize(460, 300)
        self.label2.setWordWrap(True)
        self.label2.setStyleSheet('border: 0px;')
        self.label2.setAlignment(Qt.AlignJustify)
        self.label2.setFont(QFont(families[0], 9))
        self.label2.move(20, 70)
        self.label3.setFont(QFont(families[0], 15))
        self.label3.setFont(font)
        self.label3.adjustSize()
        self.label3.setStyleSheet('border: 0px;')
        self.label3.move(20, 165)
        self.label4.setText(
            '- 3 уровня сложности\n'
            '- Разнообразные скины\n'
            '- Динамичная музыка\n'
            '- Телепорты\n'
            '- \n'
            '- \n'
            '- \n'
        )
        self.label4.setStyleSheet('border: 0px;')
        self.label4.setFont(QFont(families[0], 9))
        self.label4.move(20, 220)
        self.label4.adjustSize()
        self.label5.setStyleSheet('border: 0px;')
        self.label5.setFont(QFont(families[0], 20))
        self.label5.setFont(font)
        self.label5.adjustSize()
        self.label5.move(20, 360)
        self.label6 = QLabel('', self)
        self.label6.setText(
            'Пройдите 3 уровня лабиринта, убивая монстров, и доберитесь до выхода. '
            'По пути используйте телепоры, подбирайте монеты, за которые можно купить '
            'оружие или скин, а также сердца, за которые можно восстановить хп.'
        )
        self.label6.resize(460, 200)
        self.label6.setWordWrap(True)
        self.label6.setStyleSheet('border: 0px;')
        self.label6.setAlignment(Qt.AlignJustify)
        self.label6.setFont(QFont(families[0], 9))
        self.label6.move(20, 410)

    def termination(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Information()
    ex.show()
    sys.exit(app.exec())
