#!/usr/bin/env python
import PySide,os,time
from PySide import QtGui,QtCore

import configparser,sys,os
import NewCat
conf = configparser.ConfigParser()
conf.add_section("Recipe")
 
#savefile = 'GenericRecipe.ini'
 
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
 
 


class Ui_RecipeCard(QtGui.QWidget): 
    savefile = 'GenericRecipe.ini'
    #dir = os.path.expanduser("~")
    dir = os.getcwd()
    #if not str(dir).endswith("CookBook"):
    try:
        #os.chdir("CookBook")
        os.chdir("Recipes")
    except:
        #os.chdir(os.pardir)
        try:
            os.mkdir("Recipes")
        except:
            pass
        os.chdir("Recipes")    
    try:
                os.mkdir('Appitizers')
                os.mkdir('Breads')
                os.mkdir('Cake')
                os.mkdir('Candy')
                os.mkdir('Cookies')
                os.mkdir('Desserts')
                os.mkdir('Fish & SeaFood')
                os.mkdir('Meat')
                os.mkdir('Misc')
                os.mkdir('Pies')
                os.mkdir('Soups & Stews')
                os.mkdir('Vegetables')
    except:
        pass     
    def list_files(dir):
        r = []
        subdirs = [x[0] for x in os.walk(dir)]
        print(subdirs)
        for subdir in subdirs:                                                                                            
            files = os.walk(subdir).next()[2]                                                                             
            if (len(files) > 0):                                                                                          
                for file in files:                                                                                        
                    r.append(subdir + "/" + file)                                                                         
        return r 
    
    
    def saveRecipe(self):
        dir = os.path.expanduser("~")
        #dir = os.getcwd()
        if not str(dir).endswith("CookBook"):
            try:
                os.chdir("CookBook")
                os.chdir("Recipes")
            except:
                #os.chdir(os.pardir)
                try:
                    os.mkdir("Recipes")
                except:
                    pass
                os.chdir("Recipes")
        
                
            
        #AllItems = [self.comboBox.itemText(i) for i in range(self.comboBox.count())]
        '''
        for i in range(self.comboBox.count()):
            txt = self.comboBox.itemText(i)
            try:
                os.mkdir(txt)
            except:
                pass
        '''
        self.pic = None
        print("CWD: "+os.getcwd())
        print("SaveButton Pressed :D")
        if not self.lineEdit.text() == None:
            self.savefile = self.lineEdit.text()+'.ini'
        conf.set("Recipe","Catagory",str(self.comboBox.currentText()) )      
        conf.set("Recipe","Name",self.lineEdit.text())
        conf.set("Recipe","Requirements", self.textEdit.toPlainText())
        conf.set("Recipe","Directions",self.textEdit_2.toPlainText())
        conf.set("Recipe","Picture",'')
        os.chdir(str(self.comboBox.currentText() ))
        Recipe = open(self.savefile,'w')
        conf.write(Recipe)
        
        Recipe.close()
        os.chdir(os.pardir)
        
        msg = QtGui.QMessageBox(self)    
        msg.setWindowTitle("CookBook")
        
        msg.NoRole=msg.addButton(QtGui.QMessageBox.NoButton)
        quit_msg = "Save Sucessful!\nClose CookBook?"

        #ToDo: Make This A User Configuration Option
        
        '''
        msg.setText("Save Sucessful! - Close CookBook?")
        reply = QtGui.QMessageBox.question(self, 'Message', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
    
        if reply == QtGui.QMessageBox.Yes:
            import sys    
            sys.exit()
            #app.quit()
        else:
            pass
        '''
    #   
    #       
        '''
   def __init__(self):
       QWidget.__init__(self)
       self.setupUi(self)
       '''
    def setupUi(self, RecipeCard):
        
        dir = os.getcwd()
        if not str(dir).endswith("Recipes"):
            try:
                os.chdir("Recipes")
            except:
                #os.chdir(os.pardir)
                os.mkdir("Recipes")
                os.chdir("Recipes")
                        
                  
       # RecipeCard.setObjectName(_fromUtf8("RecipeCard"))
        RecipeCard.resize(640, 776)
       
        #self.resize(640,776)
        self.verticalLayout_2 = QtGui.QVBoxLayout(RecipeCard)
        #self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        #
        #
        '''
        self.img = QtGui.QLabel(Form)
        self.img.setPixmap('Creeper.png')
        self.verticalLayout.addWidget(self.img)
        self.img.show() 
        '''
        #
        #
                
        #self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBox = QtGui.QComboBox(RecipeCard)
        #self.comboBox.setObjectName(_fromUtf8("comboBox"))
        '''
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
        '''
        self.verticalLayout.addWidget(self.comboBox)
        self.newCat = QtGui.QPushButton("New Cataogry!?") 
        self.verticalLayout.addWidget(self.newCat)     
        self.label = QtGui.QLabel(RecipeCard)

        #self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        #
        self.lineEdit = QtGui.QLineEdit(RecipeCard)
        #self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        
        
        #Picture#
        #Note: This Needs To Be Dynamic Based On Recipe Name
        
        self.pic = QtGui.QLabel()
        self.verticalLayout.addWidget(self.pic)        
              
        try:
            self.pic.setPixmap('food.jpg')
        except:
            self.pic.setPixmap('food.png')
        #End Picture#
        
        
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_2 = QtGui.QLabel(RecipeCard)
        #self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.textEdit = QtGui.QTextEdit(RecipeCard)
        #self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_2.addWidget(self.textEdit)
        self.label_3 = QtGui.QLabel(RecipeCard)
        #self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.textEdit_2 = QtGui.QTextEdit(RecipeCard)
        #self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.verticalLayout_2.addWidget(self.textEdit_2)
        self.pushButton = QtGui.QPushButton(RecipeCard)
        #self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setText("Save Recipe!")
         #self.pushButton.setText(_translate("RecipeCard", "Save Recipe!", None))
        self.verticalLayout_2.addWidget(self.pushButton)
       
        self.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.saveRecipe)
        self.connect(self.newCat,QtCore.SIGNAL("clicked()"),self.createCat)
        #self.pushButton.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.saveRecipe(self.savefile))                
          
          
      
        subdirs = [x[0] for x in os.walk(os.getcwd())] 
        for folder in subdirs:
            self.comboBox.addItem(folder)
       
        self.retranslateUi(RecipeCard)
        QtCore.QMetaObject.connectSlotsByName(RecipeCard)
        
       
    def createCat(self):
        dir = os.getcwd()
        if not str(dir).endswith("Recipes"):
            try:
                os.chdir("Recipes")
            except:
                #os.chdir(os.pardir)
                os.mkdir("Recipes")
                os.chdir("Recipes")
                
        try:
            print("NewCat?")
            '''
            msg = QtGui.QMessageBox()
            msg.setText("Sorry, Not Yet Implemented...")
            msg.setWindowTitle("CookBook")
            msg.exec_()
            '''
             
            self.Form2 = QtGui.QWidget()
            self.ui2 = NewCat.Ui_Dialog()
            self.ui2.setupUi(self.Form2)
            self.Form2.show()
            
            
            
            
        except Exception as e:
            print("TraceStack?:\n"+str(e.with_traceback))
            print("\n\n"+str(e.args)+"\n\n")
            print(e)
                      
        
    def retranslateUi(self, RecipeCard):
            RecipeCard.setWindowTitle("CookBook - RecipeCard")
            #RecipeCard.setWindowTitle(_translate("RecipeCard", "PyCookBook - RecipeCard", None))
            
            '''
            self.comboBox.setItemText(0, _translate("RecipeCard", "Appitizers", None))
            self.comboBox.setItemText(1, _translate("RecipeCard", "Breads", None))
            self.comboBox.setItemText(2, _translate("RecipeCard", "Cake", None))
            self.comboBox.setItemText(3, _translate("RecipeCard", "Candy", None))
            self.comboBox.setItemText(4, _translate("RecipeCard", "Cookies", None))
            self.comboBox.setItemText(5, _translate("RecipeCard", "Desserts", None))
            self.comboBox.setItemText(6, _translate("RecipeCard", "Fish & SeaFood", None))
            self.comboBox.setItemText(7, _translate("RecipeCard", "Meat", None))
            self.comboBox.setItemText(8, _translate("RecipeCard", "Misc", None))
            self.comboBox.setItemText(9, _translate("RecipeCard", "Pies", None))
            self.comboBox.setItemText(10, _translate("RecipeCard", "Soups & Stews", None))
            self.comboBox.setItemText(11, _translate("RecipeCard", "Vegetables", None))
            '''
            self.label.setText(_translate("RecipeCard", "Recipe Name:", None))
            self.label_2.setText(_translate("RecipeCard", "Ingredients:", None))
            self.textEdit.setHtml(_translate("RecipeCard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'Source Sans Pro\'; font-size:13pt; font-weight:200; font-style:normal;\">\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
            self.label_3.setText(_translate("RecipeCard", "Directions:", None))






if __name__ == "__main__":
    import sys
    dir = "."
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_RecipeCard()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
