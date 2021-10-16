import os

# #* instalando o app
os.system('sudo add-apt-repository ppa:alessandro-strada/ppa')
os.system('sudo apt-get update')
os.system('sudo apt-get install google-drive-ocamlfuse')

# #* Dependendicas
os.system('sudo apt install python3-pip')
os.system('pip3 install lxml')

#* Configuracao dos drives
os.system('python3 install_for_session.py')
os.system('python3 install_automount.py')