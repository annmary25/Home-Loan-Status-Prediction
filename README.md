# Home Loan Status Prediction

## Project Overview

Business Understanding: Currently processing home loan application is done manually and it takes about 2-3 days to inform the applicant whether loan is approved or not.

Business Objective: Reduce the time taken to inform the applicants about home loan status

Hypothesis: Develop a machine learning model that can accurately predict whether a loan application is approved or rejected with less amount of time

## Solution

Constructed a Flask web application with a Home Loan Status Prediction model that leveraged machine learning algorithms to predict loan approvals and rejections and decreased loan approval time by 90% 

Dockerized the application, implemented a CI/CD pipeline, and deployed the app on Azure

## Dataset

The dataset consists of 12 independant variables and 1 dependant variable

#### Independant Variables:

- `Loan_ID` - unique identifier for each loan
- `Gender` - Gender of the loan applicant
- `Education` - Education status of the applicant. Whether the applicant is graduated or not
- `Self_Employed` - Whether the applicant is self employed or not
- `Married` - Marital status of the loan applicant
- `Dependents` - Number of dependents for the loan applicant
- `Property_Area` - Property area type of the applicant 
- `ApplicantIncome` - Monthly gross income of the applicant
- `CoapplicantIncome` - Monthly gross income of the Coapplicant
- `LoanAmount` - Loan amount needed by the applicant
- `Loan_Amount_Term` - Loan amount term required by the applicant (In months)
- `Credit_History` - Credit history of the applicant

#### Dependant variable:

- `Loan_Status` - Indicates if the loan is approved or rejected

_**Link to data used in the project**_ - https://github.com/annmary25/Home-Loan-Status-Prediction/blob/main/data.csv

## Demo

https://user-images.githubusercontent.com/47209907/233424931-c8f31a36-b53d-49be-bcd5-235375c94bb0.mov



https://user-images.githubusercontent.com/47209907/233424944-48b39b37-3e26-4866-9b03-55292f61d8c1.mov

## Run Project locally 

#### Using github

- Clone the complete project using `git clone https://github.com/annmary25/Home-Loan-Status-Prediction.git`
-  Complete the following steps inside the directory `Home-Loan-Status-Prediction`
    - Create python3 virtual environment using `virtualenv -p python3 {name_of_environment}`
    - Activate the environment using `source {path_to_virtual_environment}/bin/activate`
    - Install the dependencies using `pip install -r requirements.txt`
    - Finally run the project using `python app.py`

#### Using Docker

Dockerhub link: https://hub.docker.com/repository/docker/annmary25/home-loan-status-prediction/general

- Pull the code using `docker pull annmary25/home-loan-status-prediction:main`
- Run the project using `python app.py`

## Project Approach

#### Data Ingestion 

- The dataset is read and split into training and testing.
- The raw dataset, training dataset and test dataset is saved as csv file in `artifacts` folder.

#### Data Analysis

- 68 % of loans are approved 
- 78 % of the loan applicants were graduates
- 80% of loan applicants are men but there isn’t a significant difference in the percentage of loans approved for men and women
- The average income of self employed people are more than people who are not self employed
- 60% of loan applicants does not have dependents
- People with credit history have higher chance of getting loan than people without credit history
 
#### Data Transformation

- A ColumnTransformer Pipeline is created.
- for Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
- for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
- This preprocessor is saved as pickle file.

#### Model Training 

- In this phase base model is tested . The best model found was catboost regressor.
- After this hyperparameter tuning is performed on catboost and knn model.
- A final VotingRegressor is created which will combine prediction of catboost, xgboost and knn models.
- This model is saved as pickle file.

#### Prediction Pipeline 

- This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

#### Model deployment

- Constructed a Flask web application with a Home Loan Status Prediction model to predict loan approvals and rejections and decreased loan approval time by 90% 
- Dockerized the application, implemented a CI/CD pipeline, and deployed the app on Azure
