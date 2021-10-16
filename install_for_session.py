from connection import *
from get_labels_and_ids import readLabelsIds
from prepare_mount import *
from global_vars import *
import sys

drives_ids = readLabelsIds(sys.argv[1])
createAllMountDirs(drives=drives_ids.keys(),mount_path=MOUNT_PATH)

for label,id in drives_ids.items():
	authTeamDrive(label,id)
	configTeamDrive(label,id)
	mountTeamDrive(label,id)
