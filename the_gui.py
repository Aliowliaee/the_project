from PyQt6 import QtCore, QtGui, QtWidgets
from the_logic import previous_vote, new_vote


class Ui_ProjectWindow(object):
    """the layout for the voting window is created."""
    def setupUi(self, ProjectWindow):
        """All the buttons, labels, and layout will be built."""
        ProjectWindow.setObjectName("ProjectWindow")
        ProjectWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=ProjectWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.app_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.app_label.setGeometry(QtCore.QRect(170, 10, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.app_label.setFont(font)
        self.app_label.setObjectName("app_label")
        self.id_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(90, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        self.id_label.setFont(font)
        self.id_label.setObjectName("id_label")
        self.id_input = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.id_input.setGeometry(QtCore.QRect(160, 90, 281, 41))
        self.id_input.setObjectName("id_input")
        self.candidate_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.candidate_label.setGeometry(QtCore.QRect(210, 150, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.candidate_label.setFont(font)
        self.candidate_label.setObjectName("candidate_label")
        self.biancaButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.biancaButton.setGeometry(QtCore.QRect(220, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.biancaButton.setFont(font)
        self.biancaButton.setObjectName("biancaButton")
        self.edwardButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.edwardButton.setGeometry(QtCore.QRect(220, 260, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.edwardButton.setFont(font)
        self.edwardButton.setObjectName("edwardButton")
        self.feliciaButton = QtWidgets.QRadioButton(parent=self.centralwidget, clicked=lambda: self.submit()) """AI-assisted"""
        self.feliciaButton.setGeometry(QtCore.QRect(220, 310, 89, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.feliciaButton.setFont(font)
        self.feliciaButton.setObjectName("feliciaButton")
        self.submitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(170, 360, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.submitButton.clicked.connect(self.submit)
        ProjectWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ProjectWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        ProjectWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ProjectWindow)
        self.statusbar.setObjectName("statusbar")
        ProjectWindow.setStatusBar(self.statusbar)
        
        self.the_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.the_label.setGeometry(QtCore.QRect(300, 560, 200, 30))
        self.the_label.setWordWrap(True)
        self.the_label.setText("Already Voted")
        self.the_label.setStyleSheet("color: red") """AI-assisted"""
        self.the_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.retranslateUi(ProjectWindow)
        QtCore.QMetaObject.connectSlotsByName(ProjectWindow)

    def retranslateUi(self, ProjectWindow):
        """The text for the buttons and labels will get set."""
        _translate = QtCore.QCoreApplication.translate
        ProjectWindow.setWindowTitle(_translate("ProjectWindow", "MainWindow"))
        self.app_label.setText(_translate("ProjectWindow", "VOTING APPLICATION"))
        self.id_label.setText(_translate("ProjectWindow", "ID"))
        self.candidate_label.setText(_translate("ProjectWindow", "CANDIDATES"))
        self.biancaButton.setText(_translate("ProjectWindow", "BIANCA"))
        self.edwardButton.setText(_translate("ProjectWindow", "EDWARD"))
        self.feliciaButton.setText(_translate("ProjectWindow", "FELICIA"))
        self.submitButton.setText(_translate("ProjectWindow", "SUBMIT VOTE"))
      
    def submit(self):
        """

        The vote submission process will be handled.
        
        The function checks the input, prevents repeat votes, and shows messages on screen.
        
        """
        try:
            id_val = int(self.id_input.toPlainText().strip())
            the_vote = None
            if self.biancaButton.isChecked():
                the_vote = 'Bianca'
            elif self.edwardButton.isChecked():
                the_vote = 'Edward'
            elif self.feliciaButton.isChecked():
                the_vote = 'Felicia'
                
            if the_vote is None:
                self.the_label.setText("Please select a candidate.")
                self.the_label.setStyleSheet("color: red") """AI-assisted"""
                return
            
            if previous_vote(id_val):
                self.the_label.setText(previous_vote(id_val))
                self.the_label.setStyleSheet("color: red") """AI-assisted"""
                return
            
            vote_message = new_vote(id_val, the_vote)
            self.the_label.setText(vote_message)
            self.the_label.setStyleSheet("color: blue") """AI-assisted"""
        
        except ValueError:
            self.the_label.setText("Enter a correct numeric value.")
            self.the_label.setStyleSheet("color: red") """AI-assisted"""
            
    def clear(self):
        """The function clears the inputs and resets the label to default state."""
        self.id_input.clear()
        self.biancaButton.setChecked(False)
        self.edwardButton.setChecked(False)
        self.feliciaButton.setChecked(False)
        self.the_label.setText("Already Voted")
        self.the_label.setStyleSheet("color: red") """AI-assisted"""


