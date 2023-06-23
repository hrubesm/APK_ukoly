from PyQt6.QtWidgets import *

class SettingDialog(QDialog):
    def __init__(self, min, max, step):

        # Initialization
        super().__init__(parent=None)
        self.setWindowTitle("Parameters of contour lines")
        self.__min = QLineEdit(self)
        self.__max = QLineEdit(self)
        self.__step = QLineEdit(self)


        # Text of input lines
        self.__min.setText(str(min))
        self.__max.setText(str(max))
        self.__step.setText(str(step))


        # Button boxes
        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        # Layout
        layout = QFormLayout(self)
        layout.addRow("Set Minimum", self.__min)
        layout.addRow("Set Maximum", self.__max)
        layout.addRow("Set Step", self.__step)
        layout.addWidget(buttonBox)

    # Return of parameters
    def getInputs(self):
        return (self.__min.text(), self.__max.text(), self.__step.text())
