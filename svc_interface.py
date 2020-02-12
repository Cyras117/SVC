from tkinter import messagebox
import mainscreen
import tkinter
#import svc // falta terminar as funçoẽs


#Definindo tela principal
mainScreen = tkinter.Tk()
mainScreen.title('SVC')
mainScreen.resizable(False,False)
#mainScreen.iconbitmap('Iconka-Easter-Egg-Bunny-Blue-demon.ico')//verificar



#Funçẽs
def configi():
    print('config.templet')#Configuração de templete
def ajudaMenu():
    messagebox.showinfo('Ajuda','Duvidas e sugestões:\nalexsandro.a\nkledyson.f')

#Menu_Bar
menubar = tkinter.Menu(mainScreen)
menubar.add_command(label='Conf. templete', command=lambda: configi())
menubar.add_command(label='Ajuda', command=lambda: ajudaMenu())

#Frame_Menu_Principal
mSpace = mainscreen.mScreen(mainScreen)
#sSpace
#mSpace
#aSpace
#cSpace

mSpace.pack()

#Main_loop
mainScreen.config(menu=menubar)
mainScreen.mainloop()