import sys

from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QComboBox, QLineEdit


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        self.distance_label = QLabel("Distance")
        self.distance_text_edit = QLineEdit()
        self.units_combo_box = QComboBox()
        self.units_combo_box.addItems(["Imperial (miles)", "Metric (kms)"])

        self.time_label = QLabel("Time (hours)")
        self.time_text_edit = QLineEdit()

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_speed)

        self.output_label = QLabel("")

        grid.addWidget(self.distance_label, 0, 0)
        grid.addWidget(self.distance_text_edit, 0, 1)
        grid.addWidget(self.units_combo_box, 0, 2)
        grid.addWidget(self.time_label, 1, 0)
        grid.addWidget(self.time_text_edit, 1, 1)
        grid.addWidget(self.calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = self.distance_text_edit.text()
        time = self.time_text_edit.text()
        speed = float(distance)/float(time)
        if self.units_combo_box.currentText() == "Imperial (miles)":
            units = "mpr"
        else:
            units = "km/h"
        self.output_label.setText(f"Average speed: {speed} {units}")


app = QApplication(sys.argv)
age_calculator = SpeedCalculator()
age_calculator.show()
app.exit(app.exec())