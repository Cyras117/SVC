data = {}

def setData(di):
    data['pkgs'].append(di)

def rmData(pkg):
    index = -1
    for p in data['pkgs']:
        if(p['pkg'] == pkg):
            index = data['pkgs'].index(p)
    if(index != -1):
        data['pkgs'].pop(index)

data['temp'] = {
    "id":True,
    "pass":True,
    "model":False,
    "os":False,
    "binary":False,
    "csc":False,
    "carriers":False,
    "accounts":False,
    "issues":False
}
data['pkgs']=[{
    "pkg": "com.samsung.android.mdecservice", 
    "name": "cmc", 
    "scope": {
        "teams": ["settings"], 
        "inscope": ["call", "message","all"]
        }
    },
    {
        "pkg":"com.samsung.android.dialer",
        "name":"Phone",
        "scope":{
            "teams":["settings"],
            "inscope":["call","sanity","all"]
        }
    },
    {
        "pkg":"com.santander.app",
        "name":"Santander",
        "scope":{
            "teams":["settings"],
            "inscope":["3rdparty_settings","all"]
        }
    },
    {
        "pkg":"com.bradesco",
        "name":"Bradesco",
        "scope":{
            "teams":["settings"],
            "inscope":["3rdparty_settings","all"]
        }
    },
    {
        "pkg":"br.com.bb.android",
        "name":"Banco do Brasil",
        "scope":{
            "teams":["settings"],
            "inscope":["3rdparty_settings","all"]
        }
    },
    {
        "pkg":"br.com.gabba.Caixa",
        "name":"Caixa",
        "scope":{
            "teams":["settings"],
            "inscope":["3rdparty_settings","all"]
        }
    },
    {
        "pkg":"com.itau",
        "name":"Itau",
        "scope":{
            "teams":["settings"],
            "inscope":["3rdparty_settings","all"]
        }
    },
    {
        "pkg":"com.samsung.android.messaging",
        "name":"Message",
        "scope":{
            "teams":["settings"],
            "inscope":["message","sanity","all"]
        }
    },
    {
        "pkg":"com.sec.android.inputmethod",
        "name":"Keyboard",
        "scope":{
            "teams":["settings"],
            "inscope":["keyboard","keypad","sanity","all"]
        }
    },
    {
        "pkg":"com.android.settings",
        "name":"Settings",
        "scope":{
            "teams":["settings"],
            "inscope":["settings","sanity","all"]
        }
    },
    {
        "pkg":"com.microsoft.appmanager",
        "name":"Link To Windows",
        "scope":{
            "teams":["settings"],
            "inscope":["message","all"]
        }
    },
    {
        "pkg":"com.samsung.android.app.telephonyui",
        "name":"Call Service",
        "scope":{
            "teams":["settings"],
            "inscope":["call","all"]
        }
    },
    {
        "pkg":"com.samsung.android.app.tips",
        "name":"Tips",
        "scope":{
            "teams":["settings"],
            "inscope":["settings","all"]
        }
    },
    {
        "pkg":"com.facebook.katana",
        "name":"Facebook",
        "scope":{
            "teams":["ic"],
            "inscope":["dual_mensager","all"]
        }
    },
    {
        "pkg":"com.whatsapp",
        "name":"Whatsapp",
        "scope":{
            "teams":["ic"],
            "inscope":["dual_mensager","all"]
        }
    },    
]