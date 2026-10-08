import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from review_midterm.midterm1.Q2.ui.TTFlowerMainWindowEx import TTFlowerMainWindowEx

app = QApplication(sys.argv)
myui = TTFlowerMainWindowEx()
myui.setupUi(QMainWindow())
myui.showWindow()
app.exec()