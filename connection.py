import os
import shutil
from global_vars import *


#* Unmoutns from .confg list
def unmountAllConnectedDrives(gdfuse_dir=CONFIG_DIR,mount_path=MOUNT_PATH,clear_config=True):
	connected_drives = os.listdir(gdfuse_dir)
	for label in connected_drives:
		mounted_drive_path = f'fusermount -u "{os.path.join(mount_path,label)}"'
		print(mounted_drive_path, ' is being disconnected')
		os.system(mounted_drive_path)
		print(label,'  has been disconnected')
		if clear_config:
			shutil.rmtree(f'{os.path.join(gdfuse_dir,label)}')

#* leitura do arquivo de configuracao sem team_drive_id
def getDefaultConnectionConfig(config='./resources/config.txt'):
	with open(config,'r') as f:
		lines = f.readlines()
	string = ''
	for line in lines:
		string+=line
	return string 

#* mount path is supposed to be absolute dir
def authTeamDrive(label,id,config_dir=CONFIG_DIR,mount_path=MOUNT_PATH):
	initialize_command = f'/usr/bin/google-drive-ocamlfuse -label "{label}"'
	print('issued command ',initialize_command)
	os.system(initialize_command)
	print(label, 'concluded')

def configTeamDrive(label,id,config_dir=CONFIG_DIR,mount_path=MOUNT_PATH):
	print('starting ', label, ' config')
	config_path = os.path.join(config_dir,label,'config')
	default_connection_config = getDefaultConnectionConfig()

	with open(config_path,'w') as file:
		file.writelines(default_connection_config+'team_drive_id='+id)

	print('--- id added for ',label, 'drive')

def mountTeamDrive(label,id,config_dir=CONFIG_DIR,mount_path=MOUNT_PATH):
	#? ---
	mount_command = f'/usr/bin/google-drive-ocamlfuse -label "{label}" "{os.path.join(mount_path,label)}"'
	print(f'mount for {label} concluded')
	os.system(mount_command)

if __name__ == '__main__':

	unmountAllConnectedDrives()