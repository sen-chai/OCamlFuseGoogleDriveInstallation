import subprocess
import os

#* pegar as duas global vars mais importantes USER e DESKTOP
USER = subprocess.check_output('whoami',encoding='utf-8')
USER = USER.strip("\n")

area_de_trabalho = 'Área de Trabalho'
desktop = 'Desktop'

home_dir = os.listdir(f'/home/{USER}')

if area_de_trabalho in home_dir: 
	DESKTOP = area_de_trabalho 
else:
	DESKTOP = desktop

CONFIG_DIR = f'/home/{USER}/.gdfuse'
MOUNT_PATH = f'/home/{USER}/{DESKTOP}/GoogleDrive'

if '__main__' == __name__:
	print(f'_{USER}_')