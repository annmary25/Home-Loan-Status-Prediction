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

## Project Approach

#### Data Ingestion 

- The dataset is read and split into training and testing.
- The raw dataset, training dataset and test dataset is saved as csv file in `artifacts` folder.

#### Data Analysis
- 68 % of loans are approved 
- 60% of the applicants income lies between 25000 to 60000 
- 45% of the coapplicant income is 0
- 50% of the totalincome lies between 40000 and 75000
- 60% of the loan amount lies in between 10 lakh and 20 lakh 
- Maximum loan amount is 70 Lakh
- Loan amount tenure opted by 83% of applicants is 360 months ie. 30 years
- Applicants with credit history has higher chance of getting loan than applicants without credit hitory. 
- 80% of applicants whose loan got approved has credit history
- Loan was rejected for 92% of applicants who did not have credit history
- 81% of loan applicants are male but there isnt any considerable difference between the loans approved to men and women
- 65% of loan applicants are married and there is 68% chance that a loan is approved for a married applicant
- 58% loan applicants does not have dependents
- 78% of loan applicants are graduates and the employment status % of graduates and not graduates are the same.
- 80% of people whose loan got approved are graduates
- 85% of loan applicants are not self employed
- The % of loan approved for self employed people and employees is same
- There isn't a considerable difference in the property area however 37% of the property is in semi urban area.

#### Data Transformation

- A ColumnTransformer Pipeline is created.
- for Numeric Variables first SimpleImputer is applied with strategy mean , then Standard Scaling is performed on numeric data.
- for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
- This preprocessor is saved as pickle file.

#### Model Training 

- In this phase multiple models were trained and after performing hyperparameter tuning, the best model was chosen. 
- This model is saved as pickle file.

#### Prediction Pipeline 

- The pipeline converts the custom data into dataframe and predict the outcome based on the model chosen.

#### Model deployment

- Constructed a Flask web application with a Home Loan Status Prediction model to predict loan approvals and rejections and decreased loan approval time by 90% 
- Dockerized the application, implemented a CI/CD pipeline, and deployed the app on Azure
