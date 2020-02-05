#!/usr/bin/python3
import subprocess;

#filtra a string de retorno dos subprocessos
def filtraStringDeProcesso(bi):
    st = str(bi);
    st = st.split("'")[1];
    st = st.split("\\")[0];
    return st;

#pega o modelo do aparelho
def getModel:
    model = filtraStringDeProcesso(subprocess.check_output('adb shell getprop ro.product.model',shell=True));
    return(model);

#pega o Os do aparelho
def getOS:
    os = filtraStringDeProcesso(subprocess.check_output('adb shell getprop ro.build.version.release',shell=True));
    return os;
