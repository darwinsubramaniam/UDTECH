# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'udlab.ui'
#
# Created: Sat Sep 26 19:38:04 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 596)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 80, 431, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.NumOfVar_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.NumOfVar_layout.setContentsMargins(0, 0, 0, 0)
        self.NumOfVar_layout.setObjectName("NumOfVar_layout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(219, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.NumOfVar_layout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_7.addWidget(self.horizontalSlider)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_7.addWidget(self.lineEdit_2)
        self.NumOfVar_layout.addLayout(self.horizontalLayout_7)
        spacerItem3 = QtWidgets.QSpacerItem(20, 49, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.NumOfVar_layout.addItem(spacerItem3)
        self.LabName_layout = QtWidgets.QSplitter(self.centralwidget)
        self.LabName_layout.setGeometry(QtCore.QRect(70, 30, 331, 27))
        self.LabName_layout.setOrientation(QtCore.Qt.Horizontal)
        self.LabName_layout.setObjectName("LabName_layout")
        self.label = QtWidgets.QLabel(self.LabName_layout)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.LabName_layout)
        self.lineEdit.setMaxLength(32772)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(61, 411, 311, 111))
        self.widget.setObjectName("widget")
        self.DeviceSetting_layout = QtWidgets.QVBoxLayout(self.widget)
        self.DeviceSetting_layout.setContentsMargins(0, 0, 0, 0)
        self.DeviceSetting_layout.setObjectName("DeviceSetting_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DeviceSettingButton = QtWidgets.QPushButton(self.widget)
        self.DeviceSettingButton.setObjectName("DeviceSettingButton")
        self.horizontalLayout.addWidget(self.DeviceSettingButton)
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.DeviceSetting_layout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.DataCollectionSettingButton = QtWidgets.QPushButton(self.widget)
        self.DataCollectionSettingButton.setCheckable(False)
        self.DataCollectionSettingButton.setObjectName("DataCollectionSettingButton")
        self.horizontalLayout_5.addWidget(self.DataCollectionSettingButton)
        spacerItem4 = QtWidgets.QSpacerItem(107, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.DeviceSetting_layout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionPrint_2 = QtWidgets.QAction(MainWindow)
        self.actionPrint_2.setObjectName("actionPrint_2")
        self.actionImport_Lab = QtWidgets.QAction(MainWindow)
        self.actionImport_Lab.setObjectName("actionImport_Lab")
        self.actionExport_lab = QtWidgets.QAction(MainWindow)
        self.actionExport_lab.setObjectName("actionExport_lab")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint_2)
        self.menuFile.addAction(self.actionImport_Lab)
        self.menuFile.addAction(self.actionExport_lab)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.horizontalSlider.valueChanged['int'].connect(self.label_3.setNum)
        self.label_3.linkActivated['QString'].connect(self.lineEdit_2.setText)
        self.lineEdit_2.textEdited['QString'].connect(self.label_3.setText)
        self.horizontalSlider.rangeChanged['int','int'].connect(self.horizontalSlider.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UDlab "))
        self.label_3.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Number Of Variables :"))
        self.lineEdit_2.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Lab Name"))
        self.DeviceSettingButton.setText(_translate("MainWindow", "Device Setting "))
        self.radioButton.setText(_translate("MainWindow", "Device Connected"))
        self.DataCollectionSettingButton.setText(_translate("MainWindow", "Data Collection Settings "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionNew.setText(_translate("MainWindow", "New Lab"))
        self.actionOpen.setText(_translate("MainWindow", "Open Lab"))
        self.actionSave.setText(_translate("MainWindow", "Last Open Lab"))
        self.actionSave_as.setText(_translate("MainWindow", "Save "))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionPrint_2.setText(_translate("MainWindow", "Print "))
        self.actionImport_Lab.setText(_translate("MainWindow", "Import Lab"))
        self.actionExport_lab.setText(_translate("MainWindow", "Export lab"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

