import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit
import pandas


class AnotherWindow(QWidget):
    def __init__(self, button, row, column):
        super().__init__()
        self.button = button
        self.row = row
        self.column = column
        self.setWindowTitle(button.text())
        self.button_text = button.text()
        self.setFixedSize(QSize(400, 100))
        self.layout = QHBoxLayout()
        self.txtbox = QLineEdit()
        self.txtbox.setText(self.button_text)
        self.layout.addWidget(self.txtbox)
        self.txtbox.returnPressed.connect(self.return_pressed)
        self.setLayout(self.layout)

    def return_pressed(self):
        text = self.txtbox.text()
        label = QLabel("Changes Saved!")
        self.layout.addWidget(label)
        self.txtbox.setText(text)
        self.button.setText(text)
        data.iloc[self.row, self.column] = text
        data1 = pandas.DataFrame(data)
        data1.to_csv("./data/Timetable.csv", index=False)







class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setWindowTitle("Timetable")
        self.setFixedSize(QSize(1800, 600))
        layout = QGridLayout()
        layout.setSpacing(40)
        self.setStyleSheet("background-color: black; color:white;")
        layout.addWidget()
        for i in range(0, 9):
            label1 = QPushButton(data.axes[1][i])
            font1 = label1.font()
            font1.setPointSize(12)
            label1.setFont(font1)
            label1.setEnabled(False)
            layout.addWidget(label1, 0, i)

        for i in range(0, 6):
            for j in range(0, 9):
                label2 = QPushButton(str(data.iloc[i, j]))
                font2 = label2.font()
                font2.setPointSize(12)
                label2.setFont(font2)
                label2.clicked.connect(lambda checked, b=label2, r=i, c=j: self.button_clicked(b, r, c))
                layout.addWidget(label2, i+1, j)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def button_clicked(self, buttonx, row, column):
        self.w = AnotherWindow(buttonx, row, column)
        self.w.show()


app = QApplication(sys.argv)


data = pandas.read_csv("./data/Timetable.csv")










window = MainWindow()
window.show()
app.exec()

