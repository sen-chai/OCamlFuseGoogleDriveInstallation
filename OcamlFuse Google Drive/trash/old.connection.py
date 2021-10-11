
#* Conectar Team Drive, se nao houver ainda
def connectAllDrives(user_data,conected_drives):
	for label,id in user_data.items():
		if label not in conected_drives:
			os.system(f'/usr/bin/google-drive-ocamlfuse -label "{label}" "/home/clear/{DESKTOP}/GoogleDrive/{label}"')
		#? Adicionar Meu Drive
	if 'default' not in conected_drives:
		os.system(f'/usr/bin/google-drive-ocamlfuse  "/home/clear/{DESKTOP}/GoogleDrive/{MEU_DRIVE}"')

#* adicionar ids dentro dos .config
def insertAllTeamDriveIds(base_dir,team_drive_paths,labels,ids):
	sucess = []
	labels_ids_dict = {k:v for k,v in zip(labels,ids)}
	for team_drive_path in team_drive_paths:
		for label,id in labels_ids_dict.items():
			if label in team_drive_path:
				config_path = os.path.join(base_dir,team_drive_path,'config')
				with open(config_path,'w') as file:
					file.writelines(config_string+'team_drive_id='+id)

				sucess.append({label:id})

	return sucess
					