from lxml import etree
import os

# * Get Title and data-id from Google Drive Shared Drives

# USER_DATA = "./adm_vtv.html"
USER_DATA = "./drive_clear.html"

root = etree.parse(USER_DATA).getroot()
labels = root.xpath('.//span[@class="l-Ab-T-r" and @data-is-doc-name="true"]')
ids = root.xpath('.//div[@data-id and @tabindex]')

# * got the labels and Ids
for title,id in zip(labels,ids):
	print(title.text.strip(' \n'),id.get('data-id'))

input()

os.system(f'google-drive-ocamlfuse -label "{ids[0]}"')
DESKTOP = 'Desktop'
for label in labels:
	os.system(f'"mount | grep "/home/clear/Desktop/{label}" > /dev/null || /usr/bin/google-drive-ocamlfuse -label "{label}" "/home/clear/Desktop/GoogleDrive/{label}" & " >> ~/.profile')
