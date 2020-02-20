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
    
    tkinter.Label(sFrame,text=' ',bg='#8a9ec1').grid(row=70,column=0,sticky='we')
    
    tkinter.Button(sFrame,
        text='Voltar',bg='#5B77A8',activebackground='#4f6996',
        relief='raised',bd=1,
        command= lambda: callScreen(qch)).grid(row=80,column=0,sticky='we')
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
        tt.geometry('230x150')
        tt['bg'] = '#8a9ec1'
        ttFrame = tkinter.Frame(tt)
        ttFrame['bg']='#8a9ec1'
        #Vars
        id = tkinter.BooleanVar()
        qtd_pass = tkinter.BooleanVar()
        model = tkinter.BooleanVar()
        os = tkinter.BooleanVar()
        binary = tkinter.BooleanVar()
        csc = tkinter.BooleanVar()
        carriers = tkinter.BooleanVar()
        accounts = tkinter.BooleanVar()
        issues = tkinter.BooleanVar()

        #Functions
        def createConfigFile():
            with open('tempconfig.txt','w') as f:
                if(id.get()):
                    f.write('ID:True\n')
                else:
                    f.write('ID:False\n')
                if(qtd_pass.get()):
                    f.write('Pass:True\n')
                else:
                    f.write('Pass:False\n')
                if(model.get()):
                    f.write('Model:True\n')
                else:
                    f.write('Model:False\n')
                if(os.get()):
                    f.write('Os:True\n')
                else:
                    f.write('Os:False\n')
                if(binary.get()):
                    f.write('Binary:True\n')
                else:
                    f.write('Binary:False\n')
                if(csc.get()):
                    f.write('CSC:True\n')
                else:
                    f.write('CSC:False\n')
                if(carriers.get()):
                    f.write('Carriers:True\n')
                else:
                    f.write('Carriers:False\n')
                if(accounts.get()):
                    f.write('Accounts:True\n')
                else:
                    f.write('Accounts:False\n')
                if(issues.get()):
                    f.write('Issues:True\n')
                else:
                    f.write('Issues:False\n')

        def salvar():
            createConfigFile()
            tt.destroy()

        tkinter.Checkbutton(ttFrame,text='Id',variable=id,
        bg='#8a9ec1',activebackground='#8a9ec1',
        onvalue=True, offvalue=False).grid(row=10,column=10,sticky='W')
        
        tkinter.Checkbutton(ttFrame,text='Pass',variable=qtd_pass,
        bg='#8a9ec1',activebackground='#8a9ec1',
        onvalue=True, offvalue=False).grid(row=10,column=20,sticky='w')

        tkinter.Checkbutton(ttFrame,text='Modelo',variable=model,
        bg='#8a9ec1',activebackground='#8a9ec1',
        onvalue=True, offvalue=False).grid(row=10,column=30,sticky='w')

        tkinter.Checkbutton(ttFrame,text='Os',variable=os,
        bg='#8a9ec1',activebackground='#8a9ec1',
        onvalue=True, offvalue=False).grid(row=20,column=10,sticky='w')
        
        tkinter.Checkbutton(ttFrame,text='Versão',variable=binary,
        bg='#8a9ec1',activebackground='#8a9ec1',
        onvalue=True, offvalue=False).grid(row=20,column=20,sticky='w')

        tkinter.Checkbutton(ttFrame,text='CSC',variable=csc,
        bg='#8a9ec1',activebackground='#8a9ec1',
        onvalue=True, offvalue=False).grid(row=20,column=30,sticky='w')

        tkinter.Checkbutton(ttFrame,text='Chip',variable=carriers,
        bg='#8a9ec1',activebackground='#8a9ec1',
        onvalue=True, offvalue=False).grid(row=30,column=10,sticky='w')

        tkinter.Checkbutton(ttFrame,text='Contas',variable=accounts,
        bg='#8a9ec1',activebackground='#8a9ec1',
        onvalue=True, offvalue=False).grid(row=30,column=20,sticky='w')

        tkinter.Checkbutton(ttFrame,text='Issues',variable=issues,
        bg='#8a9ec1',activebackground='#8a9ec1',
        onvalue=True, offvalue=False).grid(row=30,column=30,sticky='w')
        
        tkinter.Label(ttFrame,text=' ',bg='#8a9ec1').grid(row=45,column=1,sticky='we')
        tkinter.Button(ttFrame,text='Salvar',bg='#5B77A8',
        activebackground='#4f6996',relief='raised',
        bd=1,command= lambda:salvar()).grid(row=50,column=20,sticky='we')

        ttFrame.pack()
        
