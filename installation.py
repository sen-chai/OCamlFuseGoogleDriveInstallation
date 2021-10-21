import os
import sys

labels_ids = sys.argv[1]

# #* instalando o app
os.system('sudo add-apt-repository ppa:alessandro-strada/ppa')
os.system('sudo apt-get update')
os.system('sudo apt-get install google-drive-ocamlfuse')

# #* Dependendicas
os.system('sudo apt install python3-pip')
os.system('pip3 install lxml')

#* Configuracao dos drives
os.system('google-drive-ocamlfuse')
os.system(f'python3 install_for_session.py {labels_ids}')
os.system(f'python3 install_automount.py {labels_ids}')

print('\n ______ \n instalação finalizada! \n _________\n ')