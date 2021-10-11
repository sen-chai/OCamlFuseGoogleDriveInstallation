import os
import shutil

#* Delete existentes, e cria novos mount paths
def createAllMountDirs(drives,mount_path):
	#? remove anyway
	if os.path.exists(mount_path):
		shutil.rmtree(mount_path)

	os.mkdir(mount_path)

	for drive in drives:
		new_dir = os.path.join(mount_path,drive)
		os.mkdir(new_dir)
		print(new_dir,'Created Dir as mountpoint dir')
	
if __name__ == '__main__':
	from get_labels_and_ids import readLabelsIds
	drives_ids = readLabelsIds('./data/labels_ids.txt')
	createAllMountDirs(drives=drives_ids.keys(),mount_path='./mount point sandbox')
