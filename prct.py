import pickle

with open("classifier.pkl", "rb") as f:
    classifier = pickle.load(f, fix_imports=True, encoding="latin1")
    print(classifier)