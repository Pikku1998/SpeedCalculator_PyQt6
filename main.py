from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        # Create type of layout
        grid = QGridLayout()

        # Create Widgets (labels, line_edits and push_buttons)
        distance_label = QLabel('Distance: ')
        distance_line_edit = QLineEdit()

        time_label = QLabel('Time: ')
        time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Speed")
        output_label = QLabel("")

        # Add Widgets to grid layout
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(output_label, 3, 0, 1, 2)

        # Set Layout to grid
        self.setLayout(grid)


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
