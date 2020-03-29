
import sys
from PyQt4 import QtGui, QtCore

import os
stream = os.popen('lsb_release -a')
output = stream.read()

class Window(QtGui.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("PyQt TUTS!")
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
		self.home()
		self.setStyleSheet("background-color: red")

	def home(self):
		btn = QtGui.QPushButton("OS Information", self)
		btn.clicked.connect(self.close_application)
		btn.resize(160,100)
		btn.move(160,100)
		self.show()

	def close_application(self):
		print(output)
		sys.exit()

def run():

	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()
