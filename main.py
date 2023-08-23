from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QComboBox, QPushButton
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        # self.resize(400, 300)
        self.setWindowTitle('Speed Calculator')

        # Create type of layout
        grid = QGridLayout()

        # Create Widgets (labels, line_edits and push_buttons)
        distance_label = QLabel('Distance(in km): ')
        self.distance_line_edit = QLineEdit()

        time_label = QLabel('Time(in hours): ')
        self.time_line_edit = QLineEdit()

        speed_units_label = QLabel('Speed in units: ')
        self.speed_unit = QComboBox()
        self.speed_unit.addItems(['km/h', 'mph'])

        calculate_button = QPushButton("Calculate Speed")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        # Add Widgets to grid layout
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(speed_units_label, 2, 0)
        grid.addWidget(self.speed_unit, 2, 1)
        grid.addWidget(calculate_button, 3, 0, 1, 1)
        grid.addWidget(self.output_label, 4, 0)

        # Set Layout to grid
        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())
        speed = distance/time

        if self.speed_unit.currentText() == 'km/h':
            speed = round(speed, 2)
            units = 'km/h'
        if self.speed_unit.currentText() == 'mph':
            speed = round(speed * 0.621371, 2)
            units = 'mph'
        self.output_label.setText(f"{speed} {units}")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
