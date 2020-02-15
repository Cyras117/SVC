import tkinter
import tkinter.ttk
import svc

class mScreen(tkinter.Frame):
    #construtor
    def __init__(self,master,screens):
        super().__init__()
        self['bg']='#8a9ec1'

        bTemplete=tkinter.Button(self,
            text='Apenas templete',bg='#5B77A8',activebackground='#4f6996',
            relief='raised',bd=1,
            command= lambda: print('tempconfig')).grid(row=0,column=0,sticky='we')

        sl = tkinter.Label(self,text=' ',bg='#8a9ec1').grid()
        def callScreen(screen):
            self.forget() 
            screen.pack()

        bInfoSettins = tkinter.Button(self,text='Versões de settings',
            bg='#5B77A8',activebackground='#4f6996',relief='raised',
            bd=1,command=lambda: callScreen(screens[0])).grid(row=5,column=0,sticky='we')
        
        sl = tkinter.Label(self,text=' ',bg='#8a9ec1').grid()
        
        bInfoApps = tkinter.Button(self,text='Versões de IC',bg='#5B77A8',activebackground='#4f6996',relief='raised',bd=1).grid(row=10,column=0,sticky='we')
        sl = tkinter.Label(self,text=' ',bg='#8a9ec1').grid()
        bInfoCommon = tkinter.Button(self,text='Versões de MM',bg='#5B77A8',activebackground='#4f6996',relief='raised',bd=1).grid(row=15,column=0,sticky='we')
        sl = tkinter.Label(self,text=' ',bg='#8a9ec1').grid()
        bInfoMm = tkinter.Button(self,text='Versões de Common',bg='#5B77A8',activebackground='#4f6996',relief='raised',bd=1).grid(row=20,column=0,sticky='we')

class sScreen(tkinter.Frame):
    def getMScreen(*args):
        global mSpace 
        mSpace = args
        
    def __init__(self,master):
        super().__init__()
        self['bg']='#8a9ec1'
        def callScreen(mspace):
                self.forget() 
                mspace[1].pack()
        bTemplete=tkinter.Button(self,
            text='Phone',bg='#5B77A8',activebackground='#4f6996',
            relief='raised',bd=1,
            command= lambda: svc.getSettingsInfo(0)).grid(row=50,column=0,sticky='we')
        bTemplete=tkinter.Button(self,
            text='Voltar',bg='#5B77A8',activebackground='#4f6996',
            relief='raised',bd=1,
            command= lambda: callScreen(mSpace)).grid(row=50,column=0,sticky='we')
    

