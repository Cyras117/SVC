data = {}
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
    "name": "CMC", 
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
            "inscope":["call","all","sanity"]
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
            "inscope":["dual_messenger","all"]
        }
    },
    {
        "pkg":"com.whatsapp",
        "name":"Whatsapp",
        "scope":{
            "teams":["ic"],
            "inscope":["dual_messenger","all"]
        }
    },   
    {
        "pkg":"com.samsung.android.honeyboard",
        "name":"Honney Board",
        "scope":{
            "teams":["settings"],
            "inscope":["keyboard","all","sanity"]
        }
    },
    {
        "pkg":"com.instagram.android",
        "name":"Instagram",
        "scope":{
            "teams":["ic"],
            "inscope":["dual_messenger","all"]
        }
    },
    {
        "pkg":"com.twitter.android",
        "name":"Twitter",
        "scope":{
            "teams":["ic"],
            "inscope":["dual_messenger","all"]
        }
    },
    {
        "pkg":"com.snapchat.android",
        "name":"Snapchat",
        "scope":{
            "teams":["ic"],
            "inscope":["dual_messenger","all"]
        }
    },
    {
        "pkg":"com.samsung.android.app.spage",
        "name":"Bixby Home/Samsung Daily",
        "scope":{
            "teams":["ic","apps"],
            "inscope":["dual_messenger","all","bixby"]
        }
    },
    {
        "pkg":"com.linkedin.android",
        "name":"Linkedin",
        "scope":{
            "teams":["ic"],
            "inscope":["dual_messenger","all"]
        }
    },
    {
        "pkg":"com.facebook.orca",
        "name":"FB Menssenger",
        "scope":{
            "teams":["ic"],
            "inscope":["dual_messenger","all"]
        }
    },
    {
        "pkg":"com.skype.raider",
        "name":"Skype",
        "scope":{
            "teams":["ic"],
            "inscope":["dual_messenger","all"]
        }
    },
    {
        "pkg":"com.netflix.mediaclient",
        "name":"Netflix",
        "scope":{
            "teams":["ic","mm"],
            "inscope":["dual_messenger","all","3rdparty_mm"]
        }
    },
    {
        "pkg":"com.mercadolibre",
        "name":"Mercado Livre",
        "scope":{
            "teams":["ic"],
            "inscope":["3rdparty_ic","all"]
        }
    },
    {
        "pkg":"com.schibsted.bomnegocio.androidApp",
        "name":"OLX",
        "scope":{
            "teams":["ic"],
            "inscope":["3rdparty_ic","all"]
        }
    },
    {
        "pkg":"com.alibaba.aliexpresshd",
        "name":"Aliexpress",
        "scope":{
            "teams":["ic"],
            "inscope":["3rdparty_ic","all"]
        }
    },
    {
        "pkg":"com.booking",
        "name":"Booking",
        "scope":{
            "teams":["ic"],
            "inscope":["3rdparty_ic","all"]
        }
    },
    {
        "pkg":"com.epicgames.fortnite",
        "name":"Fortinite",
        "scope":{
            "teams":["ic"],
            "inscope":["3rdparty_ic","all"]
        }
    },
    {
        "pkg":"com.google.android.apps.map",
        "name":"Google Maps",
        "scope":{
            "teams":["ic"],
            "inscope":["gms","all"]
        }
    },
    {
        "pkg":"com.google.android.googlequicksearchbox",
        "name":"Google",
        "scope":{
            "teams":["ic"],
            "inscope":["gms","all"]
        }
    },
    {
        "pkg":"com.android.vending",
        "name":"Playstore",
        "scope":{
            "teams":["ic"],
            "inscope":["gms","all"]
        }
    },
    {
        "pkg":"com.google.android.gms",
        "name":"Google Settings",
        "scope":{
            "teams":["ic"],
            "inscope":["gms","all"]
        }
    },
    {
        "pkg":"com.android.chrome",
        "name":"Chrome",
        "scope":{
            "teams":["ic"],
            "inscope":["internet","all"]
        }
    },
    {
        "pkg":"com.sec.android.app.sbrowser",
        "name":"S Browser",
        "scope":{
            "teams":["ic"],
            "inscope":["internet","all"]
        }
    },
    {
        "pkg":"com.samsung.accessibility",
        "name":"Accessibility",
        "scope":{
            "teams":["ic"],
            "inscope":["accessibility","all"]
        }
    },
    {
        "pkg":"com.samsung.android.game.gamehome",
        "name":"Game Laucher",
        "scope":{
            "teams":["ic"],
            "inscope":["game_laucher","all"]
        }
    },
    {
        "pkg":"com.samsung.android.game.gametools",
        "name":"Game Tools/Booster",
        "scope":{
            "teams":["ic"],
            "inscope":["game_booster","all"]
        }
    },
    {
        "pkg":"com.gm.decolar",
        "name":"Decolar",
        "scope":{
            "teams":["apps"],
            "inscope":["3rdparty_apps","all"]
        }
    },
    {
        "pkg":"com.ebay.mobile",
        "name":"Ebay",
        "scope":{
            "teams":["apps"],
            "inscope":["3rdparty_apps","all"]
        }
    },
    {
        "pkg":"com.tencent.ig",
        "name":"Pubg",
        "scope":{
            "teams":["apps"],
            "inscope":["3rdparty_apps","all"]
        }
    },
    {
        "pkg":"com.ubercab",
        "name":"Uber",
        "scope":{
            "teams":["apps"],
            "inscope":["3rdparty_apps","all"]
        }
    },
    {
        "pkg":"com.taxis99",
        "name":"99 Taxis",
        "scope":{
            "teams":["apps"],
            "inscope":["3rdparty_apps","all"]
        }
    },
    {
        "pkg":"com.samsung.android.calendar",
        "name":"Calendario",
        "scope":{
            "teams":["apps"],
            "inscope":["calendario","all"]
        }
    },
    {
        "pkg":"com.sec.android.app.samsungapps",
        "name":"Galaxy Apps/Store",
        "scope":{
            "teams":["apps"],
            "inscope":["galaxy_store","all"]
        }
    },
    {
        "pkg":"com.samsung.android.fmm",
        "name":"FMM",
        "scope":{
            "teams":["apps"],
            "inscope":["fmm","all"]
        }
    },
    {
        "pkg":"com.samsung.android.app.watchmanager",
        "name":"Galaxy Wearables",
        "scope":{
            "teams":["apps"],
            "inscope":["wearable","all"]
        }
    },
    {
        "pkg":"com.samsung.knox.securefolder",
        "name":"Secure Folder",
        "scope":{
            "teams":["apps"],
            "inscope":["secure_folder","all"]
        }
    },
    {
        "pkg":"com.osp.app.signin",
        "name":"Samsung Account",
        "scope":{
            "teams":["apps"],
            "inscope":["fmm","all"]
        }
    },
    {
        "pkg":"com.sec.android.app.camera",
        "name":"Camera",
        "scope":{
            "teams":["mm"],
            "inscope":["camera","all","sanity"]
        }
    },
    {
        "pkg":"com.samsung.android.voc",
        "name":"Samsung Members",
        "scope":{
            "teams":["mm"],
            "inscope":["samsung_members","all"]
        }
    },
    {
        "pkg":"com.samsung.sree",
        "name":"Samsung Global Goals",
        "scope":{
            "teams":["mm"],
            "inscope":["samsung_global_goals","all"]
        }
    },
    {
        "pkg":"com.google.android.apps.youtube.music",
        "name":"Youtube Music",
        "scope":{
            "teams":["mm"],
            "inscope":["3rdparty_mm","all"]
        }
    },
    {
        "pkg":"com.google.android.apps.youtube.kids",
        "name":"Youtube Kids",
        "scope":{
            "teams":["mm"],
            "inscope":["3rdparty_mm","all"]
        }
    },
    {
        "pkg":"com.dts.freefireth",
        "name":"Free Fire",
        "scope":{
            "teams":["mm"],
            "inscope":["3rdparty_mm","all"]
        }
    },
    {
        "pkg":"deezer.android.app",
        "name":"Deezer",
        "scope":{
            "teams":["mm"],
            "inscope":["3rdparty_mm","all"]
        }
    },
    {
        "pkg":"com.spotify.music",
        "name":"Spotfy",
        "scope":{
            "teams":["mm"],
            "inscope":["3rdparty_mm","all"]
        }
    },
    {
        "pkg":"com.pontomobi.smiles",
        "name":"Smiles",
        "scope":{
            "teams":["mm"],
            "inscope":["3rdparty_mm","all"]
        }
    },
    {
        "pkg":"mobile.latam.com.latamapp",
        "name":"Latam",
        "scope":{
            "teams":["mm"],
            "inscope":["3rdparty_mm","all"]
        }
    },
    {
        "pkg":"com.samsung.android.scloud",
        "name":"Samsung Cloud",
        "scope":{
            "teams":["common"],
            "inscope":["samsung_cloud","all"]
        }
    },
    {
        "pkg":"com.microsoft.skydrive",
        "name":"One Drive",
        "scope":{
            "teams":["common"],
            "inscope":["one_drive","all"]
        }
    },
    {
        "pkg":"com.samsung.android.themestore",
        "name":"Galaxy Themes",
        "scope":{
            "teams":["common"],
            "inscope":["galaxy_themes","all"]
        }
    },
    {
        "pkg":"com.sec.android.app.clockpackage",
        "name":"Clock",
        "scope":{
            "teams":["common"],
            "inscope":["clock_calculator","all"]
        }
    },
    {
        "pkg":"com.sec.android.app.popupcalculator",
        "name":"Calculadora",
        "scope":{
            "teams":["common"],
            "inscope":["clock_calculator","all"]
        }
    },
    {
        "pkg":"com.samsung.android.authfw",
        "name":"Samsung Pass",
        "scope":{
            "teams":["common"],
            "inscope":["samsung_pass","all"]
        }
    },
    {
        "pkg":"com.sec.android.app.kidshome",
        "name":"Kids Home",
        "scope":{
            "teams":["common"],
            "inscope":["kids_mode","all"]
        }
    },
    {
        "pkg":"com.sec.kidsplat.drawing",
        "name":"Bobby's Canvas",
        "scope":{
            "teams":["common"],
            "inscope":["kids_mode","all"]
        }
    },
    {
        "pkg":"com.sec.kidsplat.media.kidsmusic",
        "name":"Lisa's Music Band",
        "scope":{
            "teams":["common"],
            "inscope":["kids_mode","all"]
        }
    },
    {
        "pkg":"com.sec.kidsplat.kidstalk",
        "name":"My Magic Voice",
        "scope":{
            "teams":["common"],
            "inscope":["kids_mode","all"]
        }
    },
    {
        "pkg":"com.sec.kidsplat.kidsbcg",
        "name":"Croco Adventure",
        "scope":{
            "teams":["common"],
            "inscope":["kids_mode","all"]
        }
    },
    {
        "pkg":"com.sec.kidsplat.kidsbrowser",
        "name":"My Browser",
        "scope":{
            "teams":["common"],
            "inscope":["kids_mode","all"]
        }
    },
    {
        "pkg":"com.samsung.android.artstudio",
        "name":"My Art Studio",
        "scope":{
            "teams":["common"],
            "inscope":["kids_mode","all"]
        }
    },
    {
        "pkg":"com.sec.kidsplat.phone",
        "name":"My Phone",
        "scope":{
            "teams":["common"],
            "inscope":["kids_mode","all"]
        }
    },
    {
        "pkg":"com.sec.kidsplat.kidsgallery",
        "name":"Gallery/Coki's Video",
        "scope":{
            "teams":["common"],
            "inscope":["kids_mode","all"]
        }
    },
    {
        "pkg":"br.com.brainweb.ifood",
        "name":"Ifood",
        "scope":{
            "teams":["common"],
            "inscope":["3rdparty_common","all"]
        }
    },
    {
        "pkg":"com.amazon.mShop.android.shopping",
        "name":"Amazon",
        "scope":{
            "teams":["common"],
            "inscope":["3rdparty_common","all"]
        }
    },
    {
        "pkg":"com.gameloft.android.ANMP.GloftA8HM",
        "name":"Asphalt 8",
        "scope":{
            "teams":["common"],
            "inscope":["3rdparty_common","all"]
        }
    },
    {
        "pkg":"com.gameloft.android.ANMP.GloftA9HM",
        "name":"Asphalt 9",
        "scope":{
            "teams":["common"],
            "inscope":["3rdparty_common","all"]
        }
    },
    {
        "pkg":"com.gameloft.android.ANMP.GloftAGHM",
        "name":"Asphalt Nitro",
        "scope":{
            "teams":["common"],
            "inscope":["3rdparty_common","all"]
        }
    },
    {
        "pkg":"com.supercell.clashroyale",
        "name":"Clash Royale",
        "scope":{
            "teams":["common"],
            "inscope":["3rdparty_common","all"]
        }
    },
]