import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd

# pickle_in = open("classifier.pkl", "rb")
# classifier = pickle.load(pickle_in)
with open("classifier.pkl", "rb") as f:
    classifier = pickle.load(f, fix_imports=True, encoding="latin1")
print("***************************************************************")
print(classifier)
app  = FastAPI()

@app.get('/')
def index():
    return {'message': "Hello World"}

@app.get('/{name}')
def get_name(name:str):
    return {'my name is ' : f"{ name}"}

@app.post('/predict')
def predict_species(data:BankNote):
    data= data.dict()
    print(data)
    variance = data["variance"]
    print(variance)
    skewness = data["skewness"]
    curtosis = data['curtosis']
    entropy = data['entropy']
    # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    if (prediction[0]> 0.5):
        prediction = "Fake Note"
    else:
        prediction = "It's a bank note"
    
    return {
        'pridiction' : prediction
            }


 
if __name__ == "__main__":

    uvicorn.run(app,host='127.0.0.1',port=8000)
    #uvicorn main:app --reload



