#!/usr/bin/python3.8
import subprocess;

def extractSim(stC):
    stCStart = stC.find('displayName=')+12;
    stCEnd = stC.find('carrierName',stCStart);
    carrier = stC[stCStart:stCEnd-1];
    return carrier

def getCarriers():
    isub = subprocess.check_output(['adb','shell','dumpsys','isub'],text = True);
    isubStart = isub.find('ActiveSubInfoList:')+18;
    isubEnd =isub.find('++++++++++++++++++++++++++++++++',isubStart);
    if((isubEnd - isubStart) == 1 ):
        return "Carrier: "
    
    if((isubEnd - isubStart) < 600):
        #apenas 1 carrier
        carrier = extractSim(isub[isubStart+1:(isubEnd - isubStart)]);
        return "Carrier: "+carrier
    else:
        #2 carriers
        stC = isub[isubStart+1:(isubEnd - isubStart)];
        arC = stC.split('\n');
        s1 = extractSim(arC[0]);
        s2 = extractSim(arC[1]);
        return "Carriers: "+s1+", "+s2

def filtraStringDeProcesso(bi):
    st = str(bi)
    st = st.split("'")[1]
    st = st.split("\\")[0]
    return st

def getModel():
    model = subprocess.check_output(['adb','shell','getprop','ro.product.model'],text=True);
    return "Model: "+model[:-1];

def getOS():
    os = subprocess.check_output(['adb','shell','getprop','ro.build.version.release'],text=True);
    return "Android Version: "+os[:-1];

def extractAccount(aString):
    accountsA = [];
    accounts = "Accounts:\n";
    acString = aString.find('Accounts:');
    acStart = aString.find('\n',acString)+5;
    acEnd = aString.find('AccountId')-6;
    acString = aString[acStart:acEnd];
    acString = acString.split('\n');
    for ac in acString :
        if('com.google' in ac):
            accountPosI = ac.find('name=')+5;
            accountPosF = ac.find(',');
            account = ac[accountPosI:accountPosF]
            accountsA.append("Google: "+account);

        if('com.osp.app.signin' in ac):
            accountPosI = ac.find('name=')+5;
            accountPosF = ac.find(',');
            account = ac[accountPosI:accountPosF]
            accountsA.append("Samsung: "+account);
    for ac in accountsA :
        accounts += ac+'\n';
    return accounts


def getAccounts():
        aString = subprocess.check_output(['adb','shell','dumpsys','account'],text=True);
        tc = aString.find('Accounts:')+10;
        if((tc == 1)or('com.google' in aString)or('com.osp.app.signin' in aString)):
            return extractAccount(aString);
        else:
            return "Accounts: " 
