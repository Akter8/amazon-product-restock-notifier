import os
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
                             QPushButton, QWidget)
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class App(QWidget):

    def __init__(self, x, y, x_end, y_end, file):
        super().__init__()
        self.title = 'View and Set Inputs'
        self.left = x
        self.top = y
        self.right = y_end
        self.bottom = x_end
        self.file = file
        self.configurePalette()
        self.edit = True
        self.initUI()

    def configurePalette(self):
        self.darkPalette = QPalette
        # self.darkPalette.setColor(QPalette::base)

    def initUI(self):
        layout = self.createFormGroupBox()
        self.setLayout(layout)

        self.saveButton = QPushButton('Save and close', self)
        self.saveButton.setToolTip('Click to save your details')
        self.saveButton.move(100, self.bottom - 50)
        self.saveButton.setEnabled(not self.edit)
        self.saveButton.clicked.connect(self.saveButtonClicked)

        self.editButton = QPushButton('Edit values', self)
        self.editButton.setToolTip('Edit your details')
        self.editButton.move(300, self.bottom - 50)
        self.editButton.setEnabled(self.edit)
        self.editButton.clicked.connect(self.editButtonClicked)

        self.cancelButton = QPushButton('Cancel', self)
        self.cancelButton.setToolTip('Edit your details')
        self.cancelButton.move(500, self.bottom - 50)
        self.cancelButton.clicked.connect(
            QtCore.QCoreApplication.instance().quit)

        self.startButton = QPushButton('Save and Start', self)
        self.startButton.setToolTip('Run the script')
        self.startButton.move(700, self.bottom - 50)
        self.startButton.setEnabled(self.edit)
        self.startButton.clicked.connect(self.startButtonClicked)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.right, self.bottom)
        self.show()

    def editButtonClicked(self):
        self.edit = not self.edit
        self.saveButton.setEnabled(not self.edit)
        self.startButton.setEnabled(self.edit)
        self.txt_toEmail.setReadOnly(self.edit)
        self.txt_url.setReadOnly(self.edit)
        self.txt_agent.setReadOnly(self.edit)
        self.txt_pass.setReadOnly(self.edit)
        self.txt_email.setReadOnly(self.edit)
        self.txt_hours.setReadOnly(self.edit)
        self.txt_mins.setReadOnly(self.edit)

    def saveButtonClicked(self):
        with open(self.file, 'w') as f:
            f.write('url='+self.txt_url.text()+'\n')
            f.write('login='+self.txt_email.text()+'\n')
            f.write('pass='+self.txt_pass.text()+'\n')
            f.write('user_agent='+self.txt_agent.text()+'\n')
            f.write('target='+self.txt_toEmail.text()+'\n')
            f.write('freqh='+self.txt_hours.text()+'\n')
            f.write('freqm='+self.txt_mins.text()+'\n')
            f.write("LeaveThis=AsIs")
        f.close()
        sys.exit()

    def startButtonClicked(self):
        with open(self.file, 'w') as f:
            f.write('url='+self.txt_url.text()+'\n')
            f.write('login='+self.txt_email.text()+'\n')
            f.write('pass='+self.txt_pass.text()+'\n')
            f.write('user_agent='+self.txt_agent.text()+'\n')
            f.write('target='+self.txt_toEmail.text()+'\n')
            f.write('freqh='+self.txt_hours.text()+'\n')
            f.write('freqm='+self.txt_mins.text()+'\n')
            f.write("LeaveThis=AsIs")
        f.close()
        os.system(
            'C:/Python37/pythonw.exe "d:/Python Scripts/Amazon Restock Notification/amazonRestockedNotification.py"'
            )
        sys.exit()

    def createFormGroupBox(self):
        layout = QGridLayout()
        layout.setSpacing(1)
        self.fileOpen()

        self.label_url = QLabel('URL:')
        self.txt_url = QLineEdit()
        self.txt_url.setPlaceholderText("Enter URL")
        self.txt_url.setText(self.data['url'])
        self.txt_url.setReadOnly(self.edit)
        layout.addWidget(self.label_url, 1, 0)
        layout.addWidget(self.txt_url, 1, 1)

        self.label_agent = QLabel('User Agent:')
        self.txt_agent = QLineEdit()
        self.txt_agent.setPlaceholderText("Enter User Agent")
        self.txt_agent.setText(self.data['user_agent'])
        self.txt_agent.setReadOnly(self.edit)
        layout.addWidget(self.label_agent, 2, 0)
        layout.addWidget(self.txt_agent, 2, 1)

        self.label_email = QLabel('From Email:')
        self.txt_email = QLineEdit()
        self.txt_email.setPlaceholderText("Enter From-Email")
        self.txt_email.setText(self.data['login'])
        self.txt_email.setReadOnly(self.edit)
        layout.addWidget(self.label_email, 3, 0)
        layout.addWidget(self.txt_email, 3, 1)

        self.label_pass = QLabel('Password:')
        self.txt_pass = QLineEdit()
        self.txt_pass.setPlaceholderText("Enter Password")
        self.txt_pass.setText(self.data['pass'])
        self.txt_pass.setReadOnly(self.edit)
        layout.addWidget(self.label_pass, 4, 0)
        layout.addWidget(self.txt_pass, 4, 1)

        self.label_toEmail = QLabel('Target Email:')
        self.txt_toEmail = QLineEdit()
        self.txt_toEmail.setPlaceholderText("Enter Target-Email")
        self.txt_toEmail.setText(self.data['target'])
        self.txt_toEmail.setReadOnly(self.edit)
        # regex = QRegExp('/\S+@\S+\.\S+/')
        # txt_toEmail_validator = QRegExpValidator(regex, self.txt_toEmail)
        # self.txt_toEmail.setValidator(txt_toEmail_validator)
        layout.addWidget(self.label_toEmail, 5, 0)
        layout.addWidget(self.txt_toEmail, 5, 1)

        self.label_hours = QLabel('Freq Hours:')
        self.txt_hours = QLineEdit()
        self.txt_hours.setPlaceholderText("Enter Frequency Hours")
        self.txt_hours.setText(self.data['freqh'])
        self.txt_hours.setReadOnly(self.edit)
        self.label_mins = QLabel('Minutes:')
        self.txt_mins = QLineEdit()
        self.txt_mins.setPlaceholderText("Enter Frequency in Minutes")
        self.txt_mins.setText(self.data['freqm'])
        self.txt_mins.setReadOnly(self.edit)
        regex = QRegExp('[0-9]+')
        txt_hours_validator = QRegExpValidator(regex, self.txt_hours)
        self.txt_hours.setValidator(txt_hours_validator)
        txt_mins_validator = QRegExpValidator(regex, self.txt_mins)
        self.txt_mins.setValidator(txt_mins_validator)
        layout.addWidget(self.label_hours, 6, 0)
        layout.addWidget(self.txt_hours, 6, 1)
        layout.addWidget(self.label_mins, 6, 2)
        layout.addWidget(self.txt_mins, 6, 3)

        return(layout)

    def fileOpen(self):
        data = {}
        file = open(self.file, "r")
        for f in file:
            [a, b] = f.split('=', 1)
            data[a] = b[:-1]
        self.data = data
        file.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    x = 100
    y = 100
    x_end = 700
    y_end = 900
    file = 'D:\\Python Scripts\\Amazon Restock Notification\\pars.txt'
    ex = App(x, y, x_end, y_end, file)
    sys.exit(app.exec_())
