import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import random


class Game2(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.cube_label = QLabel("Введите количество кубиков:")
        layout.addWidget(self.cube_label)

        self.cube_input = QLineEdit()
        layout.addWidget(self.cube_input)

        self.br_label = QLabel("Введите количество бросков:")
        layout.addWidget(self.br_label)

        self.br_input = QLineEdit()
        layout.addWidget(self.br_input)

        self.calculate_button = QPushButton("Рассчитать")
        self.calculate_button.clicked.connect(self.calculate_probability)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_probability(self):
        cube_kol = int(self.cube_input.text())
        br_kol = int(self.br_input.text())
        result = []

        for i in range(br_kol):
            count = 0
            for j in range(cube_kol):
                num = random.randint(1, 6)
                count += num
            result.append(count)

        probability_text = ""
        for i in range(cube_kol, (cube_kol * 6) + 1):
            kol_sum = result.count(i)
            ver = (kol_sum / br_kol) * 100
            probability_text += f'Вероятность выпадения {i}: {ver:.2f}%\n'

        self.result_label.setText(probability_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Game2()
    window.setWindowTitle("Вероятность выпадения суммы очков на кубиках")
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec())
