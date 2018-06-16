import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.timer1 = QTimer()
        loadUi('uis/main.ui', self)

        # Присваиваем название форме
        self.setWindowTitle('Работа с таймерами Python')

        # Присваиваем изображение иконке фомры
        self.setWindowIcon(QtGui.QIcon('img/logo.png'))

        # Присваиваем переменной label изображение 
        # маршрушта автобуса в качестве заднего фона
        pixmap_background = QPixmap('img/background.png')
        self.background.setPixmap(pixmap_background)
        self.background.setScaledContents(True)

        # Присваиваем перменной label исходное изображение автобуса
        pixmap_bus = QPixmap('img/bus.png')
        self.bus.setPixmap(pixmap_bus)
        self.bus.setScaledContents(True)

        # Узнаем начальные позиции автобуса
        self.x = self.bus.pos().x()
        self.y = self.bus.pos().y()

        # При нажатии на кнопку активируется метод run()
        self.startButton.clicked.connect(self.run)

    def run(self):
        # Если значение в первом слайдере меньше чем во втором,
        # то делаем фон кнопки красной, иначе продолжаем программу
        if self.theFirstSlider.value() >= self.theSecondSlider.value():
            self.startButton.setStyleSheet("color: black;"
                                           "background-color: red;")
        else:
            # Делаем кнопку недоступной для нажатия
            self.startButton.setEnabled(False)

            # Присваиваем нормальный фон кнопке
            self.startButton.setStyleSheet("color: black;"
                                           "background-color: none;")

            # Начинаем движение с первой остановки
            if self.theFirstSlider.value() == 1:

                # Присваиваем автобусу координаты первой остановки
                self.x = 25
                self.y = 57

                # Устанавливаем присвоенные координаты и
                # при необходимости меняем размеры нашего автобуса (label)
                self.bus.setGeometry(self.x, self.y, 141, 71)

                # Присваиваем перменной label исходное изображение автобуса
                pixmap_bus = QPixmap('img/bus.png')
                self.bus.setPixmap(pixmap_bus)
                self.bus.setScaledContents(True)

                # Продолжаем движение по маршруту
                if self.theSecondSlider.value() >= 2:
                    self.timer1 = QTimer()
                    self.timer1.timeout.connect(self.from_the_first_to_the_second)
                    self.timer1.start(5)

            # Начинаем движение со второй остановки
            elif self.theFirstSlider.value() == 2:

                self.x = 315
                self.y = 27

                self.bus.setGeometry(self.x, self.y, 71, 141)

                pixmap_bus = QPixmap('img/bus1.png')
                self.bus.setPixmap(pixmap_bus)
                self.bus.setScaledContents(True)

                if self.theSecondSlider.value() >= 3:
                    self.timer2 = QTimer()
                    self.timer2.timeout.connect(self.from_the_second_to_the_third)
                    self.timer2.start(5)

            # Начинаем движение с третьей остановки
            elif self.theFirstSlider.value() == 3:

                self.x = 285
                self.y = 175

                self.bus.setGeometry(self.x, self.y, 141, 71)

                pixmap_bus = QPixmap('img/bus.png')
                self.bus.setPixmap(pixmap_bus)
                self.bus.setScaledContents(True)

                if self.theSecondSlider.value() >= 4:
                    self.timer3 = QTimer()
                    self.timer3.timeout.connect(self.from_the_third_to_the_fourth)
                    self.timer3.start(5)

            # Начинаем движение с четвертой остановки
            elif self.theFirstSlider.value() == 4:

                self.x = 560
                self.y = 175

                self.bus.setGeometry(self.x, self.y, 141, 71)

                pixmap_bus = QPixmap('img/bus.png')
                self.bus.setPixmap(pixmap_bus)
                self.bus.setScaledContents(True)

                if self.theSecondSlider.value() >= 5:
                    self.timer4_1 = QTimer()
                    self.timer4_1.timeout.connect(self.from_the_fourth_to_the_fifth_one)
                    self.timer4_1.start(5)

            # Начинаем движение с пятой остановки
            elif self.theFirstSlider.value() == 5:

                self.x = 631
                self.y = 392

                self.bus.setGeometry(self.x, self.y, 141, 71)

                pixmap_bus = QPixmap('img/bus2.png')
                self.bus.setPixmap(pixmap_bus)
                self.bus.setScaledContents(True)

                if self.theSecondSlider.value() >= 6:
                    self.timer5_1 = QTimer()
                    self.timer5_1.timeout.connect(self.from_the_fifth_to_the_sixth_one)
                    self.timer5_1.start(5)

            # Начинаем движение с шестой остановки
            elif self.theFirstSlider.value() == 6:

                self.x = 272
                self.y = 274

                self.bus.setGeometry(self.x, self.y, 141, 71)

                pixmap_bus = QPixmap('img/bus2.png')
                self.bus.setPixmap(pixmap_bus)
                self.bus.setScaledContents(True)

                if self.theSecondSlider.value() >= 7:
                    self.timer6 = QTimer()
                    self.timer6.timeout.connect(self.from_the_sixth_to_the_seventh)
                    self.timer6.start(5)

    # Движемся до второй остановки
    def from_the_first_to_the_second(self):
        # Делаем кнопку недоступной для нажатия
        self.startButton.setEnabled(False)

        # Продвигаем автобус вдоль абциссы
        self.x += 1
        self.bus.move(self.x, self.y)

        if self.x == 285:

            # Поправляем расположение автобуса
            self.x += 30
            self.y -= 30

            # Устанавливаем поправленное расположение и
            # меняем размеры автобуса (label)
            self.bus.setGeometry(self.x, self.y, 71, 141)

            # Устанавливаем автобусу новое изображение
            pixmap_bus = QPixmap('img/bus1.png')
            self.bus.setPixmap(pixmap_bus)
            self.bus.setScaledContents(True)

            # Останавливаем первый таймер
            self.timer1.stop()

            # Продолжаем движение, если второй
            # слайдер больше установленного значения
            if self.theSecondSlider.value() >= 3:
                self.timer2 = QTimer()
                self.timer2.timeout.connect(self.from_the_second_to_the_third)
                self.timer2.start(5)
            else:
                # Делаем кнопку активной
                self.startButton.setEnabled(True)

    # Движемся до третьей остановки
    def from_the_second_to_the_third(self):
        self.startButton.setEnabled(False)

        self.y += 1
        self.bus.move(self.x, self.y)

        if self.y == 140:

            self.x -= 30
            self.y += 35

            self.bus.setGeometry(self.x, self.y, 141, 71)

            pixmap_bus = QPixmap('img/bus.png')
            self.bus.setPixmap(pixmap_bus)
            self.bus.setScaledContents(True)

            self.timer2.stop()

            if self.theSecondSlider.value() >= 4:
                self.timer3 = QTimer()
                self.timer3.timeout.connect(self.from_the_third_to_the_fourth)
                self.timer3.start(5)
            else:
                self.startButton.setEnabled(True)

    # Движемся до четвертой остановки
    def from_the_third_to_the_fourth(self):
        self.startButton.setEnabled(False)

        self.x += 1
        self.bus.move(self.x, self.y)

        if self.x == 560:

            self.timer3.stop()

            if self.theSecondSlider.value() >= 5:
                self.timer4_1 = QTimer()
                self.timer4_1.timeout.connect(self.from_the_fourth_to_the_fifth_one)
                self.timer4_1.start(5)
            else:
                self.startButton.setEnabled(True)

    # Движемся до первой части пятой остановки
    def from_the_fourth_to_the_fifth_one(self):
        self.startButton.setEnabled(False)

        self.x += 1
        self.bus.move(self.x, self.y)

        if self.x == 645:

            self.x += 28
            self.y -= 30

            self.bus.setGeometry(self.x, self.y, 71, 141)

            pixmap_bus = QPixmap('img/bus1.png')
            self.bus.setPixmap(pixmap_bus)
            self.bus.setScaledContents(True)

            self.timer4_1.stop()

            self.timer4_2 = QTimer()
            self.timer4_2.timeout.connect(self.from_the_fourth_to_the_fifth_two)
            self.timer4_2.start(5)

    # Движемся до второй части пятой остановки
    def from_the_fourth_to_the_fifth_two(self):
        self.startButton.setEnabled(False)

        self.y += 1
        self.bus.move(self.x, self.y)

        if self.y == 355:

            self.x -= 42
            self.y += 37

            self.bus.setGeometry(self.x, self.y, 141, 71)

            pixmap_bus = QPixmap('img/bus2.png')
            self.bus.setPixmap(pixmap_bus)
            self.bus.setScaledContents(True)

            self.timer4_2.stop()

            if self.theSecondSlider.value() >= 6:
                self.timer5_1 = QTimer()
                self.timer5_1.timeout.connect(self.from_the_fifth_to_the_sixth_one)
                self.timer5_1.start(5)
            else:
                self.startButton.setEnabled(True)

    # Движемся до первой части шестой остановки
    def from_the_fifth_to_the_sixth_one(self):
        self.startButton.setEnabled(False)

        self.x -= 1
        self.bus.move(self.x, self.y)

        if self.x == 280:

            self.x += 36
            self.y -= 44

            self.bus.setGeometry(self.x, self.y, 71, 141)

            pixmap_bus = QPixmap('img/bus3.png')
            self.bus.setPixmap(pixmap_bus)
            self.bus.setScaledContents(True)

            self.timer5_1.stop()

            self.timer5_2 = QTimer()
            self.timer5_2.timeout.connect(self.from_the_fifth_to_the_sixth_two)
            self.timer5_2.start(5)

    # Движемся до второй части шестой остановки
    def from_the_fifth_to_the_sixth_two(self):
        self.startButton.setEnabled(False)

        self.y -= 1
        self.bus.move(self.x, self.y)

        if self.y == 232:

            self.x -= 44
            self.y += 42

            self.bus.setGeometry(self.x, self.y, 141, 71)

            pixmap_bus = QPixmap('img/bus2.png')
            self.bus.setPixmap(pixmap_bus)
            self.bus.setScaledContents(True)

            self.timer5_2.stop()

            if self.theSecondSlider.value() == 7:
                self.timer6 = QTimer()
                self.timer6.timeout.connect(self.from_the_sixth_to_the_seventh)
                self.timer6.start(5)
            else:
                self.startButton.setEnabled(True)

    # Движемся до седьмой остановки
    def from_the_sixth_to_the_seventh(self):
        self.startButton.setEnabled(False)

        self.x -= 1
        self.bus.move(self.x, self.y)

        if self.x == 10:

            self.timer6.stop()
            self.startButton.setEnabled(True)


# Отсюда начинается программа
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())