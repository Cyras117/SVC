import tkinter
import tkinter.ttk
import svc
import json
import style

def tempConfigScreen(master):
    ttFrame = tkinter.Frame(master)
    ttFrame['bg']= style.mainColor()
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

    def createConfigFile(item=None,value=None):
        configdata = svc.checkConfigFile()
        if(item == None and value == None):
            if(id.get()):
                configdata['tempConfig'][0]['id'] = True
            else:
                configdata['tempConfig'][0]['id'] = False
            if(qtd_pass.get()):
                configdata['tempConfig'][0]['pass'] = True
            else:
                configdata['tempConfig'][0]['pass'] = False
            if(model.get()):
                configdata['tempConfig'][0]['model'] = True
            else:
                configdata['tempConfig'][0]['model'] = False
            if(os.get()):
                configdata['tempConfig'][0]['os'] = True
            else:
                configdata['tempConfig'][0]['os'] = False
            if(binary.get()):
                configdata['tempConfig'][0]['binary'] = True
            else:
                configdata['tempConfig'][0]['binary'] = False
            if(csc.get()):
                configdata['tempConfig'][0]['csc'] = True
            else:
                configdata['tempConfig'][0]['csc'] = False
            if(carriers.get()):
                configdata['tempConfig'][0]['carriers'] = True
            else:
                configdata['tempConfig'][0]['carriers'] = False
            if(accounts.get()):
                configdata['tempConfig'][0]['accounts'] = True
            else:
                configdata['tempConfig'][0]['accounts'] = False
            if(issues.get()):
                configdata['tempConfig'][0]['issues'] = True
            else:
                configdata['tempConfig'][0]['issues'] = False
        else:
            configdata['tempConfig'][0][item] = value
        with open('config.json','w') as config:
            json.dump(configdata,config)

    cid = tkinter.Checkbutton(ttFrame,text='ID',variable=id,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= createConfigFile)
    
    cpass = tkinter.Checkbutton(ttFrame,text='PASS',variable=qtd_pass,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= createConfigFile)

    cmodel = tkinter.Checkbutton(ttFrame,text='MODELO',variable=model,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= createConfigFile)

    cos = tkinter.Checkbutton(ttFrame,text='OS',variable=os,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= createConfigFile)
    
    cbinary = tkinter.Checkbutton(ttFrame,text='VERSÃO',variable=binary,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= createConfigFile)

    ccsc = tkinter.Checkbutton(ttFrame,text='CSC',variable=csc,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= createConfigFile)

    ccarriers = tkinter.Checkbutton(ttFrame,text='CHIP',variable=carriers,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= createConfigFile)

    ccontas = tkinter.Checkbutton(ttFrame,text='CONTAS',variable=accounts,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= createConfigFile)

    cissue = tkinter.Checkbutton(ttFrame,text='ISSUES',variable=issues,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= createConfigFile)

    cid.grid(row=0,column=0,sticky='w')
    cpass.grid(row=0,column=1,sticky='w')
    cmodel.grid(row=0,column=2,sticky='w')
    cos.grid(row=1,column=0,sticky='w')
    cbinary.grid(row=1,column=1,sticky='w')
    ccsc.grid(row=1,column=2,sticky='w')
    ccarriers.grid(row=2,column=0,sticky='w')
    ccontas.grid(row=2,column=1,sticky='w')
    cissue.grid(row=2,column=2,sticky='w')

    return ttFrame

def settingsScreen(master,qch):
    qch.grid_forget()
    sFrame =  tkinter.Frame()
    sFrame['bg']=style.mainColor()
    def callScreen(mspace):
            sFrame.destroy()
            mspace.grid(row=5)
    tkinter.Button(sFrame,
        text='Phone',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getSettingsInfo(0)).grid(row=60,column=0,sticky='we')
    
    tkinter.Label(sFrame,text=' ',
    bg=style.mainColor()).grid(row=70,column=0,sticky='we')
    
    tkinter.Button(sFrame,
        text='Voltar',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: callScreen(qch)).grid(row=80,column=0,sticky='we')

    sFrame.grid(row=5)

def mFrame(master):
    mFrame = tkinter.Frame()
    mFrame['bg']=style.mainColor()
    btemp = tkinter.Button(mFrame,
        text='Template',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),
        relief='raised',bd=1)

    bsettings = tkinter.Button(mFrame,text='Settings',
        bg=style.backGroundButtonColor(),activebackground=style.activeBackGroundButtonColor(),
        relief='raised',command=lambda: settingsScreen(master,mFrame))
    bapps = tkinter.Button(mFrame,text='Settings',
        bg=style.backGroundButtonColor(),activebackground=style.activeBackGroundButtonColor(),
        relief='raised')

    bic = tkinter.Button(mFrame,text='IC',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised')

    bmm = tkinter.Button(mFrame,text='MM',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised')

    bcommon = tkinter.Button(mFrame,text='Common',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised')

    btemp.config(width=10)
    bsettings.config(width=10)
    bapps.config(width=10)
    bic.config(width=10)
    bmm.config(width=10)
    bcommon.config(width=10)

    btemp.grid()
    tkinter.Label(mFrame,text=' ',bg=style.mainColor()).grid()
    bsettings.grid()
    tkinter.Label(mFrame,text=' ',bg=style.mainColor()).grid()
    bapps.grid()
    tkinter.Label(mFrame,text=' ',bg=style.mainColor()).grid()
    bic.grid()
    tkinter.Label(mFrame,text=' ',bg=style.mainColor()).grid()
    bmm.grid()
    tkinter.Label(mFrame,text=' ',bg=style.mainColor()).grid()
    bcommon.grid()
    return mFrame
  
