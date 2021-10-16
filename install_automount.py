import os
from connection import *
from get_labels_and_ids import readLabelsIds
from prepare_mount import *
from global_vars import *
import sys

#todo verificar se .profile esta limpo antes de entrar

drives_ids = readLabelsIds(sys.argv[1])
labels = list(drives_ids.keys())
ids = list(drives_ids.values())

#* Prepare Mount Folders, etc
# createAllMountDirs(drives=labels,mount_path=MOUNT_PATH)

#* Automount Install

with open(os.path.join(f"/home/{USER}",".profile"),'a') as install_file:
	for label in labels:
		command = f'(mount | grep "{os.path.join(MOUNT_PATH,label)}" > /dev/null || /usr/bin/google-drive-ocamlfuse -label "{label}" "{os.path.join(MOUNT_PATH,label)}" &) \n'
		install_file.write(command)
