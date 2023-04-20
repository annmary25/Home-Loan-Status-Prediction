import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

# Route for a homepage

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            Gender = request.form.get('Gender'),
            Married = request.form.get('Married'),
            Dependents = request.form.get('Dependents'),
            Education = request.form.get('Education'),
            Self_Employed = request.form.get('Self_Employed'),
            ApplicantIncome = int(request.form.get('ApplicantIncome')),
            CoapplicantIncome = float(request.form.get('CoapplicantIncome')),
            LoanAmount = float(request.form.get('LoanAmount')),
            Loan_Amount_Term = float(request.form.get('Loan_Amount_Term')),
            Credit_History = float(request.form.get('Credit_History')),
            Property_Area = request.form.get('Property_Area')
        )
        predicted_dataframe = data.get_data_as_dataframe()
        print(predicted_dataframe)
        
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(predicted_dataframe)
        if results == 0:
            result = "SORRY, Your loan is not approved!!!"
        else:
            result = "CONGRAGULATIONS, Your loan is approved!!!"
        return render_template('home.html',results=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
