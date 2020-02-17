import tkinter
import tkinter.ttk
import svc

def settingsScreen(master,qch):
    qch.forget()
    sFrame =  tkinter.Frame()
    sFrame['bg']='#8a9ec1'
    def callScreen(mspace):
            sFrame.destroy() 
            mspace.pack()
    tkinter.Button(sFrame,
        text='Phone',bg='#5B77A8',activebackground='#4f6996',
        relief='raised',bd=1,
        command= lambda: svc.getSettingsInfo(0)).grid(row=60,column=0,sticky='we')
    tkinter.Button(sFrame,
        text='Voltar',bg='#5B77A8',activebackground='#4f6996',
        relief='raised',bd=1,
        command= lambda: callScreen(qch)).grid(row=50,column=0,sticky='we')
    sFrame.pack()


def mFrame(master):
    mFrame = tkinter.Frame()
    mFrame['bg']='#8a9ec1'
    tkinter.Button(mFrame,
        text='Apenas templete',bg='#5B77A8',activebackground='#4f6996',
        relief='raised',bd=1,
        command= lambda: print('tempconfig')).grid(row=0,column=0,sticky='we')

    tkinter.Label(mFrame,text=' ',bg='#8a9ec1').grid()

    tkinter.Button(mFrame,text='Versões de settings',
        bg='#5B77A8',activebackground='#4f6996',relief='raised',
        bd=1,command=lambda: settingsScreen(master,mFrame)).grid(row=5,column=0,sticky='we')
    
    tkinter.Label(mFrame,text=' ',bg='#8a9ec1').grid()
    
    tkinter.Button(mFrame,text='Versões de IC',bg='#5B77A8',activebackground='#4f6996',relief='raised',bd=1).grid(row=10,column=0,sticky='we')
    tkinter.Label(mFrame,text=' ',bg='#8a9ec1').grid()
    tkinter.Button(mFrame,text='Versões de MM',bg='#5B77A8',activebackground='#4f6996',relief='raised',bd=1).grid(row=15,column=0,sticky='we')
    tkinter.Label(mFrame,text=' ',bg='#8a9ec1').grid()
    tkinter.Button(mFrame,text='Versões de Common',bg='#5B77A8',activebackground='#4f6996',relief='raised',bd=1).grid(row=20,column=0,sticky='we')
    mFrame.pack()
  

def tempConfigScreen():
        tt = tkinter.Toplevel()
        tt.title('Config. de Templet')
        tt.resizable(False,False)
        tt.geometry('250x300')
        tt['bg'] = '#8a9ec1'

        tkinter.Button(tt,text='Salvar',command= lambda:tt.destroy()).pack()
        
