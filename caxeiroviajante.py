from random import randint

def cidades():
	a = [20,20]
	b = [40,30]
	c = [30,50]
	d = [70,60]
	e = [90,30]
	allcity = [a,b,c,d,e]
	return allcity


def random_cromossomo():
	listafin = []
	listaindi = []
	prim = cidades()[randint(0,4)]
	listaindi.append(prim)
	sec = cidades()[randint(0,4)]
	ter = cidades()[randint(0,4)]
	quar = cidades()[randint(0,4)]
	quin = cidades()[randint(0,4)]
	while sec in listaindi:
		sec = cidades()[randint(0,4)]
	listaindi.append(sec)
	while ter in listaindi:
		ter = cidades()[randint(0,4)]
	listaindi.append(ter)
	while quar in listaindi:
		quar = cidades()[randint(0,4)]
	listaindi.append(quar)
	while quin in listaindi:
		quin = cidades()[randint(0,4)]
	listaindi.append(quin)

	if listaindi is not listafin:
		listafin.append(listaindi)
	return listafin

#def random_populacao:


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

def valorviagem(lista):
	#para cada metro ele gasta 0.50 centavos
	listavalor = []
	for i in range(len(lista)):
		listavalor.append(float(lista[i])*0.5)

	return listavalor

a = valorviagem(funcapt(random_cromossomo()))
for i in range(len(a)):
	print(a[i])