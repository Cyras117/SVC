from tkinter import messagebox
import screens
import tkinter
import tkinter.ttk
import svc #falta terminar as funçoẽs


#Definindo tela principal
mainScreen = tkinter.Tk()
mainScreen.title('SVC')
mainScreen.resizable(False,False)
mainScreen.geometry('250x300')
mainScreen['bg'] = '#8a9ec1'
#mainScreen.iconbitmap('Iconka-Easter-Egg-Bunny-Blue-demon.ico')#verificar

#Funçẽs
def configi():
    print('config.templet')#Configuração de templete
def ajudaMenu():
    messagebox.showinfo('Ajuda','Duvidas e sugestões:\nalexsandro.a\nkledyson.f')

#Menu_Bar
menubar = tkinter.Menu(mainScreen)
configmenu = tkinter.Menu(menubar,tearoff=0)
configmenu.add_command(label='Connfig. Templet',command=lambda: screens.tempConfigScreen())
menubar.add_cascade(label='Config.',menu=configmenu)
menubar.add_command(label='Ajuda', command=lambda: ajudaMenu())


#Gerenciando_Telas
screens.mFrame(mainScreen)

#mSpace
#aSpace
#cSpace

#Main_loop
mainScreen.config(menu=menubar)
mainScreen.mainloop()