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
    configdata = svc.loadConfigFile()

    def updateConfigFile():    
        if(id.get()):
            configdata['temp']['id'] = True
        else:
            configdata['temp']['id'] = False
        if(qtd_pass.get()):
            configdata['temp']['pass'] = True
        else:
            configdata['temp']['pass'] = False
        if(model.get()):
            configdata['temp']['model'] = True
        else:
            configdata['temp']['model'] = False
        if(os.get()):
            configdata['temp']['os'] = True
        else:
            configdata['temp']['os'] = False
        if(binary.get()):
            configdata['temp']['binary'] = True
        else:
            configdata['temp']['binary'] = False
        if(csc.get()):
            configdata['temp']['csc'] = True
        else:
            configdata['temp']['csc'] = False
        if(carriers.get()):
            configdata['temp']['carriers'] = True
        else:
            configdata['temp']['carriers'] = False
        if(accounts.get()):
            configdata['temp']['accounts'] = True
        else:
            configdata['temp']['accounts'] = False
        if(issues.get()):
            configdata['temp']['issues'] = True
        else:
            configdata['temp']['issues'] = False

        with open('config.json','w') as config:
            json.dump(configdata,config)

    cid = tkinter.Checkbutton(ttFrame,text='ID',variable=id,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= updateConfigFile)
    
    cpass = tkinter.Checkbutton(ttFrame,text='PASS',variable=qtd_pass,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= updateConfigFile)

    cmodel = tkinter.Checkbutton(ttFrame,text='MODELO',variable=model,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= updateConfigFile)

    cos = tkinter.Checkbutton(ttFrame,text='OS',variable=os,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= updateConfigFile)
    
    cbinary = tkinter.Checkbutton(ttFrame,text='VERSÃO',variable=binary,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= updateConfigFile)

    ccsc = tkinter.Checkbutton(ttFrame,text='CSC',variable=csc,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= updateConfigFile)

    ccarriers = tkinter.Checkbutton(ttFrame,text='CHIPS',variable=carriers,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= updateConfigFile)

    ccontas = tkinter.Checkbutton(ttFrame,text='CONTAS',variable=accounts,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= updateConfigFile)

    cissue = tkinter.Checkbutton(ttFrame,text='ISSUES',variable=issues,
    bg=style.mainColor(),activebackground=style.mainColor(),
    onvalue=True, offvalue=False,justify='left',
    command= updateConfigFile)

    if(configdata['temp']['id']):
        cid.select()
    
    if(configdata['temp']['pass']):
        cpass.select()
    if(configdata['temp']['model']):
        cmodel.select()
    if(configdata['temp']['os']):
        cos.select()
    if(configdata['temp']['binary']):
        cbinary.select()
    if(configdata['temp']['csc']):
        ccsc.select()
    if(configdata['temp']['id']):
        cid.select()
    if(configdata['temp']['carriers']):
        ccarriers.select()
    if(configdata['temp']['accounts']):
        ccontas.select()
    if(configdata['temp']['issues']):
        cissue.select()

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
        command= lambda: svc.getInfo('settings','call')).grid(row=60,column=0,sticky='we')

    tkinter.Label(sFrame,text=' ',
    bg=style.mainColor()).grid(row=70,column=0,sticky='we')

    tkinter.Button(sFrame,
        text='Message',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('settings','message')).grid(row=80,column=0,sticky='we')

    tkinter.Label(sFrame,text=' ',
    bg=style.mainColor()).grid(row=90,column=0,sticky='we')

    tkinter.Button(sFrame,
        text='Settings',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('settings','settings')).grid(row=100,column=0,sticky='we')

    tkinter.Label(sFrame,text=' ',
    bg=style.mainColor()).grid(row=110,column=0,sticky='we')
    
    tkinter.Button(sFrame,
        text='Keyboard',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('settings','keyboard')).grid(row=120,column=0,sticky='we')

    tkinter.Label(sFrame,text=' ',
    bg=style.mainColor()).grid(row=130,column=0,sticky='we')

    tkinter.Button(sFrame,
        text='3°Party',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('settings','3rdparty_settings')).grid(row=140,column=0,sticky='we')

    tkinter.Label(sFrame,text=' ',
    bg=style.mainColor()).grid(row=150,column=0,sticky='we')

    tkinter.Button(sFrame,
        text='All',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('settings','all')).grid(row=160,column=0,sticky='we')

    tkinter.Label(sFrame,text=' ',
    bg=style.mainColor()).grid(row=170,column=0,sticky='we')

    tkinter.Button(sFrame,
        text='Voltar',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: callScreen(qch)).grid(row=1000,column=0,sticky='we')

    sFrame.grid(row=5)

def icScreen(master,qch):
    qch.grid_forget()
    sFrame =  tkinter.Frame()
    sFrame['bg']=style.mainColor()
    def callScreen(mspace):
            sFrame.destroy()
            mspace.grid(row=5)

    tkinter.Button(sFrame,
        text='Dual Menseger',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('settings','call')).grid(row=60,column=0,sticky='we')

    tkinter.Label(sFrame,text=' ',
    bg=style.mainColor()).grid(row=70,column=0,sticky='we')

    tkinter.Button(sFrame,
        text='Message',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('settings','message')).grid(row=80,column=0,sticky='we')

    tkinter.Label(sFrame,text=' ',
    bg=style.mainColor()).grid(row=90,column=0,sticky='we')

    tkinter.Button(sFrame,
        text='Settings',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('settings','settings')).grid(row=100,column=0,sticky='we')

    tkinter.Label(sFrame,text=' ',
    bg=style.mainColor()).grid(row=110,column=0,sticky='we')
    
    tkinter.Button(sFrame,
        text='Keyboard',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('settings','keyboard')).grid(row=120,column=0,sticky='we')

    tkinter.Label(sFrame,text=' ',
    bg=style.mainColor()).grid(row=130,column=0,sticky='we')

    tkinter.Button(sFrame,
        text='3°Party',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('settings','3rdparty_settings')).grid(row=140,column=0,sticky='we')

    tkinter.Label(sFrame,text=' ',
    bg=style.mainColor()).grid(row=150,column=0,sticky='we')

    tkinter.Button(sFrame,
        text='All',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('settings','all')).grid(row=160,column=0,sticky='we')

    tkinter.Label(sFrame,text=' ',
    bg=style.mainColor()).grid(row=170,column=0,sticky='we')

    tkinter.Button(sFrame,
        text='Voltar',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: callScreen(qch)).grid(row=1000,column=0,sticky='we')

    sFrame.grid(row=5)


def mFrame(master):
    mFrame = tkinter.Frame()
    mFrame['bg']=style.mainColor()
    btemp = tkinter.Button(mFrame,
        text='Template',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),
        relief='raised',command= svc.wrap)

    bsettings = tkinter.Button(mFrame,text='Settings',
        bg=style.backGroundButtonColor(),activebackground=style.activeBackGroundButtonColor(),
        relief='raised',command=lambda: settingsScreen(master,mFrame))

    bapps = tkinter.Button(mFrame,text='Apps',
        bg=style.backGroundButtonColor(),activebackground=style.activeBackGroundButtonColor(),
        relief='raised')

    bic = tkinter.Button(mFrame,text='IC',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command=lambda: icScreen(master,mFrame))

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
  
