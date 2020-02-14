function setADB {
    $path = get-location
    $path = ";"+$path.toString()+"\Sfiles"
    $env:Path += $path   
}

function getCarries{
    $isub = adb  shell dumpsys isub
    $index = $isub.indexOf(' ActiveSubInfoList:')

    if($isub[$index+1] -eq '++++++++++++++++++++++++++++++++'){
        $sim = "N/A"
    }else{
        $sim = $isub[$index+1].substring($isub[$index+1].indexOf('displayName=')+12,$isub[$index+1].indexOf('carrierName=') - ($isub[$index+1].indexOf('displayName=')+12));
        if($isub[$index+2] -ne '++++++++++++++++++++++++++++++++'){
            $sim += "`t,`t"+$isub[$index+2].substring($isub[$index+2].indexOf('displayName=')+12,$isub[$index+2].indexOf('carrierName=') - ($isub[$index+2].indexOf('displayName=')+12));
        }
    }
    "Carriers:$sim" >> Versions.txt
}

function getModel() {
    $md = adb shell getprop ro.product.model
    "Model: " + $md >> Versions.txt
}

function getOSVersion(){
    $av = adb shell getprop ro.build.version.release
    "Android Version: " + $av>> Versions.txt
}

function ckFile() {
    if (Test-Path "Versions.txt" -PathType Leaf) {
        Remove-Item "Versions.txt"
    }    
}

function getAc(){
    "Accounts:" >> Versions.txt
    $wga
    $gc = adb shell dumpsys account | findstr /r name=
    foreach ($i in $gc) {
       if($i.indexOf("com.google") -eq -1){
       }else{
        $wa = $i.substring($i.indexOf("name=")+5)
        $wa = $wa.split(",")
        $wga += "`tGooge:"+$wa[0]+"`n"
       } 
       if($i.indexOf("com.osp.app.signin") -eq -1){
       }else{
           $wa = $i.substring($i.indexOf("name=")+5)
           $wa = $wa.split(",")
           $wga += "`tSamsung:"+$wa[0]+"`n"
       }
    }
    $wga >> Versions.txt
}

function generateTemplet {
    "Sample ID:" >> Versions.txt
    "Pass:" >> Versions.txt
    getModel
    getOSVersion
    getCarries
    getAc
    "`n" >> Versions.txt
}

function ckDevice(){
    adb wait-for-device    
    $d = adb devices
    $d = $d[1]
    $st = $d.indexOf("unauthorized")
    while ($st -ne -1) {
        DrawScreen
        "`tDevice nao autorizado"
        "`tAutrize a dapuracao para cntinuar"
    }
    DrawScreen
    "`n `tDevice detectado, inicializando..."
}

function startSC {
    setADB
    ckFile
    generateTemplet
    DrawScreen
    "`tIncializando, por favor, ative as opções de depuracao USB do device."
    "`tEsperando o device..."
    ckDevice
}

function openV {
    "`tArquivo gerado com sucesso."
    .\Versions.txt
}

function getv($p, $n) {
    $a = $null
    $a = adb shell dumpsys package $p | findstr /R versionName
    if($null -ne $a){        
        if($a.getType().IsArray){
            $a = $a[0]
        }
        $a = $a.substring($a.indexOf("=")+1)  
        $n + ": $a" >> Versions.txt
     }
}


function getSettings {
    DrawScreen
    "`t1- Apenas 3rd Party"
    "`t2- Todos(Incluindo 3rd party)"
    "`t0- Voltar"
    "`n `tInforme a opcao desejada:"
    $r = Read-Host

    $op = ("1" -eq $r) -or ("2" -eq $r) -or ("0" -eq $r)
    while (!$op) {
        "`t Informe um valor valido:"
        $r = Read-Host
        $op = ("1" -eq $r) -or ("2" -eq $r) -or ("0" -eq $r)
    }

    if($r -eq "0"){
        MMenu
        break
    }
    
    if($r -eq "1"){
        DrawScreen
        "`tChecando Pacotes..."
        "`tPara cancelar pressione ctrl+c"
        getv -p com.santander.app  -n Santander
        getv -p com.bradesco  -n Bradesco
        getv -p br.com.bb.android  -n "Banco do Brasil"
        getv -p br.cm.gabba.Caixa  -n Caixa
        getv -p com.itau  -n Itau
    }else{
        DrawScreen
        "`tChecando Pacotes..."
        "`tPara cancelar pressione ctrl+c"
        getv -p com.samsung.android.dialer -n Phone
        getv -p com.samsung.android.messaging -n Message
        getv -p com.sec.android.inputmethod -n Keyboard
        getv -p com.android.settings -n Settings
        getv -p com.samsung.android.mdecservice  -n CMC
        getv -p com.microsoft.appmanager  -n "Link To Windows"
        getv -p com.santander.app  -n Santander
        getv -p com.bradesco  -n Bradesco
        getv -p br.com.bb.android  -n "Banco do Brasil"
        getv -p br.cm.gabba.Caixa  -n Caixa
        getv -p com.itau  -n Itau
        
    }

    openV        
}

function getIc {
    DrawScreen
    "`t1- Apenas aplicativos padroes"
    "`t2- 3rd party Exloratorio"
    "`t3- GMS"
    "`t4- Internet"
    "`t5- Acessibilidade"
    "`t6- Game Tools"
    "`t7- Game Launcher"
    "`t0- Voltar"
    "`n `tInforme a opcao desejada:"
    $r = Read-Host

    $op = ("1" -eq $r) -or ("2" -eq $r) -or ("3" -eq $r) -or ("4" -eq $r) -or ("5" -eq $r) -or ("6" -eq $r) -or ("0" -eq $r) -or ("7" -eq $r)
    while (!$op) {
        "`t Informe um valor valido:"
        $r = Read-Host
        $op = ("1" -eq $r) -or ("2" -eq $r) -or ("3" -eq $r) -or ("4" -eq $r) -or ("5" -eq $r) -or ("6" -eq $r) -or ("0" -eq $r) -or ("7" -eq $r)
    }
    if($r -eq "0"){
        MMenu
        break
    }
    
    if($r -eq "1"){
        DrawScreen
        "`tChecando Pacotes..."
        "`tPara cancelar pressione ctrl+c"
        getv -p com.facebook.katana  -n Facebook
        getv -p com.whatsapp  -n Whatsapp
        getv -p com.instagram.android  -n Instagram
        getv -p com.twitter.android  -n Twitter
        getv -p com.snapchat.android  -n Snapchat
        getv -p com.samsung.android.app.spage  -n "Bixby Home"
        getv -p com.linkedin.android  -n Linkedin
        getv -p com.facebook.orca  -n "FB Messenger"
        getv -p com.skype.raider  -n Skype
        getv -p com.netflix.mediaclient  -n Netflix
        
    }
    if($r -eq "2"){
        DrawScreen
        "`tChecando Pacotes..." 
        "`tPara cancelar pressione ctrl+c"
        getv -p com.mercadolibre  -n "Mercado Livre"
        getv -p com.schibsted.bomnegocio.androidApp  -n OLX
        getv -p com.alibaba.aliexpresshd  -n Aliexpress
        getv -p com.booking  -n Booking
        getv -p com.epicgames.fortnite  -n Fortinite
    }
    if($r -eq "3"){
        DrawScreen
        "`tChecando Pacotes..." 
        "`tPara cancelar pressione ctrl+c"
        getv -p com.google.android.apps.map  -n "Google Maps"
        getv -p com.google.android.googlequicksearchbox  -n Google
        getv -p com.android.vending  -n "Google Playstore"
        getv -p com.google.android.gms  -n "Google Settings"
    }
    if($r -eq "4"){
        DrawScreen
        "`tChecando Pacotes..." 
        "`tPara cancelar pressione ctrl+c"
        getv -p com.android.chrome  -n Chrome
        getv -p com.sec.android.app.sbrowser  -n "S Browser"
    }
    if($r -eq "5"){
        DrawScreen
        "`tChecando Pacotes..." 
        "`tPara cancelar pressione ctrl+c"
        getv -p  com.samsung.accessibility  -n "Accessibility"
    }
    if($r -eq "6"){
        DrawScreen
        "`tChecando Pacotes..." 
        "`tPara cancelar pressione ctrl+c"
        getv -p com.samsung.android.game.gametools  -n 'Game Tools'
    }
    if($r -eq "7"){
        DrawScreen
        "`tChecando Pacotes..." 
        "`tPara cancelar pressione ctrl+c"
        getv -p com.samsung.android.game.gamehome  -n 'Game Laucher/Booster'
    }


    openV        
}

function getMm {
    DrawScreen
    "`t1- Apenas 3rd Party"
    "`t2- Todos(Incluindo 3rd party)"
    "`t0- Voltar"
    "`n `tInforme a opcao desejada:"
    $r = Read-Host

    $op = ("1" -eq $r) -or ("2" -eq $r) -or ("0" -eq $r)
    while (!$op) {
        "`t Informe um valor valido:"
        $r = Read-Host
        $op = ("1" -eq $r) -or ("2" -eq $r) -or ("0" -eq $r)
    }
    if($r -eq "0"){
        MMenu
        break
    }
    
    if($r -eq "1"){
        DrawScreen
        "`tChecando Pacotes..."
        "`tPara cancelar pressione ctrl+c"
        getv -p com.google.android.apps.youtube.music  -n "Youtube Music"
        getv -p com.google.android.apps.youtube.kids  -n "Youtube Kids"
        getv -p com.dts.freefireth  -n "Free Fire"
        getv -p deezer.android.app  -n Deezer
        getv -p com.spotify.music  -n Spotify
        getv -p com.pontomobi.smiles  -n Smiles
        getv -p mobile.latam.com.latamapp  -n Latam
        getv -p com.netflix.mediaclient  -n Netflix
    }else{
        DrawScreen
        "`tChecando Pacotes..."
        "`tPara cancelar pressione ctrl+c"
        getv -p com.sec.android.app.camera  -n Camera
        getv -p com.samsung.android.voc  -n "Samsung Members"
        getv -p com.samsung.sree  -n "Samsung Global Goals"
        getv -p com.google.android.apps.youtube.music  -n "Youtube Music"
        getv -p com.google.android.apps.youtube.kids  -n "Youtube Kids"
        getv -p com.dts.freefireth  -n "Free Fire"
        getv -p deezer.android.app  -n Deezer
        getv -p com.spotify.music  -n Spotify
        getv -p com.pontomobi.smiles  -n Smiles
        getv -p mobile.latam.com.latamapp  -n Latam
        getv -p com.netflix.mediaclient  -n Netflix
    }

    openV
}

function getApps {
    DrawScreen
    "`t1- Apenas 3rd Party"
    "`t2- Todos(Incluindo 3rd party)"
    "`t0- Voltar"
    "`n `tInforme a opcao desejada:"
    $r = Read-Host

    $op = ("1" -eq $r) -or ("2" -eq $r) -or ("0" -eq $r)
    while (!$op) {
        "`t Informe um valor valido:"
        $r = Read-Host
        $op = ("1" -eq $r) -or ("2" -eq $r) -or ("0" -eq $r)
    }
    if($r -eq "0"){
        MMenu
        break
    }

    if($r -eq "1"){
        DrawScreen
        "`tChecando Pacotes..."
        "`tPara cancelar pressione ctrl+c"
        getv -p com.gm.decolar  -n Decolar
        getv -p com.ebay.mobile  -n Ebay
        getv -p com.tencent.ig  -n Pubg
        getv -p com.ubercab  -n Uber
        getv -p com.taxis99  -n "99"
    }else{
        DrawScreen
        "`tChecando Pacotes..."
        "`tPara cancelar pressione ctrl+c"
        getv -p com.samsung.android.calendar  -n Calendario
        getv -p com.sec.android.app.samsungapps  -n "Galaxy Apps/Store"
        getv -p com.samsung.android.fmm  -n FMM
        getv -p com.samsung.android.app.spage  -n "Samsung daily/Bixby Home"
        getv -p com.gm.decolar  -n Decolar
        getv -p com.ebay.mobile  -n Ebay
        getv -p com.tencent.ig  -n Pubg
        getv -p com.ubercab  -n Uber
        getv -p com.taxis99  -n "99"
        getv -p com.samsung.android.app.watchmanager -n "Galaxy Wearable"
        getv -p com.samsung.android.app.reminder  -n "Reminder"
        getv -p com.samsung.knox.securefolder  -n "Secure Folder"
        getv -p com.samsung.android.app.spage  -n "Samsung daily/Bixby Home"
        getv -p com.osp.app.signin  -n "Samsung Account"
    }

    openV
}

function getCommon {
    DrawScreen
    "`t1- Apenas 3rd Party"
    "`t2- Todos(Incluindo 3rd party)"
    "`t0- Voltar"
    "`n `tInforme a opcao desejada:"
    $r = Read-Host

    $op = ("1" -eq $r) -or ("2" -eq $r) -or ("0" -eq $r)
    while (!$op) {
        "`t Informe um valor valido:"
        $r = Read-Host
        $op = ("1" -eq $r) -or ("2" -eq $r) -or ("0" -eq $r)
    }
    if($r -eq "0"){
        MMenu
        break
    }
    
    if($r -eq "1"){
        DrawScreen
        "`tChecando Pacotes..."
        "`tPara cancelar pressione ctrl+c"
        getv -p  br.com.brainweb.ifood -n Ifood
        getv -p  com.amazon.mShop.android.shopping -n Amazon
        getv -p  com.gameloft.android.ANMP.GloftA8HM -n "Asphalt 8"
        getv -p  com.gameloft.android.ANMP.GloftA9HM -n "Asphalt 9"        
        getv -p  com.gameloft.android.ANMP.GloftAGHM -n "Asphalt Nitro"        
        getv -p  com.supercell.clashroyale -n "Clash Royale"
        getv -p  com.microsoft.skydrive -n "One Drive"
    }else{
        DrawScreen
        "`tChecando Pacotes..."
        "`tPara cancelar pressione ctrl+c"
        getv -p  com.sec.android.app.clockpackage -n Clock
        getv -p  com.samsung.android.scloud -n "Samsung Cloud"
        getv -p  com.samsung.android.authfw -n "Samsung Pass"
        getv -p  com.samsung.android.themestore -n "Galaxy Themes"
        getv -p  com.sec.android.app.kidshome -n "Kids Home"
        getv -p  com.sec.kidsplat.drawing -n "Bobby's Canvas"
        getv -p  com.sec.kidsplat.media.kidsmusic -n "Lisa's Music Band"
        getv -p  com.sec.kidsplat.kidstalk -n "My Magic Voice "
        getv -p  com.sec.kidsplat.kidsbcg -n "Croco Adventure"
        getv -p  com.sec.kidsplat.kidsbrowser -n "My Browser"
        getv -p  com.samsung.android.artstudio -n "My Art Studio"
        getv -p  com.sec.kidsplat.phone -n "My Phone"
        getv -p  com.sec.kidsplat.camera -n "My Camera"
        getv -p  com.sec.kidsplat.kidsgallery -n "Gallery/Coki's Video"
        getv -p  br.com.brainweb.ifood -n Ifood
        getv -p  com.amazon.mShop.android.shopping -n Amazon
        getv -p  com.gameloft.android.ANMP.GloftA8HM -n "Asphalt 8"
        getv -p  com.gameloft.android.ANMP.GloftA9HM -n "Asphalt 9"        
        getv -p  com.gameloft.android.ANMP.GloftAGHM -n "Asphalt Nitro"  
        getv -p  com.supercell.clashroyale -n "Clash Royale"
        getv -p  com.microsoft.skydrive -n "One Drive"
        getv -p  com.sec.android.app.popupcalculator -n "Calculadora"
    }

    openV
}

function DrawScreen {
    Clear-Host
    "`n `n"
    "`t SVC by alexsandro.a & kledyson.f"
    "`n"
    
}

function getA {
    DrawScreen
    "`tChecando Pacotes..."
    "`tPode demorar um pouco..."
    "`tPara cancelar pressione ctrl+c"
    getv -p com.samsung.android.dialer -n "Phone"
    getv -p com.samsung.android.messaging -n "Message"
    getv -p com.sec.android.inputmethod -n "Keyboard"
    getv -p com.android.settings -n "Settings"
    getv -p com.samsung.android.mdecservice  -n "CMC"
    getv -p com.microsoft.appmanager  -n "Link To Windows"
    getv -p com.santander.app  -n "Santander"
    getv -p com.bradesco  -n "Bradesco"
    getv -p br.com.bb.android  -n "Banco do Brasil"
    getv -p br.cm.gabba.Caixa  -n "Caixa"
    getv -p com.itau  -n "Itau"
    getv -p com.facebook.katana  -n "Facebook"
    getv -p com.whatsapp  -n "Whatsapp"
    getv -p com.instagram.android  -n "Instagram"
    getv -p com.twitter.android  -n "Twitter"
    getv -p com.snapchat.android  -n "Snapchat"
    getv -p com.linkedin.android  -n "Linkedin"
    getv -p com.facebook.orca  -n "FB Messenger"
    getv -p com.skype.raider  -n "Skype"
    getv -p com.netflix.mediaclient  -n "Netflix"
    getv -p com.mercadolibre  -n "Mercado Livre"
    getv -p com.schibsted.bomnegocio.androidApp  -n "OLX"
    getv -p com.alibaba.aliexpresshd  -n "Aliexpress"
    getv -p com.booking  -n "Booking"
    getv -p com.epicgames.fortnite  -n "Fortinite"
    getv -p com.google.android.apps.map  -n "Google Maps"
    getv -p com.google.android.googlequicksearchbox  -n "Google"
    getv -p com.android.vending  -n "Google Playstore"
    getv -p com.google.android.gms  -n "Google Settings"
    getv -p com.android.chrome  -n "Chrome"
    getv -p com.sec.android.app.sbrowser  -n "S Browser"
    getv -p com.sec.android.app.camera  -n "Camera"
    getv -p com.samsung.android.voc  -n "Samsung Members"
    getv -p com.samsung.sree  -n "Samsung Global Goals"
    getv -p com.google.android.apps.youtube.music  -n "Youtube Music"
    getv -p com.google.android.apps.youtube.kids  -n "Youtube Kids"
    getv -p com.dts.freefireth  -n "Free Fire"
    getv -p deezer.android.app  -n "Deezer"
    getv -p com.spotify.music  -n "Spotify"
    getv -p com.pontomobi.smiles  -n "Smiles"
    getv -p mobile.latam.com.latamapp  -n "Latam"
    getv -p com.netflix.mediaclient  -n "Netflix"    
    getv -p com.samsung.android.calendar  -n "Calendario"
    getv -p com.sec.android.app.samsungapps  -n "Galaxy Apps/Store"
    getv -p com.samsung.android.fmm  -n "FMM"
    getv -p com.samsung.android.app.spage  -n "Samsung daily/Bixby Home"
    getv -p com.gm.decolar  -n "Decolar"
    getv -p com.ebay.mobile  -n "Ebay"
    getv -p com.tencent.ig  -n "Pubg"
    getv -p com.ubercab  -n "Uber"
    getv -p com.taxis99  -n "99"
    getv -p  com.sec.android.app.clockpackage -n "Clock"
    getv -p  com.samsung.android.scloud -n "Samsung Cloud"
    getv -p  com.samsung.android.authfw -n "Samsung Pass"
    getv -p  com.samsung.android.themestore -n "Galaxy Themes"
    getv -p  com.sec.android.app.kidshome -n "Kids Home"
    getv -p  com.sec.kidsplat.drawing -n "Bobby's Canvas"
    getv -p  com.sec.kidsplat.media.kidsmusic -n "Lisa's Music Band"
    getv -p  com.sec.kidsplat.kidstalk -n "My Magic Voice "
    getv -p  com.sec.kidsplat.kidsbcg -n "Croco Adventure"
    getv -p  com.sec.kidsplat.kidsbrowser -n "My Browser"
    getv -p  com.samsung.android.artstudio -n "My Art Studio"
    getv -p  com.sec.kidsplat.phone -n "My Phone"
    getv -p  com.sec.kidsplat.camera -n "My Camera"
    getv -p  com.sec.kidsplat.kidsgallery -n "Gallery/Coki's Video"
    getv -p  br.com.brainweb.ifood -n "Ifood"
    getv -p  com.amazon.mShop.android.shopping -n "Amazon"
    getv -p  com.gameloft.android.ANMP.GloftA8HM -n "Asphalt 8"
    getv -p  com.supercell.clashroyale -n "Clash Royale"
    getv -p  com.microsoft.skydrive -n "One Drive"
    getv -p  com.samsung.android.app.watchmanager  -n "Galaxy Wearable"
    getv -p  com.samsung.android.app.reminder   -n "Reminder"
    getv -p  com.samsung.accessibility  -n "Accessibility"
    getv -p com.samsung.knox.securefolder  -n "Secure Folder"
    openV
}

function checkOpMm ($o){
    $re = ("1" -eq $o) -or ("2" -eq $o) -or ("3" -eq $o) -or ("4" -eq $o) -or ("5" -eq $o) -or ("6" -eq $o) -or ("0" -eq $o) -or ("7" -eq $o) 
    while (!$re) {
        "`tInforme um valor valido:"
        $o = Read-Host
        $re = ("1" -eq $o) -or ("2" -eq $o) -or ("3" -eq $o) -or ("4" -eq $o) -or ("5" -eq $o) -or ("6" -eq $o) -or ("0" -eq $o) -or ("7" -eq $o) 
    }
    if ($o -eq 1) {
        getIc
    }
    if ($o -eq 2) {
        getMm
    }
    if ($o -eq 3) {
        getApps
    }
    if ($o -eq 4) {
        getCommon
    }
    if($o -eq 5){
        getSettings
    }
    if($o -eq 6){
        getA
    }
    if($o -eq 0){
        break
    }
    if($o -eq 7){
        .\Versions.txt
        MMenu
        break
    }
}
function MMenu {
    DrawScreen
    "`n `t1- Versao de IC"
    "`n `t2- Versao de MM"
    "`n `t3- Versao de Apps"
    "`n `t4- Versao de Commom"
    "`n `t5- Versao de Settings"
    "`n `t6- Todas as versoes"
    "`n `t7- Apenas template"
    "`n `t0- Finalizar script"
    
    "`n `tInforme a opcao desejada:`t"
    $i = Read-Host
    checkOpMm($i)
}

function svc(){
    startSC
    while(1){
        
        MMenu
    }
}

svc