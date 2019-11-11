


'''from wand.image import Image as Img
with Img(filename='factPdf.pdf', resolution=300) as img:
    img.compression_quality = 99
    img.save(filename='factPdf.jpg')
	
from wand.image import Image as WImage
image_file = open("sample.jpeg", "wb")
index = 1 #Page Number Of Pdf
with WImage(filename='factPdf.pdf' + "[{}]".format(index), resolution=400) as img:
    image_jpeg = img.convert('jpeg')
    image_jpeg.save(filename=image_file.name)
image_file.close()	
from PIL import ImageEnhance, ImageFilter
#from PIL import Image as Img
im = Img.open("sample.jpeg")
im = im.filter(ImageFilter.MedianFilter())
 
enhancer = ImageEnhance.Contrast(im)
 
im = enhancer.enhance(2)
im = im.convert('1')
im.save('sample.jpeg')	
'''
import image_slicer

#ImagineFactura = 'fact1.jpg'
#ImagineFactura = 'F3.png'
#ImagineFactura = 'Fact14.pdf'
#ImagineFactura = 'Fscanned.jpg'
#ImagineFactura = 'NewFact4.pdf'
import os

path = os.getcwd()

files = []
# r=root, d=directories, f = files
fileIterat=0
for r, d, f in os.walk(path):
	for file in f:
		if '.png' in file or '.pdf' in file:
			files.append(file)
			fileIterat=fileIterat+1
fileIteratStart=0
print(files)
for f in files:
	
	ImagineFactura=f
	from PIL import Image
	import tkinter as tk	
	m = tk.Tk()
	m.title('Counting Seconds') 
	button = tk.Button(m, text='Stop', width=25, command=m.destroy) 
	m.geometry("400x300")

	button.pack()

	if ImagineFactura[-4:]=='.pdf':
		from wand.image import Image
		from wand.color import Color
		
		
		
		from tika import parser
		with Image(filename=ImagineFactura, resolution=250) as img:
			with Image(width=img.width, height=img.height, background=Color("white")) as bg:
				bg.composite(img,0,0)
				bg.save(filename="pikachu2.png")
				ImagineFactura = "pikachu2.png"
	print(ImagineFactura[-4:])
	try:
		from PIL import Image
	except ImportError:
		import Image
	import pytesseract
	import re 
	pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
	pytessData=pytesseract.image_to_string(Image.open(ImagineFactura))
	#f = open('a.txt.txt','r')
	#f1 = open('b.txt','w')
	#f1.write(pytessData)
	all=pytessData
	print('----------------------start')
	print(all)
	print('----------------------end')
	#image_slicer.slice(ImagineFactura, 4)
	#all = f.read()
	#f1.close()
	bucatiJson=[]
	pretAfisat=0
	tvaAfisat=100
	numFact=0
	data=''
	cif=''
	nrFound=0
	adrFound=0
	x=re.findall("[0-9][0-9][./][0-9][0-9][./][0-9][0-9][0-9][0-9]",all)
	dateX=re.search(r'Seria[ a-zA-Z0-9-]{0,15}nr[ :\.]{0,5}[a-zA-Z]{0,3}([ 0-9]{0,10})',all)
	addrX=re.search(r'((Sediul)|(Sos)|(Strada)|(strada)|(Adresa)|(STRADA)|(STR)|(ADR)|(SEDIUL))[\.,:a-zA-Z0-9 -]{10,55}',all)
	#print(all)
	testKey=753217532
	actualTestKey=int(str(testKey)[::-1])
	myCifReg="[^0-9](RO)?([0-9][0-9][0-9]{5,7})[^0-9]"
	cuiType2=re.findall(myCifReg,all)
	myCnpReg="[1-8][0-9][0-9][0-1][0-9][0-3][0-9][0-5][0-9][0-9][0-9][0-9][0-9]"
	cnpData=re.findall(myCnpReg,all)
	print('CNP',cnpData)
	myCNPSet=set([])
	#Verificare CNP
	cnpKey=str(279146358279)
	#cnpData.append('2960628048017')
	for a in cuiType2:
		a=a[0:-1]
	'''
	for i in cnpData:
		sumaCNP=0
		iterator=0
		for cifra in i[0:12]:
			sumaCNP+=int(cifra) * int(cnpKey[iterator])
			print(cifra,cnpKey[iterator])
			iterator+=1

			
		if (sumaCNP % 11) == 10:
			if (int(i[-1]))==1:
				print('Goodbye world')
				myCNPSet.add(i)
		if (sumaCNP% 11) == int(i[-1]):
			myCNPSet.add(i)
			print('Hello world')
		print('abc',sumaCNP%11,i[-1])
	'''
	def get_CNPS(available_data):
		myCnpReg="[1-8][0-9][0-9][0-1][0-9][0-3][0-9][0-5][0-9][0-9][0-9][0-9][0-9]"
		cnpData=re.findall(myCnpReg,available_data)
		for i in cnpData:
			sumaCNP=0
			iterator=0
			for cifra in i[0:12]:
				sumaCNP+=int(cifra) * int(cnpKey[iterator])
				print(cifra,cnpKey[iterator])
				iterator+=1

				
			if (sumaCNP % 11) == 10:
				if (int(i[-1]))==1:
					print('Goodbye world')
					myCNPSet.add(i)
			if (sumaCNP% 11) == int(i[-1]):
				myCNPSet.add(i)
				print('Hello world')
			print('abc',sumaCNP%11,i[-1])
	get_CNPS(all)		
	#Verificare CIF
	my2ndCifSet=set([])
	print('CUI 2',cuiType2)
	for cifObj in cuiType2:
		sum=0
		controlDigit=cifObj[1][-1]
		count=0
		for cifra in cifObj[1][::-1][1:]:
			sum=sum+int(cifra)*int(str(actualTestKey)[count])
			#print(str(actualTestKey)[count])
			count=count+1
			print(cifra)
		sum=sum*10
		print(cifObj,(sum%11),controlDigit)
		if int(controlDigit)==(sum%11) or (int(controlDigit)==0 and sum%11==10):
			if len(cifObj[1])>5:
				my2ndCifSet.add(cifObj[0]+cifObj[1])
	print(my2ndCifSet)
		
	#cuiType2=re.search(myCifReg,all).groups()
	print('xxxxxxxxxxxxxx',cuiType2,'xxxxxxxxxxxxxxxxxx')
	if dateX:
		print(dateX.group())
		nrFound=1
	if addrX:
		adrFound=1
		print('foundAddr',addrX.group())
	#Spargere în rânduri
	for y in x:
		if (int(y[-4:]) > 2000 or (float(y[-2:])<20) )and (int(y[-4:])<2100 and int(y[:2]) <30 and int(y[3:5]) <12):
			if data!='':
				if int(y[-4:])<=int(data[-4:]) and int(y[:2])<=int(data[:2]) and int(y[3:5])<=int(data[3:5]):
					data=y
			else:
				data=y
			print(y)
			print(y[-4:],y[:2],y[3:5])

	if all.find('Str')>0:
		adresa=all[all.find('Str'):all.find('Str')+25]
	else:
		adresa='None'
		
	adresaSplit = adresa.split('   ')
	print('Adresa=',adresaSplit)
	#ints=[float(s) for s in all.split() if s.isdigit()]
	ints = re.findall("[0-9]+,[0-9]{2}",all)
	ints2 = re.findall("[0-9]+,[0-9]+\.[0-9]{2}",all)
	ints2 = ints2 + re.findall("[0-9]+\.[0-9]+,[0-9]{2}",all)
	ints = ints + re.findall("[0-9]+\.[0-9]{2}",all)
	print(ints2)
	valori=[]
	valoriMari=[]
	for toreplace in ints:
		valori.append(float(re.sub(',','.',toreplace)))
	if len(ints2)>0:
		for toreplace in ints2:	
			#valoriMari.append(float(re.sub('.','',toreplace)))
			print(float((toreplace.replace(',','')).replace('.','')[:-2]) + float((toreplace.replace(',','')).replace('.','')[-2:])/100)
			valoriMari.append(float((toreplace.replace(',','')).replace('.','')[:-2]) + float((toreplace.replace(',','')).replace('.','')[-2:])/100)
			print('asd')
			#valoriMari.append(float(re.sub('.','',(re.sub('.','',toreplace)))[:-2]) + float(re.sub('.','',(re.sub('.','',toreplace)))[-2:]))
			#print(re.sub(',','',toreplace),float(re.sub(',','',toreplace)),end="BIGX")
	print(valori)
	#print(valoriMari)
	preturi=set([])
	tva=set([])
	total=set([])
	#preturi2=set([])
	#tva2=set([])
	#total2=set([])
	auxlst=[]
	#valori.append(0)
	valori = valori + valoriMari
	if 0 in valori:
		for i in range(len(valori)):
			for j in range(len(valori)):
				if valori[i]==valori[j] and i!=j:
					preturi.add(valori[i])
					tva.add(0)
					total.add(valori[j])
		for i in range(len(valoriMari)):
			for j in range(len(valoriMari)):
				if valoriMari[i]==valoriMari[j] and i!=j:
					preturi.add(valoriMari[i])
					tva.add(0)
					total.add(valoriMari[j])				
	for i in valori:
		for j in valori:
			for k in valori:
				if i+j==k and min(i,j,k)>0.15 * max(i,j,k) and min(i,j,k) <0.17 * max(i,j,k):
					tva.add(min(i,j,k))
					total.add(max(i,j,k))
					auxlst.append(i)
					auxlst.append(j)
					auxlst.append(k)
					auxlst.remove(min(i,j,k))
					auxlst.remove(max(i,j,k))
					preturi.add(auxlst[0])
					auxlst=[]
	if len(ints2)>0:
		for i in valoriMari:
			for j in valoriMari:
				for k in valoriMari:
					if (k-i-j>(-0.1) and k-i-j<0.1) and min(i,j,k)>0.15 * max(i,j,k) and min(i,j,k) <0.17 * max(i,j,k):
						tva.add(min(i,j,k))
						total.add(max(i,j,k))
						auxlst.append(i)
						auxlst.append(j)
						auxlst.append(k)
						auxlst.remove(min(i,j,k))
						auxlst.remove(max(i,j,k))
						preturi.add(auxlst[0])
						auxlst=[]				
						#print(i,j,k)
	if  preturi==set([]):			
		for i in valori:
			for j in valori:
				if i>0.84*j and i<0.85*j:
					preturi.add(i)
					total.add(j)
					tva.add(round((j-i),2))
				if i>0.185 * j and i<0.21*j:
					preturi.add(j)
					tva.add(i)
					tva.add(round((j-i),2))
	boxes_list=[]				
	print('---------------------')
	print(valoriMari)
	print('---------------------')
	boxes_data=pytesseract.image_to_boxes(Image.open(ImagineFactura))
	boxes_lines=boxes_data.splitlines()
	allLines=all.splitlines()
	#print(all.replace('\n',';'))
	#print(allLines)
	printThisLineToo=0;
	for lineIt in allLines:
		if len(lineIt)>1:
			if 'enumire' in lineIt or (lineIt[0].isdigit() and not lineIt[1].isdigit() and lineIt[1]!=','):
				print (lineIt)
				bucatiJson.append(lineIt)
				printThisLineToo=1
			else:
				if printThisLineToo==1:
					print(lineIt)
					bucatiJson.append(lineIt)
				printThisLineToo=0

				
	print('-------------------Hello')
	'''
	for myPars in boxes_lines:
			#print(myPars[0:22])
			print(int(re.search(r'\d+', myPars[1:]).group()),myPars)
			#print(myPars[0],myPars[1],myPars[2],myPars[3],myPars[4],myPars[5])
	'''

	for boxLine in boxes_lines:
		auxSplit=boxLine.split(' ')
		boxes_list.append(auxSplit)

	currMinY=0
	currMaxY=0
	diffMeanMaxMinY=0
	sumMaxMinY=0
	currMinX=0
	currMaxX=0
	diffMeanMaxMinX=0
	sumMaxMinX=0
	countDifferences=0
	fromHereOn=1000000
	for myIterator in range(len(boxes_list)):
		sumMaxMinY=sumMaxMinY+int(boxes_list[myIterator][4])-int(boxes_list[myIterator][2])
		countDifferences=countDifferences+1
		sumMaxMinX=sumMaxMinX+int(boxes_list[myIterator][3])-int(boxes_list[myIterator][1])
		countDifferences=countDifferences+1	
		if countDifferences!=0:
			diffMeanMaxMinY=sumMaxMinY/countDifferences
			diffMeanMaxMinX=sumMaxMinX/countDifferences

	for myIterator in range(len(boxes_list)-10):
		if int(boxes_list[myIterator][2])>100 and int(boxes_list[myIterator][2])<1500:
			if currMinY==0:
				currMinY=int(boxes_list[myIterator][2])
				currMaxY=int(boxes_list[myIterator][4])
			if currMinY-diffMeanMaxMinY>int(boxes_list[myIterator][2]) or currMinY+diffMeanMaxMinY<int(boxes_list[myIterator][2]):
				currMinY=int(boxes_list[myIterator][2])
				currMaxY=int(boxes_list[myIterator][4])
				print(" ")
			#if currMinY<=int(boxes_list[myIterator][2]) and currMaxY>=int(boxes_list[myIterator][2]):
			if myIterator != 0:
				if int(boxes_list[myIterator][1])-int(boxes_list[myIterator-1][1])>2*diffMeanMaxMinX:
					print("   ",end='')
			#if int(boxes_list[myIterator][2])>=fromHereOn:
				#print(boxes_list[myIterator][0], end='')
			#print(boxes_list[myIterator][0], end='')
		#if boxes_list[myIterator][0]=='S'  and boxes_list[myIterator+4][0]=='a' and boxes_list[myIterator+8][0]=='a':
			#print(boxes_list[myIterator][0],boxes_list[myIterator+1][0],boxes_list[myIterator+2][0])
		if boxes_list[myIterator][0]=='e'  and boxes_list[myIterator+3][0]=='m' and boxes_list[myIterator+6][0]=='e' and fromHereOn==1000000:		
			fromHereOn=int(boxes_list[myIterator][2])
	print('From here on------------')
	for myIterator in range(2,len(boxes_list)):
		if int(boxes_list[myIterator][2])<=fromHereOn:
			if abs(int(boxes_list[myIterator][2])-int(boxes_list[myIterator-1][2]))>2*diffMeanMaxMinY:
				print(" ")
			if abs(int(boxes_list[myIterator][1])-int(boxes_list[myIterator-1][1]))>1.2*diffMeanMaxMinX:
				print("",end=" ")	
			print(boxes_list[myIterator][0], end='')
	print('Till here------------')
	rows=[]
	rowsaux=[]
	rowHeight=60
	for valMin in range(55):
		for box_num in range(len(boxes_list)):
			if int(boxes_list[box_num][2])>valMin*rowHeight and int(boxes_list[box_num][2])<valMin*rowHeight+rowHeight:
				if box_num>1 and (int(boxes_list[box_num][1])-int(boxes_list[box_num-1][1])>82):
					print('', end=' ')
				#print(boxes_list[box_num][0],end='')
				rowsaux.append(boxes_list[box_num][0])
		rows.append(''.join(rowsaux))
		rowsaux=[]
		print(' ')
	myRegExp="(numarul de factura)|(Factura)|(factura)|(Nr. Factura)|(Nr. Facturii)|(Nr. facturii)|(Seria[ ]{0,2}si[ ]{0,2}numarul[ ]{0,2}facturii)"
	myRegExpCif="(CIF:?)|(CNP)|(cif)|(cnp)|(CUI)|(cui)|(C.U.I)|(c.u.i)|(Cod TVA)"
	#myRegExpData="((data facturii)|(data fact)|(fact data)|(data facturii)|(data emitere)|(data emiterii)|(emisa la)|(data))[ :]{0,10}[0-9]{0,2}[/\.][0-9]{0,2}[/\.][0-9]{2,4}"
	myRegExpData="(la data de|din data de|\(zi[,/\.]luna[,/\.]an\)|\(ziua[,/\.]luna[,/\.]anul\)|data[ ]{0,4}emiterii[ ]{0,4}facturii|data[ ]{0,4}emiterii[ ]{0,4}factura|data[ ]{0,4}facturii|data[ ]{0,4}fact|fact[ ]{0,4}data|data[ ]{0,4}factura|data[ ]{0,4}emitere|data[ ]{0,4}emiterii|emisa[ ]{0,4}la|data|Data)[ :@]{0,10}([0-9]{2}[-\/.][0-9]{2}[-\/.][0-9]{2,4})"
	facturaRows=[]
	facturaRowsSpecCase=[]
	print(preturi)
	cifList=[]
	dateList=[]
	for row in rows:
		if re.search('(FACTURA)|(FACT)',row):
			facturaRowsSpecCase.append(row)
		if re.search(myRegExp,row,re.IGNORECASE):
			if re.search("(Nr)|(Numar)|(Num)|(nr)|(num)|(numar)",row):	
				if len(re.findall(r"\d+",row)):
					numFact=int(re.findall(r"\d+",row)[0])
			else:
				if 	len(re.findall(r"\d+",row))>0:
					numFact=int(re.findall(r"\d+",row)[0])
		if re.findall(myRegExpCif,row):
			if len(re.findall(r"\d+",row))>0:
				cif=re.findall(r"\d+",row)[0]
			cifX=re.findall("RO[0-9]+",row)
			for a in cifX:
				if a:
					cif=a
					cifList.append(a)
			cifList.append(cif)
			cifX=''
		if re.search(myRegExpData,row,re.IGNORECASE):
			dataRows=re.search(myRegExpData,row,re.IGNORECASE).groups()
			print(dataRows)
			print('XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD')
			#for dataRow in dataRows:
			if dataRows!='':
				dateList.append(dataRows[-1])
	print('List of cif',cifList)
	print('List of dates',dateList)
	if numFact==0 and len(facturaRowsSpecCase)>0:
		numFact=facturaRowsSpecCase[0].replace('FACTURA','')

	print('factRows',facturaRows)
	print('dateX',dateX)
	print('data',numFact)
	if nrFound==1:
		print('Nr. factura:',dateX.group())
	else:
		print('Factura Nr.',numFact)
	if(len(dateList)==0):
		print('(unsure)Data facturii:',data)
	else:
		print('Data facturii:',dateList[0])
	cifSet=set([])
	for a in cifList:
		if a:
			cifSet.add(a)
	#print('Set of cif',cifSet,len(cifSet))
	if len(cifSet)>0:
		print('CIF/CNP/CUI#1:',cifSet.pop())
	if len(cifSet)>0:
		print('CIF/CNP/CUI#2:',cifSet.pop())
	if adrFound==1:
		print(addrX.group())
	else:
		print('Adresa:',adresa)
	if len(preturi)>0:
		print('pret=',max(preturi))
		pretAfisat = max(preturi)
	if len(preturi)>0 and len(total)>0:
		if max(preturi)!=max(total):
			tvaAfisat=max(tva)
			print('tva=',max(tva))
		else:
			tvaAfisat=0
			print('tva=0')
		print('total=',max(total))
	if tvaAfisat==0:
		print('Cota TVA:0%');
	elif 0.19*pretAfisat - tvaAfisat > (-0.1) and 0.19*pretAfisat - tvaAfisat < 0.1:
		print('Cota TVA:19%');
	elif 0.9*pretAfisat - tvaAfisat > (-0.1) and 0.9*pretAfisat - tvaAfisat < 0.1:
		print('Cota TVA:9%');
	elif 0.5*pretAfisat - tvaAfisat > (-0.1) and 0.5*pretAfisat - tvaAfisat < 0.1:
		print('Cota TVA:5%');	
	else:
		print('Cota TVA:not found');
	#print(rows)
	print('factRows',facturaRows)
	print('------------------------------------------')
	if nrFound==1:
		print('Nr. factura:',dateX.group())
	else:
		print('Factura Nr.',numFact)
	textNrFact=tk.Label( text='Factura numărul ' + str(numFact))
	textNrFact.pack()
	print('Verified CIF set:',my2ndCifSet)
	print('CNP list:',myCNPSet)
	if adrFound==1:
		print(addrX.group())
	else:
		print('Adresa:',adresa)
	if len(preturi)>0:
		print('pret=',max(preturi))
		pretAfisat = max(preturi)
	if len(preturi)>0 and len(total)>0:
		if max(preturi)!=max(total):
			tvaAfisat=max(tva)
			print('tva=',max(tva))
		else:
			tvaAfisat=0
			print('tva=0')
		print('total=',max(total))
	printedCotaTva=0
	if len(total)==0 and len(valori)>0:
		print('pret=',max(valori))
		print('tva=',0)
		print('total=',max(valori))
		print('Cota tva:',0)
		printedCotaTva=1

		
	if tvaAfisat==0:
		print('Cota TVA:0%');
	elif 0.19*pretAfisat - tvaAfisat > (-0.1) and 0.19*pretAfisat - tvaAfisat < 0.1:
		print('Cota TVA:19%');
	elif 0.9*pretAfisat - tvaAfisat > (-0.1) and 0.9*pretAfisat - tvaAfisat < 0.1:
		print('Cota TVA:9%');
	elif 0.5*pretAfisat - tvaAfisat > (-0.1) and 0.5*pretAfisat - tvaAfisat < 0.1:
		print('Cota TVA:5%');	
	else:
		if printedCotaTva==0:
			print('Cota TVA:not found');
	lastSetTVA=set([])
	lastSetTotal=set([])
	lastResortSet=set([])
	for i in valori:
		lastResortSet.add(i)
	for i in lastResortSet:
		for j in lastResortSet:
			if (i>0.189*j and i<0.191*j) or (i>0.089*j and i<0.091*j) or (i>0.049*j and i<0.051 * j):
				lastSetTVA.add(i)
				lastSetTotal.add(j)
	if len(lastSetTVA)>0:
		print('-----------------------------------')
		print('If pret missing')
		print('TVA:',max(lastSetTVA))
		print('Pret:',max(lastSetTotal))
		
	print('-----------------------------------')
	seriaGasita=re.search(r"seri[ae][0-9a-zA-Z ]{0,9}numar(ul)?( ?factura| ?facturii)?[ 0-9]{0,9}|seri[ae][0-9a-zA-Z ]{0,9}nr( ?factura| ?facturii)?[., ]?[ul]?[ 0-9]{0,9}",all,re.IGNORECASE);
	if seriaGasita:
		print(seriaGasita.group(0))

		

		
		

		
	pretJson=0
	tvaJson=0
	totalJson=0
	importantInformation=[]
	if len(preturi)>0 and len(tva)>0 and len(total)>0:
		if round((max(preturi)+max(tva)),2) in total or round((max(total)-max(preturi)),2) in tva or  max(total)+max(preturi) in tva:
			pretJson=max(preturi)
			tvaJson=max(tva)
			totalJson=max(total)
			importantInformation.append(("Pret: ",max(preturi)))
			importantInformation.append(("Tva: ",max(tva)))
			importantInformation.append(("Total: ",max(total)))
	elif len(total)==0 and len(valori)>0:
		pretJson=max(valori)
		tvaJson=0
		totalJson=max(valori)
		importantInformation.append(("Pret: ",max(valori)))
		importantInformation.append(("Tva: ",0))
		importantInformation.append(("Total: ",max(valori)))
	elif len(lastSetTVA)>0:
		pretJson=max(lastSetTotal)
		tvaJson=max(lastSetTVA)
		totalJson=round(max(lastSetTotal)+max(lastSetTVA),2)
		

	if nrFound==1:
		nrFactJson=dateX.group()
	elif numFact:
		nrFactJson=numFact
	elif seriaGasita:
		nrFactJson=seriaGasita.group(0)	

	cifOrCnpJson=[]
	if len(my2ndCifSet)==2:
		cifOrCnpJson.append(list(my2ndCifSet)[0])
		cifOrCnpJson.append(list(my2ndCifSet)[1])

	cifsWithRo=[]
	cifsWithoutRo=[]
	for myCifIt in my2ndCifSet:
		if myCifIt[0]=='R' and myCifIt[1]=='O':
			cifsWithRo.append(myCifIt)
		else:
			cifsWithoutRo.append(myCifIt)
	
	if len(cifsWithRo)>=2:
		cifOrCnpJson=cifsWithRo
	elif len(cifsWithRo)==1:
		cifOrCnpJson.append(cifsWithRo[0])
		if len(cifsWithRo)>=2:
			if cifsWithRo[0][2:]==cifsWithoutRo[0]:
				cifOrCnpJson.append(cifsWithoutRo[1])
			else:
				cifOrCnpJson.append(cifsWithoutRo[0])
	elif len(cifsWithoutRo)>=2:
		cifOrCnpJson.append(cifsWithoutRo[0])
		cifOrCnpJson.append(cifsWithoutRo[1])
	elif len(cifsWithoutRo)==1:
		cifOrCnpJson.append(cifsWithoutRo[0])
		if len(myCNPSet)>=1:
			cifOrCnpJson.append(list(myCNPSet)[0])

	if(len(dateList)==0):
		dataJson=data
	else:
		dataJson=dateList[0]
		
	if tvaJson==0:
		cotaTvaJson=0
	else:
		cotaTvaJson=round((tvaJson/pretJson)*100,0)
	print("------------------------")
	print("Informații importante")
	print("Nr.fact:",nrFactJson)
	print("Data facturii:",dataJson)
	if len(cifOrCnpJson)>=2:
		print("\nCIF 1: ",cifOrCnpJson[0])
		print("CIF 2: ",cifOrCnpJson[1])
	elif len(cifOrCnpJson)==1:	
		print("CIF 1: ",cifOrCnpJson[0])
	print("\nPreț ",pretJson)
	print("TVA ",tvaJson)
	print("Total ",totalJson)
	print("\nCota TVA:",cotaTvaJson,"%")
	#print(preturi,tva,total)
	print("---------------------------------")
	print("Informații mai puțin importante")

	if adrFound==1:
		adrJson=addrX.group()
	else:
		adrJson=adresa
	print(adrJson)
	print("----------------------------------")
	print("Informatii pe bucată")
	for bucJs in bucatiJson:
		print(bucJs)


		
		
	f1 = open("myOutput"+str(fileIteratStart)+".txt", "w")
	fileIteratStart+=1
	f1.write("------------------------\n")
	f1.write("Informatii importante\n")
	f1.write("Nr.fact:%s\n"%nrFactJson)
	f1.write("Data facturii:%s\n"%dataJson)
	if len(cifOrCnpJson)>=2:
		f1.write("\nCIF 1: %s\n"%cifOrCnpJson[0])
		f1.write("CIF 2: %s\n"%cifOrCnpJson[1])
	elif len(cifOrCnpJson)==1:	
		f1.write("CIF 1: %s\n"%cifOrCnpJson[0])
	f1.write("\nPret %s\n"%pretJson)
	f1.write("TVA %s\n"%tvaJson)
	f1.write("Total %s\n"%totalJson)
	f1.write("\nCota TVA:%s\n"%cotaTvaJson)
	#print(preturi,tva,total)
	f1.write("---------------------------------\n")
	f1.write("Informatii mai putin importante\n")

	if adrFound==1:
		adrJson=addrX.group()
	else:
		adrJson=adresa
	f1.write(adrJson)
	f1.write("\n")
	f1.write("----------------------------------\n")
	f1.write("Informatii pe bucata\n")
	for bucJs in bucatiJson:
		f1.write(bucJs)
		f1.write('\n')
	f1.close()



#print(all)
#print(preturi2)
#print(total2)
#print(tva2)
#print(rows)
#m.mainloop() 