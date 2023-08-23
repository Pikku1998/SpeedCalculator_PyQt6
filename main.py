from PyQt6.QtWidgets import QApplication, QWidget
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
