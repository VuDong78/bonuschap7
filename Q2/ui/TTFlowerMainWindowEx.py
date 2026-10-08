


from review_midterm.midterm1.Q2.ui.Ui_TTFlowerMainWindow import Ui_MainWindow as Ui_TTFlowerMainWindow
from review_midterm.midterm1.Q2.libs.ultil import calculate_flower_price, get_cumulative_statistics
from PyQt6.QtWidgets import QMessageBox


class TTFlowerMainWindowEx(Ui_TTFlowerMainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        # Initialize cumulative statistics
        self.cumulative_stats = get_cumulative_statistics()
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonCalc.clicked.connect(self.processTTFlower)

    def processTTFlower(self):
        try:
            da_lat_qty = int(self.lineEditDaLatQty.text())
            sapa_qty = int(self.lineEditSapaQty.text())
        except ValueError:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText("Vui lòng nhập số hợp lệ")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
            ret = msgBox.exec()
            return
        da_lat_revenue, sapa_revenue = calculate_flower_price(da_lat_qty, sapa_qty)
        self.cumulative_stats = get_cumulative_statistics(da_lat_stat_qty=da_lat_qty, sapa_stat_qty=sapa_qty, da_lat_stat_value=da_lat_revenue, sapa_stat_value=sapa_revenue, previous_stats=self.cumulative_stats)

        self.lineEditStatDaLatQty.setText(str(self.cumulative_stats['da_lat_stat_qty']))
        self.lineEditStatDaLatVal.setText(str(self.cumulative_stats['da_lat_stat_value']))
        self.lineEditStatSapaQty.setText(str(self.cumulative_stats['sapa_stat_qty']))
        self.lineEditStatSapaVal.setText(str(self.cumulative_stats['sapa_stat_value']))
        self.lineEditTotalRevenue.setText(str(self.cumulative_stats['total_revenue']))