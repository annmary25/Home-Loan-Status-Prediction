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

    def get_data_transformer_object(self):
        # Data Transformation
        try:
            numerical_columns = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", "Credit_History"]
            categorical_columns = ["Gender", "Married", "Dependents", "Education", "Self_Employed", "Property_Area"]

            numerical_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="mean")),
                    ("scalar", StandardScaler())
                ]
            )
            logging.info("Standard scaling of numerical columns is completed")

            categorical_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scalar", StandardScaler(with_mean=False))
                ]
            )
            logging.info("Encoding of categorical columns is completed")

            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline", numerical_pipeline, numerical_columns),
                    ("categorical_pipeline", categorical_pipeline, categorical_columns)
                ]
            )
            logging.info("Completed column transformation")
            
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Completed reading train & test data")

            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "Loan_Status"
            
            input_feature_train_df = train_df.drop(columns=[target_column_name, "Loan_ID"], axis=1)
            target_feature_train_df = train_df[target_column_name]
            target_feature_train_df = np.where(target_feature_train_df == 'Y', 1, 0)

            input_feature_test_df = test_df.drop(columns=[target_column_name, "Loan_ID"],axis=1)
            target_feature_test_df = test_df[target_column_name]
            target_feature_test_df = np.where(target_feature_test_df == 'Y', 1, 0)

            logging.info("Applying preprocessing object on training dataframe and testing dataframe.")

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.fit_transform(input_feature_test_df)
 
            train_arr = np.c_[input_feature_train_arr, target_feature_train_df]
            test_arr = np.c_[input_feature_test_arr, target_feature_test_df]

            logging.info("Saved preprocessing object.")

            save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path, obj=preprocessing_obj)
            return (train_arr, test_arr, self.data_transformation_config.preprocessor_obj_file_path)
        except Exception as e:
            raise CustomException(e,sys)
