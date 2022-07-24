import os,re,json

file2 = input('Перетащите файл в консоль или папку в консоль: ').replace('"','')

mas = []
if '.txt' in file2:
	mas.append(file2)
else:
	for __ in os.listdir(file2):
		mas.append(file2+'/'+__)

for file in mas:
	with open(file,'r',encoding='utf-8',errors='ignore') as file:
		f_r = file.read()

	info = re.findall(r"'EMAIL' => '\S+'",f_r)
	info2 = re.findall(r"'PASSWORD' => '\S+'",f_r)
	for _ in range(len(info)):
		try:
			email_pass = json.loads('{'+info[_].replace('=>',':').replace("'",'"')+'}')['EMAIL'] + ':' + json.loads('{'+info2[_].replace('=>',':').replace("'",'"')+'}')['PASSWORD']
			print(email_pass)
			with open('log-email-pass.txt','a',encoding='utf-8') as file_inp:
				file_inp.write(email_pass+'\n')
		except:
			pass