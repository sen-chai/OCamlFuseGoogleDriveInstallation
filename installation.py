import os

import sys

labels_ids = sys.argv[1]

# #* instalando o app, mirror falha as vezes
# os.system('sudo add-apt-repository ppa:alessandro-strada/ppa')
# os.system('sudo apt-get update')
# os.system('sudo apt-get install google-drive-ocamlfuse')

#* instalacao usando .deb local
os.system('sudo dpkg -i ./resources/google-drive-ocamlfuse_0.7.27-0ubuntu1_ubuntu20.04.1_amd64.deb')

# #* Dependendicas
os.system('sudo apt install python3-pip')
os.system('pip3 install lxml')

#* Configuracao dos drives
os.system('google-drive-ocamlfuse')
os.system(f'python3 install_for_session.py {labels_ids}')
os.system(f'python3 install_automount.py {labels_ids}')

print('\n ______ \n instalação finalizada! \n _________\n ')