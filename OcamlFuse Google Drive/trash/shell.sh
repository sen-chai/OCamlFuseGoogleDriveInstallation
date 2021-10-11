mount | grep /home/clear/Desktop/CLEAR\ SERVIDOR\ ARQUIVOS > /dev/null || /usr/bin/google-drive-ocamlfuse -label "CLEAR SERVIDOR ARQUIVOS" "/home/clear/Desktop/GoogleDrive/CLEAR SERVIDOR ARQUIVOS" &

mount | grep /home/clear/Desktop/{label} > /dev/null || /usr/bin/google-drive-ocamlfuse -label {label} "/home/clear/Desktop/GoogleDrive/{label}" &
