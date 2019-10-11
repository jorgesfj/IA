from sklearn.neural_network import MLPClassifier
#X = [[0., 0.], [1., 1.]]
X = [[35.76,35.5,35.22,34.95,34.62,34.28,33.93,33.57,33.22,32.89,32.58,32.25,31.93,31.65,31.4,31.15],[35.5,35.22,34.95,34.62,34.28,33.93,33.57,33.22,32.89,32.58,32.25,31.93,31.65,31.4,31.15,30.91]]
y = [31, 30]
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X, y)
print(clf.predict([[35.22,34.95,34.62,34.28,33.93,33.57,33.22,32.89,32.58,32.25,31.93,31.65,31.4,31.15,30.91,30.67]]))