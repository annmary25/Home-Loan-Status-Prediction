# Home Loan Status Prediction

## Project Overview
Business Understanding: Currently processing home loan application is done manually and it takes about 2-3 days to inform the applicant whether loan is approved or not.

Business Objective: Reduce the time taken to inform the applicants about home loan status

Hypothesis: Develop a machine learning model that can accurately predict whether a loan application is approved or rejected with less amount of time

## Solution
Constructed a Flask web application with a Home Loan Status Prediction model that leveraged machine learning algorithms to predict loan approvals and rejections and decreased loan approval time by 90% 

Dockerized the application, implemented a CI/CD pipeline, and deployed the app on Azure

## Dataset
The dataset consisted of 12 independant variables and 1 dependant variable
#### Independant Variables:
- `Loan_ID` - unique identifier for each loan
- `Gender` - Gender of the loan applicant
- `Married` - Marital status of the loan applicant
- `Dependents` - Number of dependents for the loan applicant
- `Education` - Education status of the applicant. Whether the applicant is graduated or not
- `Self_Employed` - Whether the applicant is self employed or not
- `ApplicantIncome` - Monthly gross income of the applicant
- `CoapplicantIncome` - Monthly gross income of the Coapplicant
- `LoanAmount` - Loan amount needed by the applicant
- `Loan_Amount_Term` - Loan amount term required by the applicant (In months)
- `Credit_History` - Indicates whether the applicant has good credit history or not
- `Property_Area` - Whether the property area is Urban, Semi-urban or Rural
#### Dependant variable:
- `Loan_Status` - Indicates if the loan is approved or rejected

Link to data used in the project - https://github.com/annmary25/Home-Loan-Status-Prediction/blob/main/data.csv

## Demo

https://user-images.githubusercontent.com/47209907/233424931-c8f31a36-b53d-49be-bcd5-235375c94bb0.mov



https://user-images.githubusercontent.com/47209907/233424944-48b39b37-3e26-4866-9b03-55292f61d8c1.mov

## Project Approach

#### Data Ingestion 
- The data is read as csv and then split into training and testing and saved as csv file.

#### Data Analysis
- % of loan approved - 68 
- People with credit history have higher chance of getting loan than people without credit history
- Loans are applied more by men but there isn’t a difference in the percentage of loans approved for men and women
- The average income of self employed people are more than people who are not self employed
- About 60% of loan applicants does not have dependents

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

Dockerhub link: https://hub.docker.com/repository/docker/annmary25/home-loan-status-prediction/general



