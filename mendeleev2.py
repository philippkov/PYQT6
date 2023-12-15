from PyQt6 import QtWidgets
from mendeleev import Ui_MainWindow
import csv

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(53)
        self.ui.pushButton.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.ui.textEdit.clear()
        self.ui.textEdit.clear()
        with open('periodictable.csv') as file:
            reader = csv.reader(file)
            element = list(reader)
# Загрузка данных из csv-файла и представлена их в виде словаря
        columns = ['Atomic Number', 'Symbol', 'Element', 'Origin of name', 'Group', 'Period', 'Atomic weight',
                   'Density', 'Melting point', 'Boiling point', 'Specific heat capacity', 'Electronegativity',
                   'Abundance in earths crust']
        element_data = {}
        for i in element:
            element = {'Atomic Number': i[0], 'Symbol': i[1], 'Element': i[2], 'Origin of name': i[3], 'Group': i[4],
                       'Period': i[5], 'Atomic weight': i[6], 'Density': i[7], 'Melting point': i[8], 'Boiling point': i[9],
                       'Specific heat capacity': i[10], 'Electronegativity': i[11], 'Abundance in earths crust': i[12]}
#Использование символа элемента в качестве ключа
            element_data[i[0]] = element
            element_data[i[1]] = element
#Получение запроса пользователя
        user_input = self.ui.lineEdit.text()
        self.ui.lineEdit.clear()
#Вывод информации об элементе при совпадении запроса
        if user_input in element_data:
            for column in columns:
                true = column.rjust(max(map(len, columns)))
                self.ui.textEdit.append(true + ': ' + element_data[user_input][column])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.resize(1050, 800)
    window.show()
    sys.exit(app.exec())
