import requests
import urllib3
from PyQt5 import QtWidgets, uic
from winreg import *
import sys, os
import win32api
import re
import time
import pyautogui

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# getIp

def verifyIP():
	pegarIp = requests.get('http://meuip.com/api/meuip.php', verify=False)
	if pegarIp.status_code == 200:
		verifyVpn = requests.get('https://blackbox.ipinfo.app/lookup/' + pegarIp.text, verify=False)
		if verifyVpn.text == 'Y':
			detectVPN = 1
		else:
			detectVPN = 0
	else:
		detectVPN = 1

	if detectVPN == 0:
		libertIP()
	else:
		win32api.MessageBox(0, 'Foi detectado um serviço de VPN no seu PC!\n\nQualquer dúvida, entre em contato com nosso suporte:\nwww.loskatchorros.com.br/forum', 'AVISO', 0x00001000) 
#

def libertIP():
	liberarIP = requests.get('API_REMOVIDA', verify=False)
	if liberarIP.status_code == 200:
		ipLiberado = 1
	else:
		ipLiberado = 0
	
	if ipLiberado == 0:
		win32api.MessageBox(0, 'Não foi possível liberar o seu acesso!\n\nQualquer dúvida, entre em contato com nosso suporte:\nwww.loskatchorros.com.br/forum', 'AVISO', 0x00001000) 
	else:
		conectarNoSv()



def conectarNoSv():

	try:
		REG_PATH = r"SOFTWARE\SAMP"
		name = "PlayerName"
		gta = "gta_sa_exe"
		registry_key = OpenKey(HKEY_CURRENT_USER, REG_PATH, 0, KEY_WRITE)
		SetValueEx(registry_key, name, 0, REG_SZ, Interface.lineEdit.text())
		sovai = Interface.lineEdit_2.text().replace("gta_sa.exe", "")
		if sovai[-1:] == '\\':
			SetValueEx(registry_key, gta, 0, REG_SZ, sovai + 'gta_sa.exe')
		else:
			SetValueEx(registry_key, gta, 0, REG_SZ, sovai + r'\gta_sa.exe')
		CloseKey(registry_key)

		if Interface.comboBox.currentText() == 'Servidor: 4':
			os.system(caminho + ' ' + '149.56.181.17:7777' + ' ' + '')
		else:
			os.system(caminho + ' ' + 'server3.loskatchorros.com.br' + ' ' + '')

	except Exception as e:
		win32api.MessageBox(0, 'Não foi possível iniciar o jogo!\n\nQualquer dúvida, entre em contato com nosso suporte:\nwww.loskatchorros.com.br/forum', 'AVISO', 0x00001000) 


#
def resource_path(relative_path):
    
    try:
        
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#

arquivoUi = resource_path('untitled.ui')

MainWindow = QtWidgets.QApplication([])
Interface = uic.loadUi(arquivoUi)

#

hreg = ConnectRegistry(None, HKEY_CURRENT_USER)
hkey = OpenKey(hreg, 'Software\SAMP')
exibirNick = QueryValueEx(hkey, 'PlayerName')[0]

Interface.lineEdit.setText(exibirNick)

reconhecergta = QueryValueEx(hkey, 'gta_sa_exe')[0]

Interface.lineEdit_2.setText(reconhecergta)

reconhecergta = reconhecergta.replace("gta_sa.exe", "")
	
#

arquivo = reconhecergta#.replace("\\\\", "\\")
if reconhecergta[-1:] == '\\':
	caminho = '""' + arquivo + 'samp.exe' + '""'
else:
	caminho = '""' + arquivo + '\samp.exe' + '""'



#

Interface.pushButton.clicked.connect(verifyIP)
Interface.comboBox.addItems(['Servidor: 4', 'Servidor: 3'])

#

Interface.show()
MainWindow.exec()