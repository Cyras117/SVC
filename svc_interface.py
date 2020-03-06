from tkinter import messagebox
import screens
import tkinter
import tkinter.ttk
import style
import svc
 
#Setupadb
svc.setADB()
#loadingConfigFile
svc.loadConfigFile()
#Definindo tela principal
mainScreen = tkinter.Tk()
mainScreen.title('SVC')
mainScreen.resizable(False,False)
mainScreen.geometry('225x365')
mainScreen['bg'] = style.mainColor()
#mainScreen.iconbitmap('Iconka-Easter-Egg-Bunny-Blue-demon.ico')#verificar
tempMenu = screens.tempConfigScreen(mainScreen)
mScreen = screens.mFrame(mainScreen)
#Funçẽs
def ajudaMenu():
    messagebox.showinfo('Ajuda','Duvidas e sugestões:\nalexsandro.a\nkledyson.f')

#Menu_Bar
menubar = tkinter.Menu(mainScreen)
configmenu = tkinter.Menu(menubar,tearoff=0)

tempMenuState = tkinter.BooleanVar()
def showHide():
    if(tempMenuState.get()):
        tempMenu.grid(row=0,sticky='w')
        mainScreen.geometry('225x425')
    else:
        mainScreen.geometry('225x365')
        tempMenu.grid_forget()

sep = tkinter.Frame(mainScreen,bg=style.mainColor())
sep.config(width=225)
sep.grid(row=1)

mScreen.grid(row=5)

configmenu.add_checkbutton(label='Connfig. Templat',variable=tempMenuState,
onvalue=True,offvalue=False,command=showHide)

menubar.add_cascade(label='Config.',menu=configmenu)
menubar.add_command(label='Ajuda', command=ajudaMenu)

#mSpace
#aSpace
#cSpace

#Main_loop
mainScreen.config(menu=menubar)
mainScreen.mainloop()
