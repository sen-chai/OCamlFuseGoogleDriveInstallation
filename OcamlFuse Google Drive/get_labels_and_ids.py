import os 
from lxml import etree

#* Pegar Lista de Diretorios e Id's
def getLabelsIds(user_data):
	root = etree.parse(user_data).getroot()

	#todo cuiodado com o hard code na selecao. Verifique os outputs
	labels = root.xpath('.//div[@aria-label]/div[@data-tooltip-unhoverable and @aria-label]')
	ids = root.xpath('.//div[@data-id]')

	ids = ids[:round(len(ids)/2)]
	labels = labels[:round(len(labels)/2)]
	ids = [i.get('data-id') for i in ids]
	labels = [i.text.strip() for i in labels]

	print('--- labels', labels)
	print('--- ids',ids)

	print('got all labels and ids')

	return {k:v for k,v in zip(labels,ids)}

def writeLabelsIds(labels_ids,write_dir):
	with open(write_dir,'w') as f:
		for label,id in labels_ids.items():
			f.write(f"{label} ___ {id}\n")

def readLabelsIds(get_dir='./data/labels_ids.txt'):
	labels_ids = {}
	with open(get_dir,'r') as f:
		lines = f.readlines()
	for l in lines:
		label,id = l.strip('\n').split(' ___ ')
		labels_ids[label] = id
	return labels_ids


if __name__ == '__main__':
	file = './data/labels_ids.txt'
	user_data = getLabelsIds('./resources/drive_clear.html')
	writeLabelsIds(labels_ids=user_data,write_dir=file)
	output = readLabelsIds(file)
	print(output)
