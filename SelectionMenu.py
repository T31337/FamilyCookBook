#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#This File Was Created With A LIttle Help From QtDesigner4

import PySide
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
from PySide.QtGui import *
from PySide.QtCore import *
from PIL import Image
import configparser,os
import RecipeCard


dir = "."
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

class SelectionMenu(QtGui.QWidget):

    conf = configparser.ConfigParser()

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self) 
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(381, 254)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        #
        self.img = QtGui.QLabel(Form)
        self.img.setPixmap('Logo.png')
        self.verticalLayout.addWidget(self.img)
        self.img.show()
        
        #
        #
        '''
        self.mylist = QtGui.QTreeView(Form)
        self.mylist.setObjectName(_fromUtf8("mylist"))
        self.verticalLayout.addWidget(self.mylist)
        '''
        #
        #
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.openBtn = QtGui.QPushButton(Form)
        self.openBtn.setObjectName(_fromUtf8("openBtn"))
        self.horizontalLayout_2.addWidget(self.openBtn)
        self.newBtn = QtGui.QPushButton(Form)
        self.newBtn.setObjectName(_fromUtf8("newBtn"))
        self.horizontalLayout_2.addWidget(self.newBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.connect(self.openBtn,QtCore.SIGNAL("clicked()"),self.openFile)
        self.connect(self.newBtn,QtCore.SIGNAL("clicked()"),self.newRecipe)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "CookBook", None))
        self.openBtn.setText(_translate("Form", "Open Recipe", None))
        self.newBtn.setText(_translate("Form", "New Recipe", None))
        
    def openFile(self):
        print("OpenFile Pressed!")
        dir  =  os.getcwd()
        print("CWD: "+os.getcwd())
        if not str(dir).endswith("Recipes"):
            try:
                os.chdir("Recipes")
            except:
                os.chdir(os.pardir)
        print("New CWD: "+os.getcwd())
        #dir = os.chdir("Recipes")
        self.file = QtGui.QFileDialog.getOpenFileName(self,"CookBook - Open Recipe",filter="Recipe Files(*.ini)")
      
    
        if not self.file[0]:
            pass
        else:
            print("Opening File....")
           # self.file = self.win.fileSelected
            self.conf.read(self.file)
            print("Recipe File Has Been Read Into self.conf")
            self.Recipe=QtGui.QWidget()
            self.Card = RecipeCard.Ui_RecipeCard()
            self.Card.setupUi(self.Recipe)
            self.Recipe.show()
            print("Setting Values On Recipe Card...")
            
            self.Card.comboBox.setItemText(self.Card.comboBox.currentIndex(),self.conf.get("Recipe","Catagory"))
            self.Card.lineEdit.setText(self.conf.get("Recipe","Name"))
            self.Card.textEdit.setText(self.conf.get("Recipe","Requirements"))
            self.Card.textEdit_2.setText(self.conf.get("Recipe","Directions"))
            
            print("Recipe Should Be Showing And Set...")

    def newRecipe(self):
        dir = os.getcwd()
        if not str(dir).endswith("Recipes"):
            try:
                os.chdir("Recipes")
            except:
                os.chdir(os.pardir)   
                
        print("NewRecipe Button Pressed!")
        self.Recipe = QtGui.QWidget()
        self.Card = RecipeCard.Ui_RecipeCard()
        self.Card.setupUi(self.Recipe)
        self.Card.setWindowTitle("RecipeCard")
        self.Recipe.show()

    def CloseRecipe(self):
        #This Has Been Challengeing, Not Too Important, May Add In Future...
        pass
    
        
if __name__ == "__main__":
    import sys
    dir = "."
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = SelectionMenu()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())