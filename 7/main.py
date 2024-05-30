
import megagay
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel,QLineEdit, QGridLayout
import sys

def edited():
    if status.text() == "Отсутствует":
        return
    try:
        int(line.text())
    except:
        summ.setText("_")
        return
    changed()

def change1():
    status.setText("Пиджак")
    edited()

def change2():
    status.setText("Брюки")
    edited()
    
def change3():
    status.setText("Костюм-тройка")
    edited()


def save():
    if status.text() == "Отсутствует":
        return
    try:
        num=int(line.text())
    except:
        summ.setText("_")
        return
    z=status.text()
    tosave=megagay.classes[z]().__dict__
    tosave["type"]=z
    tosave["quan"]=num
    tosave["price"]=summ.text()
    megagay.save(tosave)
    
def changed():
    num=int(line.text())
    z=status.text()
    obj=megagay.classes[z]().calc()*num
    summ.setText(str(obj))

app = QApplication(sys.argv)

window = QWidget()
grid=QGridLayout()

button1=QPushButton("Пиджак")
button1.clicked.connect(change1)
button2=QPushButton("Брюки")
button2.clicked.connect(change2)
button3=QPushButton("Костюм-тройка")
button3.clicked.connect(change3)
buttonSave=QPushButton("Сохранить результат")
buttonSave.clicked.connect(save)
status=QLabel("Отсутствует")
line=QLineEdit()
line.textChanged.connect(edited)
summ=QLabel("_")
buttons = ["Выберите предмет", "", "",
    button1, "Выбранный предмет:", status,
    button2, "Введите количество", line,
    button3, "Итог", summ,
    "", "", "",
    "", "", buttonSave]
for i in range(0, len(buttons)):
    row = i / 3
    col = i % 3
    if isinstance(buttons[i],str):
        grid.addWidget(QLabel(buttons[i]), row, col)
    else:
        grid.addWidget(buttons[i], row, col)


window.setLayout(grid)


window.resize(300,300)


window.show()
sys.exit(app.exec())

