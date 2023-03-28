import uvicorn
from fastapi import FastAPI
from LoanStatusPrediction import LoanStatusPrediction
import numpy as np
import pickle
import pandas as pd

import joblib 

app = FastAPI()
#pickle_in = open("classifier.pkl","rb")
#classifier=pickle.load(pickle_in)


#joblib.dump(ds, "model.pkl") 
classifier = joblib.load('model.pkl' ) 
#model.predict(X_test)

@app.post('/predict')
def predict_banknote(data:BankNote):
    data = data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0] == 1):
        prediction="Loan Approved"
    else:
        prediction="Loan rejected"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
