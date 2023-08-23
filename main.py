from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QComboBox, QPushButton
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle('Speed Calculator')

        # Create type of layout
        grid = QGridLayout()

        # Create Widgets (labels, line_edits and push_buttons)
        distance_label = QLabel('Distance: ')
        self.distance_line_edit = QLineEdit()

        self.distance_unit = QComboBox()
        self.distance_unit.addItems(['kilometers', 'miles'])

        time_label = QLabel('Time: ')
        self.time_line_edit = QLineEdit()

        button = QPushButton("Calculate Speed")
        button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        # Add Widgets to grid layout
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.distance_unit, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(button, 2, 1, 1, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        # Set Layout to grid
        self.setLayout(grid)

    def calculate_speed(self):
        self.output_label.setText('Clicked!')


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
