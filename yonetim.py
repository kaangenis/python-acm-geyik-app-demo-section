#-----------------------Kütüphane-----------------------#
#-------------------------------------------------------#

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from geyikui import *
from time import *


#-----------------------Uygulama------------------------#
#-------------------------------------------------------#

Uygulama = QApplication(sys.argv)
penAna = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()


#Fonksiyonlar: 

def SEMTSURE():
    deger = ui.comboBox
    #ayranci = "Ayrancı, Hoşdere, Oran: 12.00, 20 TL"
    #bahceliemek = "Bahçelievler"
    #batikent = "Batıkent-1"
    
    deger.setItemData(1, (
        
        "Ayrancı Kalkış: 08.00"
        + "\n" 
        + "Beytepe Kalkış: 16.00" 
        + "\n" 
        + "Ücret: 30 TL"))
    
    
    deger.setItemData(2, (
        
        "Bahçelievler Kalkış: 08.10"
        + "\n" 
        + "Beytepe Kalkış: 16.00" 
        + "\n" 
        + "Ücret: 20 TL"))
    
    
    deger.setItemData(3, (
        
        "Batıkent-1 Kalkış: 08.00"
        + "\n" 
        + "Beytepe Kalkış: 16.00" 
        + "\n" 
        + "Ücret: 40 TL"))
    
    
    ui.textBrowser.setText(ui.comboBox.currentData())
    
    
    deger.setItemData(1, (
        
        "Şoför ve Araç Bilgileri : " 
        + "\n"
        + "Fahri Kalkan"
        + "\n"
        + "0536 953 57 88"
        + "\n"
        + "06 C 7338"
        
    ))
    
    
    deger.setItemData(2, (
        
        "Şoför ve Araç Bilgileri : " 
        + "\n"
        + "Fikret Yıldız"
        + "\n"
        + "0552 232 36 36"
        + "\n"
        + "06 C 7000"
        
    ))
    
    
    deger.setItemData(3, (
        
        "Şoför ve Araç Bilgileri : " 
        + "\n"
        + "Cesur Dizdaroğlu"
        + "\n"
        + "0535 977 37 22"
        + "\n"
        + "06 C 1956"
        
    ))
    
    ui.textBrowser_4.setText(ui.comboBox.currentData())
    
    




#Signals: 

ui.comboBox.currentIndexChanged.connect(SEMTSURE)



#-----------------------END-----------------------------#
#-------------------------------------------------------#

sys.exit(Uygulama.exec_())


