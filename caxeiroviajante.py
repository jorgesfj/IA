from random import randint

def cidades():
	a = [20,20]
	b = [40,30]
	c = [30,50]
	d = [70,60]
	e = [90,30]
	allcity = [a,b,c,d,e]
	return allcity


def random_cromossomo(allcity):
	listaindi = []
	cont = 0
	prim = allcity[randint(0,4)]
	listaindi.append(prim)
	sec = allcity[randint(0,4)]
	ter = allcity[randint(0,4)]
	quar = allcity[randint(0,4)]
	quin = allcity[randint(0,4)]
	while sec in listaindi:
		sec = allcity[randint(0,4)]
	listaindi.append(sec)
	while ter in listaindi:
		ter = allcity[randint(0,4)]
	listaindi.append(ter)
	while quar in listaindi:
		quar = allcity[randint(0,4)]
	listaindi.append(quar)
	while quin in listaindi:
		quin = allcity[randint(0,4)]
	listaindi.append(quin)
	return listaindi

def random_populacao():
	cont = 0
	lista = []
	while cont<30:
		a = random_cromossomo(cidades())
		while a in lista:
			a = random_cromossomo(cidades())
		lista.append(a)
		cont+=1
	return lista

def distancia2pt(x1,x2,y1,y2):
	dbp = (((x2-x1)**2) + ((y2-y1)**2))**(1/2)
	return dbp
 
def funcapt(lista):
	lista_distancias = []
	for i in range(len(lista)):
		aux = 0
		for j in range(len(lista[i]) - 1):
			distancia2pt = (((lista[i][j][1]- lista[i][j][0])**(2)) + ((lista[i][j+1][1]- lista[i][j+1][0])**(2))) **(0.5)
			aux  = aux + distancia2pt
		lista_distancias.append(float("{:.2f}".format(aux)))
	return lista_distancias
def valorviagem(lista):
	listavalor = []
	for i in range(len(lista)):
		listavalor.append(float(lista[i])*0.5)

	return listavalor

print(random_populacao())
print(funcapt(random_populacao()))
