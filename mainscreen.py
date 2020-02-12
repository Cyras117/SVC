import tkinter

class mScreen(tkinter.Frame):
    def __init__(self,master):
        super().__init__()
        self['bg'] = '#5B77A8'
        bTemplete=tkinter.Button(self,text='Apenas templete',bg='#5B77A8',activebackground='#4f6996',relief='raised',bd=1).grid(row=0,column=0,sticky='we')
        bInfoSettins = tkinter.Button(self,text='Versões de settings',bg='#5B77A8',activebackground='#4f6996',relief='raised',bd=1).grid(row=1,column=0,sticky='we')
        bInfoApps = tkinter.Button(self,text='Versões de IC',bg='#5B77A8',activebackground='#4f6996',relief='raised',bd=1).grid(row=2,column=0,sticky='we')
        bInfoCommon = tkinter.Button(self,text='Versões de MM',bg='#5B77A8',activebackground='#4f6996',relief='raised',bd=1).grid(row=3,column=0,sticky='we')
        bInfoMm = tkinter.Button(self,text='Versões de Common',bg='#5B77A8',activebackground='#4f6996',relief='raised',bd=1).grid(row=4,column=0,sticky='we')





