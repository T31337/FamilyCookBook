#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#This File Was Created With A Little Help From QtDesigner4

import PySide
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
from PySide.QtGui import *
from PySide.QtCore import *
import configparser,sys,os

conf = configparser.ConfigParser()
conf.add_section("Recipe")

#savefile = 'GenericRecipe.ini'
dir = os.get_exec_path()
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


class RecipeCard(QtGui.QWidget):
    
    dir = os.get_exec_path()
    path = str(os.getcwd())
    print("Current Directory:\n"+os.getcwd())
    if  not path.endswith("Recipes"):
        try:
            dir = os.chdir("Recipes")
        except:
            os.mkdir("Recipes")
            os.chdir("Recipes")
    try:
        
        os.mkdir("Appitizers")
        os.mkdir("Breads")
        os.mkdir("Cake")
        os.mkdir("Candy")
        os.mkdir("Cookies")
        os.mkdir("Desserts")
        os.mkdir("Fish And SeaFood")
        os.mkdir("Meat")
        os.mkdir("Misc")
        os.mkdir("Pasta")
        os.mkdir("Pi")
        os.mkdir("Soups Ans Stews")
        os.mkdir("Vegetables")
        
    except:
        pass
   
    savefile = 'GenericRecipe.ini'
    
    def saveRecipe(self):
        print("SaveButton Pressed :D")
       # print("Directory:\n"+os.getcwd())
              
        '''
        path = os.getcwd()
        print("Path:\n"+path)
        if os.path.curdir.endswith("Recipes"):
            print("if os.path.curdir.endswith(Recipies)...")
            print("path:\n"+path)
        else:
            print("not os.path.curdir.endswith(Recipes)")
            dir = os.chdir(os.pardir)
            print("path:\n"+path)
        path = os.chdir(self.comboBox.currentText())
        print("path:\n"+path) 
        '''
        if self.lineEdit.text() != None or self.lineEdit != "":
            self.savefile = self.lineEdit.text()+'.ini'
        
        conf.set("Recipe","Catagory",self.comboBox.currentText())       
        conf.set("Recipe","Name",self.lineEdit.text())
        conf.set("Recipe","Requirements", self.textEdit.toPlainText())
        conf.set("Recipe","Directions",self.textEdit_2.toPlainText())
       
        path = os.getcwd()
        if str(path).endswith("Recipes"):
            dir =  os.chdir(self.comboBox.currentText())
        else:
            dir = os.getcwd()
            dir = os.chdir(os.pardir)
            dir = os.chdir(self.comboBox.currentText())
        Recipe = open(self.savefile,mode='w')
        conf.write(Recipe)
       # savefile.close()#?
        Recipe.close()
        print("Save Sucessful!")
        print("Recipe Saved To:\n"+os.getcwd())
        btn = QPushButton("Close Recipe Card")
       # QMessageBox.information(self, 'PyCookBook', "Your Recipe Was Saved Sucessfuly!",QMessageBox.Ok)
        msg = QMessageBox()
        msg.setText("Save Was Sucessful!\n:D Thanks For Using PyCookBook!")
        #yes = QtGui.QPushButton("Yes!")
        #msg.addButton(yes,QtGui.QMessageBox.YesRole)
        #no = QtGui.QPushButton("No, I Still Need That!")
        #msg.addButton(no,QtGui.QMessageBox.NoRole)
        msg.exec_()
              
        #if msg.clickedButton() == yes:
         #   print("Close RecipeCard Choosen...")
          #  SelectionMenu.SelectionMenu.CloseRecipe(Recipe)
        '''
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Save Sucessful!")
        msg.setWindowTitle("PyCookBook")
        msg.addButton(btn,QMessageBox.YesRole)
        btn2 = QPushButton("OK")
        msg.addButton(btn2,QMessageBox.NoRole)
        msg.exec_()
        '''
        
        if msg.clickedButton() == btn:
            print("Close Recipe Card Selected")
            #?ToDo: Close Ui_RecipeCard
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("PyCookBook")
            msg.setText("Sorry, That Is Option Is Not Working Yet...")
            msg.addButton(QMessageBox.Ok)
            msg.exec_()
            try:
                #?How To Close The RecipeCard?#
                Ui_RecipeCard.close(SelectionMenu.Form)
                
            except Exception as e:
                print("Error:\n"+str(e))
            try:
                Ui_RecipeCard.close(RecipeCard)
            except Exception as e:
                print("Errot:\n"+str(e))
        '''

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
             

    def setupUi(self, RecipeCard):
        dir = os.get_exec_path()
        '''
        path = os.getcwd()
        print("Path:\n"+path)
        if os.path.curdir.endswith("Recipes"):
            
            try:
                for item in range(0,self.comboBox.size()):
                    print("mkdir("+self.comboBox.itemText(item)+")")
                    os.mkdir(self.comboBox.itemText(item))
            except:
                pass

       
        '''
            os.mkdir("Appitizers")
            os.mkdir("Breads")
            os.mkdir("Cake")
            os.mkdir("Candy")
            os.mkdir("Cookies")
            os.mkdir("Desserts")
            os.mkdir("Fish And SeaFood")
            os.mkdir("Meat")
            os.mkdir("Misc")
            os.mkdir("Pasta")
            os.mkdir("Pi")
            os.mkdir("Soups Ans Stews")
            os.mkdir("Vegetables")
            '''
   
        #RecipeCard.setObjectName(_fromUtf8("RecipeCard"))
        
        RecipeCard.resize(640, 776)
      #  self.setWindowTitle("RecipeCard")
        #self.resize(640,776)
        self.verticalLayout_2 = QtGui.QVBoxLayout(RecipeCard)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBox = QtGui.QComboBox(RecipeCard)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox)
        self.label = QtGui.QLabel(RecipeCard)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(RecipeCard)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_2 = QtGui.QLabel(RecipeCard)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.textEdit = QtGui.QTextEdit(RecipeCard)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_2.addWidget(self.textEdit)
        self.label_3 = QtGui.QLabel(RecipeCard)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.textEdit_2 = QtGui.QTextEdit(RecipeCard)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.verticalLayout_2.addWidget(self.textEdit_2)
        self.pushButton = QtGui.QPushButton(RecipeCard)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setText("Save Recipe!")
         #self.pushButton.setText(_translate("RecipeCard", "Save Recipe!", None))
        self.verticalLayout_2.addWidget(self.pushButton)
        
        """
        <:Testing Zone:>
        """ 
        #
        self.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.saveRecipe)
        #self.pushButton.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.saveRecipe(self.savefile))                
        
        #
        """
        <:Testing Zone:>
        """
        self.retranslateUi(RecipeCard)
        QtCore.QMetaObject.connectSlotsByName(RecipeCard)

    def retranslateUi(self, RecipeCard):
        RecipeCard.setWindowTitle(_translate("RecipeCard", "PyCookBook - RecipeCard", None))
        
        self.comboBox.setItemText(0, _translate("RecipeCard", "Appitizers", None))
        self.comboBox.setItemText(1, _translate("RecipeCard", "Breads", None))
        self.comboBox.setItemText(2, _translate("RecipeCard", "Cake", None))
        self.comboBox.setItemText(3, _translate("RecipeCard", "Candy", None))
        self.comboBox.setItemText(4, _translate("RecipeCard", "Cookies", None))
        self.comboBox.setItemText(5, _translate("RecipeCard", "Desserts", None))
        self.comboBox.setItemText(6, _translate("RecipeCard", "Fish And SeaFood", None))
        self.comboBox.setItemText(7, _translate("RecipeCard", "Meat", None))
        self.comboBox.setItemText(8, _translate("RecipeCard", "Misc", None))
        self.comboBox.setItemText(9, _translate("RecipeCard", "Pies", None))
        self.comboBox.setItemText(10,_translate("RecipieCard", "Pasta",None))
        self.comboBox.setItemText(11, _translate("RecipeCard", "Soups And Stews", None))
        self.comboBox.setItemText(12, _translate("RecipeCard", "Vegetables", None))
        self.label.setText(_translate("RecipeCard", "Recipe Name:", None))
        self.label_2.setText(_translate("RecipeCard", "Ingredients:", None))
        self.textEdit.setHtml(_translate("RecipeCard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Source Sans Pro\'; font-size:13pt; font-weight:200; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_3.setText(_translate("RecipeCard", "Directions:", None))



        
        
                  
        



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
        self.mylist = QtGui.QTreeView(Form)
        self.mylist.setObjectName(_fromUtf8("mylist"))
        self.verticalLayout.addWidget(self.mylist)
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
        Form.setWindowTitle(_translate("Form", "PyCookBook", None))
        self.openBtn.setText(_translate("Form", "Open Recipe", None))
        self.newBtn.setText(_translate("Form", "New Recipe", None))
        
    def openFile(self):
        print("OpenFile Pressed!")
        dir  = os.getcwd()
        if not str(dir).endswith("Recipes"):
            try:
                os.chdir("Recipes")
            except:
                os.chdir(os.pardir)
        #dir = os.chdir("Recipes")
        self.file = QtGui.QFileDialog.getOpenFileName(self,"PyCookBook - Open Recipe",filter="Recipe Files(*.ini)")
      
    
        if not self.file[0]:
            pass
        else:
            print("Opening File....")
           # self.file = self.win.fileSelected
            self.conf.read(self.file)
            print("Recipe File Has Been Read Into self.conf")
            self.Recipe=QtGui.QWidget()
            self.Card = RecipeCard()
            self.Card.setupUi(self.Recipe)
            self.Recipe.show()
            print("Setting Values On Recipe Card...")
            
            self.Card.comboBox.setItemText(self.Card.comboBox.currentIndex(),self.conf.get("Recipe","Catagory"))
            self.Card.lineEdit.setText(self.conf.get("Recipe","Name"))
            self.Card.textEdit.setText(self.conf.get("Recipe","Requirements"))
            self.Card.textEdit_2.setText(self.conf.get("Recipe","Directions"))
            #Recipe.show()
            print("Recipe Should Be Showing And Set...")

    def newRecipe(self):
        dir = "."
        print("NewRecipe Button Pressed!")
        self.Recipe = QtGui.QWidget()
        self.Card = RecipeCard()
        self.Card.setupUi(self.Recipe)
        self.Recipe.show()

    def CloseRecipe(self):
        #This Has Been Challengeing, Not Too Important, May Add In Future...
        pass
          

if __name__ == "__main__":
    import sys
    '''
    app = QtGui.QApplication(sys.argv)
    RecipeCard = QtGui.QWidget()
    ui = Ui_RecipeCard()
    ui.setupUi(RecipeCard)
    RecipeCard.show()
    sys.exit(app.exec_())
    '''
    app = QtGui.QApplication(sys.argv)
    Card = QtGui.QWidget()
    Menu = SelectionMenu()
    Menu.setupUi(Card)
    Card.show()
    sys.exit(app.exec_())

