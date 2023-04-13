import os
import sys
import numpy as np
import pandas as pd

from dataclasses import dataclass
from src.logger import logging
from src.utils import save_object
from src.exception import CustomException

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self, df):
        # Data Transformation
        try:
            # Dropping unwanted columns
            df.drop(['Loan_ID'], axis=1, inplace=True)
            
            # Handling missing values
            df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].median())
            df['Self_Employed'] = df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])
            df['Dependents'] = df['Dependents'].fillna(df['Dependents'].mode()[0])
            df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
            df['Married'] = df['Married'].fillna(df['Married'].mode()[0])
            df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].mean())
            df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mean()) 
            
            Y = df.Loan_Status
            Y = np.where(Y == 'Y', 1, 0)
            X = pd.get_dummies(df.drop('Loan_Status',axis=1), drop_first = True)           
 
            scaler = StandardScaler()
            # Fit the scaler to the features
            scaler.fit(X)

            # Transform the features using the scaler
            X = scaler.transform(X)

            return X,Y
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Completed reading train & test data")
            
            input_feature_train_arr, target_feature_train_df = self.get_data_transformer_object(train_df)
            input_feature_test_arr, target_feature_test_df = self.get_data_transformer_object(test_df)
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info("Saved preprocessing object.")
            '''
            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
            '''
            return train_arr, test_arr
            
            #return input_feature_train_arr, target_feature_train_df, input_feature_test_arr, target_feature_test_df
        except Exception as e:
            raise CustomException(e,sys)
