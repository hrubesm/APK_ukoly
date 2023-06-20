from PyQt6.QtWidgets import *

class SettingDialog(QDialog):
    def __init__(self, dmin, aplha, beta, gamma, lam, iters):

        # Initialization
        super().__init__(parent=None)
        self.setWindowTitle("Parameters of energy splines")
        self.__dmin = QLineEdit(self)
        self.__alpha = QLineEdit(self)
        self.__beta = QLineEdit(self)
        self.__gamma = QLineEdit(self)
        self.__lam = QLineEdit(self)
        self.__iters = QLineEdit(self)

        # Text of input lines
        self.__dmin.setText(str(dmin))
        self.__alpha.setText(str(aplha))
        self.__beta.setText(str(beta))
        self.__gamma.setText(str(gamma))
        self.__lam.setText(str(lam))
        self.__iters.setText(str(iters))

        # Button boxes
        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        # Layout
        layout = QFormLayout(self)
        layout.addRow("Minimum distance", self.__dmin)
        layout.addRow("Alpha", self.__alpha)
        layout.addRow("Beta", self.__beta)
        layout.addRow("Gamma", self.__gamma)
        layout.addRow("Lambda", self.__lam)
        layout.addRow("Number of iterations", self.__iters)
        layout.addWidget(buttonBox)

    # Return of parameters
    def getInputs(self):
        return (self.__dmin.text(), self.__alpha.text(), self.__beta.text(), self.__gamma.text(), self.__lam.text(), self.__iters.text())
