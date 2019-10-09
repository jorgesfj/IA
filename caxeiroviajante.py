from random import randint

def cidades():
	a = [20,20]
	b = [40,30]
	c = [30,50]
	d = [70,60]
	e = [90,30]
	allcity = [a,b,c,d,e]
	return allcity


def gerarpopin():
	lista = cidades()
	cont = 0
	listafin = []
	while cont<30:
		listaindi = []
		prim = lista[randint(0,4)]
		listaindi.append(prim)
		sec = lista[randint(0,4)]
		ter = lista[randint(0,4)]
		quar = lista[randint(0,4)]
		quin = lista[randint(0,4)]
		while sec in listaindi:
				sec = lista[randint(0,4)]
		listaindi.append(sec)
		while ter in listaindi:
				ter = lista[randint(0,4)]
		listaindi.append(ter)
		while quar in listaindi:
				quar = lista[randint(0,4)]
		listaindi.append(quar)
		while quin in listaindi:
				quin = lista[randint(0,4)]
		listaindi.append(quin)
		if listaindi is not listafin:
			listafin.append(listaindi)
		cont+=1
	return listafin

def distancia2pt(x1,x2,y1,y2):
	dbp = (((x2-x1)**2) + ((y2-y1)**2))**(1/2)
	return dbp

def funcapt(lista):
	lista2 = []
	for i in range(len(lista)):
		aux = 0
		for j in range(len(lista[i])-1):
			var = distancia2pt(lista[i][j][0],lista[i][j+1][0],lista[i][j][1],lista[i][j+1][1])
			aux = aux + var
		lista2.append("{:.2f}".format(aux))
	return lista2

for i in range(len(gerarpopin())):
	print(gerarpopin()[i])
