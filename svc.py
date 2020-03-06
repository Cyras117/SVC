import json
import subprocess
import tkinter
import os
import time
import pathlib
import jsb
from tkinter import messagebox

def addPkg(name,pkg,teams,scopes):
    x = {
        "pkg":pkg,
        "name":name,
        "scope":{
            "teams":teams,
            "inscope":teams
        }
    }
    jsb.setData(x)

def rmPkg(pkg):
    jsb.rmData(pkg)

def setADB():#Checar no win adb tem q ta no folder 
    os.putenv('PATH',str(pathlib.Path().absolute()))

def getCarriers():
    carriers = subprocess.check_output(['adb','shell','getprop','gsm.sim.operator.alpha'],text=True)
    carriers = carriers.split('\n')[0]
    carriers = carriers.split(',')
    if(len(carriers)>1):        
        if(carriers[0] == '' and carriers[1]==''):
            return 'Carriers:'
        if(carriers[0] != '' and carriers[1]!=''):
            return 'Carriers:'+carriers[0]+','+carriers[1]
        if(carriers[0] != '' or carriers[1]!=''):
            if(carriers[0] != ''):
                return 'Carrier:'+carriers[0]
            else:
                return 'Carrier:'+carriers[1]
    else:
        return 'Carrier:'+carriers[0]

def getModel():
    model = subprocess.check_output(['adb','shell','getprop','ro.product.model'],text=True)
    scode = subprocess.check_output(['adb','shell','getprop','ro.csc.sales_code'],text=True)
    return "Model: "+model[:-1]+" ["+scode[:-1]+"]"

def getOS():
    os = subprocess.check_output(['adb','shell','getprop','ro.build.version.release'],text=True)
    return "Android Version: "+os[:-1]

def extractAccount(aString):
    accounts = list()
    accountsA = list()
    accounts.append('Accouts:\n')
    acString = aString.find('Accounts:')
    acStart = aString.find('\n',acString)+5
    acEnd = aString.find('AccountId')-6
    acString = aString[acStart:acEnd]
    acString = acString.split('\n')
    for ac in acString :
        if('com.google' in ac and not('Duo' in ac)):
            accountPosI = ac.find('name=')+5
            accountPosF = ac.find(',')
            account = ac[accountPosI:accountPosF]
            accountsA.append("Google: "+account)

        if('com.osp.app.signin' in ac):
            accountPosI = ac.find('name=')+5
            accountPosF = ac.find(',')
            account = ac[accountPosI:accountPosF]
            accountsA.append("Samsung: "+account)
    for ac in accountsA :
        accounts.append(ac+'\n') 
    return accounts

def getAccounts():
        aString = subprocess.check_output(['adb','shell','dumpsys','account'],text=True)
        tc = aString.find('Accounts:')+10
        if((tc == 1)or('com.google' in aString)or('com.osp.app.signin' in aString)):
            return extractAccount(aString)
        else:
            return ["Accounts: \n"]

def getBinary():
    '''bl = subprocess.check_output(['adb','shell','getprop',
        'ro.bootloader'],text=True)
    '''
    ap = subprocess.check_output(['adb','shell','getprop'
        ,'ro.build.version.incremental'],text=True)
    cp = subprocess.check_output(['adb','shell','getprop'
        ,'ril.sw_ver'],text=True)
    csc = subprocess.check_output(['adb','shell','getprop'
        ,'ril.official_cscver'],text=True)

    return "Binary:["+ap[:-1]+"/"+cp[:-1]+"/"+csc[:-1]+"]"

def getCSC():
    csc = subprocess.check_output(['adb','shell','getprop'
        ,'ril.official_cscver'],text=True)
    csc = csc[:-6][-3:]
    return "CSC: "+csc

def getAppVersion(pName,Name):
        pkgv = subprocess.check_output(['adb','shell','dumpsys','package',pName,'|','grep','versionName'],text=True)
        versionPosI = pkgv.find('=')+1
        versionPosF = pkgv.find('\n',versionPosI-1)
        version = pkgv[versionPosI:versionPosF]
        if(len(version)>2):
            return Name+': '+version+'\n'
        else:
            return ''

def createDefaultConfigFile():
    data = jsb.data

    with open('config.json','w') as config:
         json.dump(data,config)
    return data

def loadConfigFile():
    try:
        with open('config.json','r') as config:
            configdata = json.load(config)
            return configdata
    except:
            configdata = createDefaultConfigFile()
            return configdata

def checkPhone():
    while(True):
        subprocess.run(['adb','start-server'])
        var = subprocess.check_output(['adb','devices'],text=True)
        time.sleep(1)
        if(var.split('\n')[1] != ''):
            if('device' in var.split('\n')[1]):
                break
            else:
                messagebox.showinfo('Aviso','Dispositivo não autorizado!!')
                subprocess.run(['adb','kill-server'])
                subprocess.run(['adb','start-server'])
        else:
            messagebox.showinfo('Aviso','Nenhum dispositivo conectado!!')     
            subprocess.run(['adb','kill-server'])
            subprocess.run(['adb','start-server'])

def deleteVersionsFile():
    try:
        os.remove('Versions.txt')
    except OSError:
        pass

def fileOpen():
    os.system('Versions.txt')#verificar encerrar o sub processo
    #subprocess.run(['notepad','Versions.txt'])

def wrap():
    checkPhone()
    temp = list()
    data = loadConfigFile()["temp"]
    deleteVersionsFile()

    if(data['id']):
        temp.append('ID:\n')
    if(data['pass']):
        temp.append('PASS:\n')
    if(data['issues']):
        temp.append('ISSUES:\n')
    if(data['model']):
        temp.append(getModel()+'\n')
    if(data['os']):
        temp.append(getOS()+'\n')
    if(data['csc']):
        temp.append(getCSC()+'\n')
    if(data['binary']):
        temp.append(getBinary()+'\n')
    if(data['carriers']):
        temp.append(getCarriers()+'\n')
    if(data['accounts']):
        acs = getAccounts()
        for ac in acs :
            temp.append(ac)

    with open('Versions.txt','w') as v:
        v.writelines(temp)

def getInfo(time,scope):
    wrap()
    data = loadConfigFile()
    lp = list()
    for p in data["pkgs"]:
        if(time in p["scope"]["teams"]):
            if(scope in p["scope"]["inscope"]):
                lp.append(getAppVersion(p["pkg"],p["name"]))
    with open('Versions.txt','a') as v:
        v.write('\nVersions:\n')
        v.writelines(lp)
