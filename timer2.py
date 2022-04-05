# -*- coding: utf-8 -*-
"""
Created on Sat May  8 08:52:55 2021

@author: 1
"""

import sys
#import time
import winsound
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QApplication, \
    QLCDNumber, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets

lcd_value = 5
duration = 5


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
#        self.lcd_value_len = 80
        self.time_begin = 0
        self.time_end = 0
        self.time_to_question = 60    # 4 часа на 150 вопросов, значит 96 секунд на вопрос
        self.time_total = 4*60*60

        self.label_time_question = QtWidgets.QLabel()
        self.label_time_question.setGeometry(QtCore.QRect(222, 195, 299, 46))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_time_question.setFont(font)
        self.label_time_question.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_question.setObjectName("label")
        self.label_time_question.setText('60 секунд')  # +++
        self.label_time_question.adjustSize()

        self.label_time_remain = QtWidgets.QLabel()
        self.label_time_remain.setGeometry(QtCore.QRect(222, 195, 299, 46))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_time_remain.setFont(font)
        self.label_time_remain.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_remain.setObjectName("label")
        self.label_time_remain.setText('4 часа')  # +++
        self.label_time_remain.adjustSize()

        self.start_btn = QPushButton('Start', self)
        self.start_btn.clicked.connect(self.start_btn_clicked)
        self.toggle_btns()

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_btn)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_time_question)
        vbox.addWidget(self.label_time_remain)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Timer PyQt5')
        self.resize(400, 300)

    def toggle_btns(self, value=True):
        self.start_btn.setEnabled(value)

    def start_btn_clicked(self):
        # Отключаем слайдер и кнопку старта
        self.toggle_btns(False)
        # запускаем отсчет
#        self.time_begin_total = time.time()
#        self.time_end_total = self.time_begin + self.time_total
        self.lcd_value_len  = self.time_total
        self.time_question = self.time_to_question
        self.tick_timer()

    def tick_timer(self):
#        if self.time_question > 0:
#            # Устанавливаем значение на 1 меньше
#            self.time_question -= 1
#            self.lcd_value_len -= 1
#        else:
#            # Значение дисплея стало 0
#            # Включаем элементы интерфейса обратно
#            self.time_question = self.time_to_question

        if self.lcd_value_len > 0:
            # Устанавливаем значение на 1 меньше
            if self.time_question > 0:
                # Устанавливаем значение на 1 меньше
                self.time_question -= 1
                self.lcd_value_len -= 1
                sec = int(self.lcd_value_len)
                h = sec//3600
                m = (sec - h*3600)//60
                s = sec % 60
                self.label_time_question.setText('осталось на вопрос: ' + str(self.time_question))
                self.label_time_remain.setText('осталось всего: ' + str(h) + ':'+ str(m) + ':' + str(s))  # +++
    
                # Засекаем таймер - значение в милисекундах
                # метод singleShot создает поток в фоне, отменить его нельзя
                if self.time_question == 0:
                    winsound.Beep(2500, 500)
                    QTimer().singleShot(500, self.tick_timer)
                else:
                    QTimer().singleShot(1000, self.tick_timer)
            else:
                # Значение дисплея стало 0
                # Включаем элементы интерфейса обратно
                self.time_question = self.time_to_question
                QTimer().singleShot(0, self.tick_timer)
        else:
            # Значение дисплея стало 0
            # Включаем элементы интерфейса обратно
            self.lcd_value_len = self.time_total
#            self.lcd_value_len = 5
            self.toggle_btns()
            # Устанавливаем на дисплей выбранную на слайдере настройку
#            self.lcd.display(lcd_value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())