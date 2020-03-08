import tkinter
import tkinter.ttk
import svc
import style
import json

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
    master.geometry('230x415')
    qch.grid_forget()
    sFrame =  tkinter.Frame()
    sFrame['bg']=style.mainColor()
    def callScreen(mspace):
            master.geometry(style.mainSize())
            sFrame.destroy()
            mspace.grid(row=5)

    p = tkinter.Button(sFrame,
        text='Phone',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('settings','call'))

    m = tkinter.Button(sFrame,
        text='Message',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('settings','message'))

    s = tkinter.Button(sFrame,
        text='Settings',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('settings','settings'))
    
    k = tkinter.Button(sFrame,
        text='Keyboard',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('settings','keyboard'))

    tr = tkinter.Button(sFrame,
        text='3°Party',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('settings','3rdparty_settings'))

    a = tkinter.Button(sFrame,
        text='All',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('settings','all'))

    b = tkinter.Button(sFrame,
        text='Voltar',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: callScreen(qch))

    p.config(width=style.larguraMaxima())
    m.config(width=style.larguraMaxima())
    s.config(width=style.larguraMaxima())
    k.config(width=style.larguraMaxima())
    tr.config(width=style.larguraMaxima())
    a.config(width=style.larguraMaxima())
    b.config(width=style.larguraMaxima())

    p.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()

    m.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()

    s.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()

    k.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()

    tr.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()

    a.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()

    b.grid(row=1000,column=0,sticky='we')

    sFrame.grid(row=5)

def appsScreen(master,qch):
    master.geometry('230x415')
    qch.grid_forget()
    sFrame =  tkinter.Frame()
    sFrame['bg']=style.mainColor()
    def callScreen(mspace):
        master.geometry(style.mainSize())
        sFrame.destroy()
        mspace.grid(row=5)

    w = tkinter.Button(sFrame,
        text='Wearables',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('apps','wearable'))

    s = tkinter.Button(sFrame,
        text='Secure Folder',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('apps','secure_folder'))

    b = tkinter.Button(sFrame,
        text='Bixby',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('apps','bixby'))
    
    f = tkinter.Button(sFrame,
        text='FMM',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('apps','fmm'))

    tr = tkinter.Button(sFrame,
        text='3°Party',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('apps','3rdparty_apps'))

    a = tkinter.Button(sFrame,
        text='All',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('apps','all'))

    bc = tkinter.Button(sFrame,
        text='Voltar',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: callScreen(qch))
    
    w.config(width=style.larguraMaxima())
    s.config(width=style.larguraMaxima())
    b.config(width=style.larguraMaxima())
    f.config(width=style.larguraMaxima())
    tr.config(width=style.larguraMaxima())
    a.config(width=style.larguraMaxima())
    bc.config(width=style.larguraMaxima())

    w.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    s.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    b.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    f.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    tr.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    a.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    bc.grid()

    sFrame.grid(row=5)

def commonScreen(master,qch):
    master.geometry('230x465')
    qch.grid_forget()
    sFrame =  tkinter.Frame()
    sFrame['bg']=style.mainColor()
    def callScreen(mspace):
        master.geometry(style.mainSize())
        sFrame.destroy()
        mspace.grid(row=5)

    s = tkinter.Button(sFrame,
        text='Samsung Cloud',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('common','samsung_cloud'))

    g = tkinter.Button(sFrame,
        text='Galaxy Themes',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('common','galaxy_themes'))

    c = tkinter.Button(sFrame,
        text='Clock/Calculadora',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('common','clock_calculator'))
 
    ss = tkinter.Button(sFrame,
        text='Samsung Pass',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('common','samsung_pass'))

    k = tkinter.Button(sFrame,
        text='Kids Mode',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('common','kids_mode'))

    tr = tkinter.Button(sFrame,
        text='3°Party',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('common','3rdparty_common'))

    a = tkinter.Button(sFrame,
        text='All',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('apps','all'))

    b = tkinter.Button(sFrame,
        text='Voltar',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: callScreen(qch))

    s.config(width=style.larguraMaxima())
    g.config(width=style.larguraMaxima())
    c.config(width=style.larguraMaxima())
    ss.config(width=style.larguraMaxima())
    k.config(width=style.larguraMaxima())
    tr.config(width=style.larguraMaxima())
    a.config(width=style.larguraMaxima())
    b.config(width=style.larguraMaxima())

    s.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()

    g.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()

    c.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    
    ss.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    
    k.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
        
    tr.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()

    a.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()

    b.grid()

    sFrame.grid(row=5)

def mmScreen(master,qch):
    qch.grid_forget()
    sFrame =  tkinter.Frame()
    sFrame['bg']=style.mainColor()
    def callScreen(mspace):
            sFrame.destroy()
            mspace.grid(row=5)

    c = tkinter.Button(sFrame,
        text='Camera',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('mm','camera'))

    s = tkinter.Button(sFrame,
        text='Samsung Members',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('mm','samsung_members'))

    sg = tkinter.Button(sFrame,
        text='Global Goals',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('mm','global_goals'))

    tr = tkinter.Button(sFrame,
        text='3°Party',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('mm','3rdparty_mm'))

    a = tkinter.Button(sFrame,
        text='All',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('mm','all'))

    b = tkinter.Button(sFrame,
        text='Voltar',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: callScreen(qch))

    c.config(width=style.larguraMaxima())
    s.config(width=style.larguraMaxima())
    sg.config(width=style.larguraMaxima())
    tr.config(width=style.larguraMaxima())
    a.config(width=style.larguraMaxima())
    b.config(width=style.larguraMaxima())

    c.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    s.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    sg.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    tr.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    a.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    b.grid()

    sFrame.grid(row=5)

def icScreen(master,qch):
    master.geometry('225x517')
    qch.grid_forget()
    sFrame =  tkinter.Frame()
    sFrame['bg']=style.mainColor()
    def callScreen(mspace):
        master.geometry(style.mainSize())
        sFrame.destroy()
        mspace.grid(row=5)

    d = tkinter.Button(sFrame,
        text='Dual Menseger',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('ic','dual_messenger'))

    g = tkinter.Button(sFrame,
        text='GMS',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('ic','gms'))

    i = tkinter.Button(sFrame,
        text='Internet',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('ic','internet'))
    
    a = tkinter.Button(sFrame,
        text='Accessibility',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('ic','accessibility'))

    gl = tkinter.Button(sFrame,
        text='Game Launcher',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('ic','game_launcher'))

    gt = tkinter.Button(sFrame,
        text='Game Tools',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('ic','game_booster'))

    tr = tkinter.Button(sFrame,
        text='3°Party',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('ic','3rdparty_ic'))

    al = tkinter.Button(sFrame,
        text='All',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: svc.getInfo('ic','all'))

    v = tkinter.Button(sFrame,
        text='Voltar',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command= lambda: callScreen(qch))

    d.config(width=style.larguraMaxima())
    g.config(width=style.larguraMaxima())
    i.config(width=style.larguraMaxima())
    a.config(width=style.larguraMaxima())
    gl.config(width=style.larguraMaxima())
    gt.config(width=style.larguraMaxima())
    tr.config(width=style.larguraMaxima())
    al.config(width=style.larguraMaxima())
    v.config(width=style.larguraMaxima())
    
    d.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    g.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    i.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    a.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    gl.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    gt.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    tr.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    al.grid()
    tkinter.Label(sFrame,text=' ',
        bg=style.mainColor()).grid()
    v.grid()

    sFrame.grid(row=5)

def addScreen(master):
    addFrame = tkinter.Toplevel()
    addFrame.title('Adicionar pacote')
    addFrame.resizable(False,False)
    addFrame.geometry('250x320')
    addFrame['bg'] = style.mainColor()
    #addFrame.iconbitmap('Iconka-Easter-Egg-Bunny-Blue-demon.ico')#verificar
    pkg = tkinter.Entry(addFrame)
    name = tkinter.Entry(addFrame)
    team = tkinter.Entry(addFrame)
    scope = tkinter.Entry(addFrame)

    sep = tkinter.Label(addFrame,text=' ',
        bg=style.mainColor())
    sep.config(width = 30)
    sep.grid(row=5,column=10)

    tkinter.Label(addFrame,text='Pacote:',
    bg=style.mainColor()).grid(row=10,column=10,sticky='w')
    pkg.grid(row=13,column=10,sticky='we')

    tkinter.Label(addFrame,text=' ',
    bg=style.mainColor()).grid(row=15,column=10,sticky='w')

    tkinter.Label(addFrame,text='Nome:',
    bg=style.mainColor()).grid(row=20,column=10,sticky='w')
    name.grid(row=23,column=10,sticky='we')

    tkinter.Label(addFrame,text=' ',
    bg=style.mainColor()).grid(row=25,column=10,sticky='w')

    tkinter.Label(addFrame,text='Time:',
    bg=style.mainColor()).grid(row=30,column=10,sticky='w')
    team.grid(row=33,column=10,sticky='we')

    tkinter.Label(addFrame,text=' ',
    bg=style.mainColor()).grid(row=35,column=10,sticky='w')

    tkinter.Label(addFrame,text='Item:',
    bg=style.mainColor()).grid(row=40,column=10,sticky='w')
    scope.grid(row=43,column=10,sticky='we')

    tkinter.Label(addFrame,text=' ',
    bg=style.mainColor()).grid(row=45,column=10,sticky='we')
    
    def clear():
        pk = pkg.get()
        na = name.get()
        ta = team.get().lower()
        sc = scope.get().lower()
        pkg.delete(0,300)
        name.delete(0,300)
        team.delete(0,300)
        scope.delete(0,300)

        if(pk == '' or na == '' or ta == '' or sc=='' or ' ' in pk):
            tkinter.messagebox.showinfo('Aviso','Erro no pacote informado!!')
            return
        tkinter.messagebox.showinfo('Aviso',svc.addPkg(pk,na,ta,sc))

    tkinter.Button(addFrame,
        text='Adicionar',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),
        command=clear).grid(row=50,column=10,sticky='we')

def rmScreen(master):
    rmFrame = tkinter.Toplevel()
    rmFrame.title('Remover pacote')
    rmFrame.resizable(False,False)
    rmFrame.geometry('230x230')
    rmFrame['bg'] = style.mainColor()
    #rmFrame.iconbitmap('Iconka-Easter-Egg-Bunny-Blue-demon.ico')#verificar
    pkg = tkinter.Entry(rmFrame)
    team = tkinter.Entry(rmFrame)

    sep = tkinter.Label(rmFrame,text=' ',
    bg=style.mainColor())
    sep.config(width = 28)
    sep.grid(row=5,column=10)

    tkinter.Label(rmFrame,text='Pacote:',
    bg=style.mainColor()).grid(row=10,column=10,sticky='w')
    pkg.grid(row=13,column=10,sticky='we')

    tkinter.Label(rmFrame,text=' ',
    bg=style.mainColor()).grid(row=15,column=10,sticky='we')

    tkinter.Label(rmFrame,text='Time:',
    bg=style.mainColor()).grid(row=20,column=10,sticky='w')
    team.grid(row=23,column=10,sticky='we')

    tkinter.Label(rmFrame,text=' ',
    bg=style.mainColor()).grid(row=25,column=10,sticky='we')
    
    def clear():
        pk = pkg.get()
        ta = team.get().lower()
        pkg.delete(0,300)
        team.delete(0,300)

        if(pk == '' or ta == '' or ' ' in pk):
            tkinter.messagebox.showinfo('Aviso','Erro no pacote informado!!')
            return
        tkinter.messagebox.showinfo('Aviso',svc.rmPkg(pk,ta))

    tkinter.Button(rmFrame,
        text='Remover',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),
        command=clear).grid(row=50,column=10,sticky='we')

def mFrame(master):
    mFrame = tkinter.Frame()
    mFrame['bg']=style.mainColor()
    btemp = tkinter.Button(mFrame,
        text='Template',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),
        relief='raised',command=lambda: svc.wrap('abrir'))

    bsettings = tkinter.Button(mFrame,text='Settings',
        bg=style.backGroundButtonColor(),activebackground=style.activeBackGroundButtonColor(),
        relief='raised',command=lambda: settingsScreen(master,mFrame))

    bapps = tkinter.Button(mFrame,text='Apps',
        bg=style.backGroundButtonColor(),activebackground=style.activeBackGroundButtonColor(),
        relief='raised',command=lambda: appsScreen(master,mFrame))

    bic = tkinter.Button(mFrame,text='IC',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command=lambda: icScreen(master,mFrame))

    bmm = tkinter.Button(mFrame,text='MM',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command=lambda: mmScreen(master,mFrame))

    bcommon = tkinter.Button(mFrame,text='Common',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),relief='raised',
        command=lambda: commonScreen(master,mFrame))

    sanity = tkinter.Button(mFrame,text='Sanity',bg=style.backGroundButtonColor(),
        activebackground=style.activeBackGroundButtonColor(),
        command=lambda: svc.getInfo('all','sanity'))

    btemp.config(width=10)
    bsettings.config(width=10)
    bapps.config(width=10)
    bic.config(width=10)
    bmm.config(width=10)
    bcommon.config(width=10)
    sanity.config(width=10)

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
    tkinter.Label(mFrame,text=' ',bg=style.mainColor()).grid()
    sanity.grid()

    return mFrame
  