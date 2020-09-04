# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dhont.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from dhont import calculate_mandates
from plot_dhont import DhontPlot


class Ui_MainWindow:

	text_edits_list = []
	text_edit_parties_list = []
	text_parties_names = []
	result_labels_list = []
	checkbox_list = []

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1366, 768)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		self.create_text_edit()


		"""
		WHITE votes
		"""
		self.textLine_White_votes = QtWidgets.QTextEdit(self.centralwidget)
		self.textLine_White_votes.setGeometry(QtCore.QRect(180, 680, 121, 31))
		self.textLine_White_votes.setObjectName("textLine_White_votes")
		self.textLine_White_votes.setPlaceholderText("NEVAŽEĆI LISTIĆI")
		self.textLine_White_votes.setTabChangesFocus(True)

		"""
		MANDATES textEdit
		"""
		self.textEdit_Mandates = QtWidgets.QTextEdit(self.centralwidget)
		self.textEdit_Mandates.setGeometry(QtCore.QRect(350, 91, 50, 31))
		self.textEdit_Mandates.setObjectName("textEdit_Mandates")
		self.textEdit_Mandates.setTabChangesFocus(True)

		"""
		CENSUS textEdit
		"""
		self.textEdit_Census = QtWidgets.QLineEdit(self.centralwidget)
		self.textEdit_Census.setGeometry(QtCore.QRect(510, 91, 50, 31))
		self.textEdit_Census.setObjectName("textEdit_Census")

		"""
		Upper labels
		"""
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(150, 41, 171, 41))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label.setFont(font)
		self.label.setObjectName("label")

		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(0, 41, 171, 40))
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")

		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(320, 41, 171, 40))
		self.label_2.setFont(font)
		self.label_2.setText("BROJ MANDATA")
		self.label_2.setObjectName("label_2")

		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(500, 41, 171, 40))
		self.label_4.setFont(font)
		self.label_4.setText("CENZUS(%)")
		self.label_4.setObjectName("label_4")

		"""
		Overall votes labels:
		"""
		self.label_overall = QtWidgets.QLabel(self.centralwidget)
		self.label_overall.setGeometry(QtCore.QRect(625, 700, 90, 40))
		self.label_overall.setFont(font)
		self.label_overall.setObjectName("label_overall")

		self.label_overall_text = QtWidgets.QLabel(self.centralwidget)
		self.label_overall_text.setGeometry(QtCore.QRect(440, 700, 170, 40))
		self.label_overall_text.setFont(font)
		self.label_overall_text.setObjectName("label_overall_text")

		"""
		Census labels
		"""
		self.label_census = QtWidgets.QLabel(self.centralwidget)
		self.label_census.setGeometry(QtCore.QRect(1000, 700, 90, 40))
		self.label_census.setFont(font)
		self.label_census.setObjectName("label_census")

		self.label_census_text = QtWidgets.QLabel(self.centralwidget)
		self.label_census_text.setGeometry(QtCore.QRect(800, 700, 180, 40))
		self.label_census_text.setFont(font)
		self.label_census_text.setObjectName("label_census_text")


		"""
		Buttons
		"""
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(440, 500, 121, 71))
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.calculate_dhont)

		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setGeometry(QtCore.QRect(30, 660, 80, 40))
		self.pushButton_2.setObjectName("pushButton2")
		self.pushButton_2.setText("LOCK")
		self.pushButton_2.clicked.connect(self.lock_text_parties)

		self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_3.setGeometry(QtCore.QRect(30, 700, 80, 40))
		self.pushButton_3.setObjectName("pushButton3")
		self.pushButton_3.setText("UNLOCK")
		self.pushButton_3.clicked.connect(self.unlock_text_parties)

		"""
		Bar plot Button
		"""
		self.pushButton_bar_plot = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_bar_plot.setGeometry(QtCore.QRect(440, 600, 121, 71))
		self.pushButton_bar_plot.setText("BarPlot")
		self.pushButton_bar_plot.setObjectName("pushButton_bar_plot")
		self.pushButton_bar_plot.clicked.connect(lambda: self.bar_plot(self.mandate_dict))

		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 877, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.set_text_parties()
		self.set_minority_checkbox()

	def create_text_edit(self):
		for i in range(1, 25):
			if i % 2 != 0:
				textEdit = QtWidgets.QTextEdit(self.centralwidget)
				textEdit.setGeometry(QtCore.QRect(20, 51+(i*25), 121, 31))
				textEdit.setObjectName(f"textEdit_{i}")
				textEdit.setTabChangesFocus(True)
				setattr(self, f"textEdit_{i}", textEdit)
			else:
				textEdit = QtWidgets.QTextEdit(self.centralwidget)
				textEdit.setGeometry(QtCore.QRect(180, 1+((i+1)*25), 121, 31))
				textEdit.setObjectName(f"textEdit_{i}")
				textEdit.setTabChangesFocus(True)
				setattr(self, f"textEdit_{i}", textEdit)

	def set_minority_checkbox(self):
		"""
		Make checkbox for each party; if checked then minority rules apply
		"""
		for i in range(12):
			checkbox = QtWidgets.QCheckBox(self.centralwidget)
			setattr(self, f"checkbox_{i}", checkbox)
			checkbox.setGeometry(QtCore.QRect(148, 35+50*(i+1), 15, 15))
			checkbox.setObjectName(f"checkbox_{i}")
			self.checkbox_list.append(checkbox)

	def set_label_overall(self, total_votes):
		self.label_overall.setText(str(total_votes))
		self.label_overall_text.setText("UKUPNO GLASOVA: ")

	def set_census(self, total_votes):
		self.label_census_text.setText("CENZUS (GLASOVA): ")
		temp_census = self.get_census() * total_votes
		self.label_census.setText(str(temp_census))

	def set_result_labels(self, mandate_dict):
		"""
		Result LABELS
		setattr()!!!
		"""
		font = QtGui.QFont()
		font.setPointSize(14)
		for i in range(len(self.text_parties_names)):
			"""
			try/except: if party > CENSUS else 0; To avoid KeyError with mandate_dict[i]; because text_parties_names contains ALL parties!
			"""
			try:
				party_mandate = mandate_dict[i]
			except:
				party_mandate = 0
			if (i+1) > len(self.result_labels_list):
				label = QtWidgets.QLabel(self.centralwidget)
				setattr(self, f"label_{i+5}", label)
				label.setGeometry(QtCore.QRect(700, (100+40*i), 80, 50))
				label.setFont(font)
				label.setText(self.text_parties_names[i] + " " + str(party_mandate))
				label.setObjectName(f"label_{i+5}")
				label.show()
				self.result_labels_list.append(label)
			else:
				self.result_labels_list[i].setText(self.text_parties_names[i] + " " + str(party_mandate))

	def set_text_parties(self):
		for i in range(1, 25):
			if i % 2 != 0:
				self.text_edit_parties_list.append(eval(f"self.textEdit_{i}"))

	def lock_text_parties(self):
		"""
		Lock party names and INITs text_parties_names LIST
		"""
		for text_edit in self.text_edit_parties_list:
			text_edit.setDisabled(1)
		self.get_parties_names()

	def unlock_text_parties(self):
		"""
		Unlock party names and CLEARs text_parties_names LIST
		"""
		for text_edit in self.text_edit_parties_list:
			text_edit.setDisabled(0)
		self.text_parties_names.clear()

	def get_parties_names(self):
		for text_edit in self.text_edit_parties_list:
			if text_edit.toPlainText():
				self.text_parties_names.append(text_edit.toPlainText())

	def set_text_edit(self):
		"""
		Adds textEdits to the list for later value extraction
		"""
		#self.text_edits_list.append(self.textEdit)
		for i in range(1, 25):
			if i % 2 == 0:
				self.text_edits_list.append(eval(f"self.textEdit_{i}"))

	def remove_text_edit(self):
		"""
		Clears the list, enables changes in the textedits and NEW calc
		"""
		self.text_edits_list.clear()

	def get_votes_from_text_edit(self):
		"""
		return: dictionary with votes
		Gets int(values) from list of textEdits, 0 if empty
		"""
		votes_dict = {}
		for i, text_edit in enumerate(self.text_edits_list):
			votes_dict[i] = int(text_edit.toPlainText()) if text_edit.toPlainText() else 0

		return votes_dict

	def get_number_of_mandates(self):
		mandate_number = int(self.textEdit_Mandates.toPlainText()) if self.textEdit_Mandates.toPlainText() else 0
		assert mandate_number > 0
		return mandate_number

	def get_census(self):
		"""
		return: census in %
		"""
		census = int(self.textEdit_Census.text()) if self.textEdit_Census.text() else 0
		return census*0.01

	def bar_plot(self, mandate_dict):
		new_bar_plot = DhontPlot(self.text_parties_names, mandate_dict)
		new_bar_plot.bar_plot()

	def prepare_dhont(self):
		"""
		return: census and mandate dict
		Init 2 dicts for calculation
		Add WHITE_votes to the sum
		If < census and minority -> *= 1.35
		Call set_overall_label(total_votes)
		"""
		temp_overall_votes_dict = self.get_votes_from_text_edit()
		temp_overall_votes_sum = sum(temp_overall_votes_dict.values())
		if self.textLine_White_votes.toPlainText():
			temp_overall_votes_sum += int(self.textLine_White_votes.toPlainText())
		temp_census_dict = {}
		temp_mandate_dict = {}

		for key in temp_overall_votes_dict.keys():
			if self.checkbox_list[key].isChecked():
				if temp_overall_votes_dict[key] < temp_overall_votes_sum * self.get_census():
					temp_overall_votes_dict[key] *= 1.35
			if temp_overall_votes_dict[key] >= temp_overall_votes_sum * self.get_census() or self.checkbox_list[key].isChecked(): #Or self.checkbox_list[key].isChecked()
				temp_census_dict[key] = temp_overall_votes_dict[key]

		for key in temp_census_dict.keys():
			temp_mandate_dict[key] = 0

		self.set_label_overall(temp_overall_votes_sum)
		self.set_census(temp_overall_votes_sum)

		return temp_overall_votes_dict, temp_census_dict, temp_mandate_dict

	def calculate_dhont(self):
		"""
		Calculates the number of mandates
		"""
		self.set_text_edit()
		overall_votes_dict, census_dict, mandate_dict = self.prepare_dhont()
		temp_mandate_dict, temp_census_dict = calculate_mandates(overall_votes_dict, census_dict, mandate_dict, self.get_number_of_mandates())
		self.mandate_dict = temp_mandate_dict
		self.cheapest_mandate_dict = temp_census_dict
		self.set_result_labels(temp_mandate_dict)
		print("NAJJEFTINIJI: ", self.cheapest_mandate_dict[0])
		self.remove_text_edit()

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "D'hont IZBORI 2020"))
		self.label.setText(_translate("MainWindow", "    BROJ GLASOVA"))
		self.label_3.setText(_translate("MainWindow", "    NAZIV LISTE"))
		self.pushButton.setText(_translate("MainWindow", "CALCULATE"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())