from os import WIFCONTINUED
from lxml import etree

# * Get Title and data-id from Google Drive Shared Drives

USER_DATA = "./resources/adm_vtv.html"

root = etree.parse(USER_DATA).getroot()
labels = root.xpath('.//span[@class="l-Ab-T-r" and @data-is-doc-name="true"]')
ids = root.xpath('.//div[@data-id and @role="option" and @tabindex]')

# # * got the labels and Ids
# for title,id in zip(labels,ids):
# 	print(title.text.strip('\n'),id.get('data-id'))
#* tratar exceptions
#? remover '/'
labels = [label.text.strip('\n') for label in labels]
labels = [label.strip('/') for label in labels]
ids = [id.get('data-id') for id in ids]
user_data = dict(zip(labels,ids))

from get_labels_and_ids import writeLabelsIds,readLabelsIds
file='data/labels_ids.txt'
writeLabelsIds(labels_ids=user_data,write_dir=file)
output = readLabelsIds()
print(output)