from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
from sklearn import preprocessing
import numpy as np

with open("signdata.txt", "r") as f:
    data = f.readlines()

clean_data = []
X = []
Y = []
for line in data:
    try:
        row = map(int, line.strip().split())
        if len(row) != 10:
            continue
        clean_data.append(row)
        X.append(np.array(row[:-1]))
        Y.append(row[-1])
    except:
        pass
# print clean_data
clf = svm.SVC(kernel='linear', C=1.0)
Y = np.array(Y)
# print len(X), len(Y)
# print X[0]
# print Y[0]
# X = preprocessing.scale(X)
clf.fit(X, Y)
joblib.dump(clf, 'mymodel.pkl')
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

# clf.fit(X_train, Y_train)

# Y_pred = clf.predict(X_test)
# print accuracy_score(Y_test, Y_pred)