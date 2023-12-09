from PyQt6 import QtWidgets, QtCore
from random import randint

class Game1(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.count = 5
        self.live = QtWidgets.QLabel(f"Жизни: {self.count}")
        self.live.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.label1 = QtWidgets.QLabel("Угадай число от 1 до 100:")
        self.label1.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.gbutton = QtWidgets.QLineEdit(self)
        self.button_start = QtWidgets.QPushButton("тык")
        self.button_restart = QtWidgets.QPushButton("Еще раз")
        self.button_exit = QtWidgets.QPushButton("&Закрыть окно")
        self.number_user = randint(1, 100)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.live)
        self.vbox.addWidget(self.label1)
        self.vbox.addWidget(self.gbutton)
        self.vbox.addWidget(self.button_start)
        self.vbox.addWidget(self.button_restart)
        self.vbox.addWidget(self.button_exit)
        self.setLayout(self.vbox)
        self.button_start.clicked.connect(self.on_clicked)
        self.button_restart.clicked.connect(self.restart)
        self.button_exit.clicked.connect(QtWidgets.QApplication.instance().quit)

    def on_clicked(self):
        answer = int(self.gbutton.text())
        self.gbutton.clear()
        if answer == self.number_user:
            self.label1.setText("Поздравляю! Вы угадали число.")
        else:
            self.count -= 1
            self.live.setText(f"Жизни: {self.count}")
            if self.count == 0:
                self.label1.setText(f"Вы проиграли! Число было: {self.number_user}. У вас больше нет попыток.")
            else:
                if answer > self.number_user:
                    self.label1.setText("Неправильно! Попробуйте меньшее число!")
                if answer < self.number_user:
                    self.label1.setText("Неправильно! Попробуйте большее число!")

    def restart(self):
        self.count = 5
        self.live.setText(f"Жизни: {self.count}")
        self.label1.setText("Угадай число от 1 до 100:")
        self.number_user = randint(1, 100)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Game1()
    window.setWindowTitle("Угадай число!")
    window.resize(400, 200)
    window.show()
    sys.exit(app.exec())
