from connection import *
from get_labels_and_ids import readLabelsIds
from prepare_mount import *
from global_vars import *

drives_ids = readLabelsIds('./data/labels_ids.txt')
createAllMountDirs(drives=drives_ids.keys(),mount_path=MOUNT_PATH)

for label,id in drives_ids.items():
	authTeamDrive(label,id)
	configTeamDrive(label,id)
	mountTeamDrive(label,id)
