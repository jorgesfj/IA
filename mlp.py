from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
import csv
lista = []

arquivo = open('valorsin.csv')
linhas = csv.reader(arquivo)
lista = []
for linha in linhas:
	l = []
	for i in range(len(linha)):
		l.append(float(linha[i]))
	lista.append(l)
X = lista

arquivo = open('valorout.csv')
linhas = csv.reader(arquivo) 
lista = []
for linha in linhas:
	for i in range(len(linha)):
		lista.append(float(linha[i]))

y= lista

print(X)
print(y)
clf = MLPRegressor(hidden_layer_sizes=(100, ), activation='relu', solver='adam', alpha=0.0001, batch_size='auto', 
	learning_rate='constant', learning_rate_init=0.001, power_t=0.5, max_iter=200, shuffle=True, random_state=None, tol=0.0001, 
	verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True, early_stopping=False, validation_fraction=0.1, 
	beta_1=0.9, beta_2=0.999, epsilon=1e-08, n_iter_no_change=10)
#clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
#                    hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X, y)
print(clf.predict([[59.99,60.00,76.3,83.4,78.35,64.36,70.6,59.99,70.04,89.8,113.2,81.8,92.2,72.38,85.9,92.2,88.7,96.9]]))