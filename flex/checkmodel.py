from sklearn.externals import joblib

clf = joblib.load('mymodel.pkl')
print clf.predict([1,1,1,1,1,1,1,1,1])