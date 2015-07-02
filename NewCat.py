# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewCatagory.ui'
#
# Created: Fri Jan 30 22:41:07 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import PySide,os
from PySide import QtCore, QtGui


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(QtGui.QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(414, 106)

        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        
        self.lbl = QtGui.QLabel("Catagory Name:")
        self.verticalLayout.addWidget(self.lbl)
        
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        #self.AbortBtn = QtGui.QPushButton(Dialog)
        #self.AbortBtn.setObjectName(_fromUtf8("AbortBtn"))
        #self.horizontalLayout.addWidget(self.AbortBtn)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
        self.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.CreateNewCat)

        #self.connect(self.AbortBtn,QtCore.SIGNAL("clicked()"),self.done)
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "CookBook", None))
        #self.AbortBtn.setText(_translate("Dialog", "/!\\ Abort! /!\\", None))
        self.pushButton.setText(_translate("Dialog", "Save", None))
    
    def done(self):
        capp.exit()
            
    def CreateNewCat(self):
        dir = os.getcwd()
        if not str(dir).endswith("Recipes"):
            try:
                os.chdir("Recipes")
            except:
                os.chdir(os.pardir)
        try:
            os.mkdir(str(self.lineEdit.text()))
            self.done()
        except Exception as e:
            print(e)
            error = QtGui.QMessageBox()
            error.setText('Error:\n'+str(e))
            error.setWindowTitle('CookBook')
            error.exec_()
            error.hasFocus()
            
if __name__ == "__main__":
    import sys

    capp = QtGui.QApplication(sys.argv)
    new_Form = QtGui.QWidget()
    new_ui = Ui_Dialog()
    new_ui.setupUi(new_Form)
    new_Form.show()
    sys.exit(capp.exec_())
