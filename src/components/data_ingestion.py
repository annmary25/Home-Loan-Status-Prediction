import os
import sys
import pandas as pd
from src.logger import logging
from dataclasses import dataclass
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts', "train.csv")
    test_data_path:str = os.path.join('artifacts', "test.csv")
    raw_data_path:str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            df = pd.read_csv("/Users/admin/Loan-Status-Prediction/train.csv")
            logging.info("Read the dataset as dataframe")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=0)
            logging.info("Train test split initiated")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Completed data ingestion")
      
            return(self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)    
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()  

    data_tranformation = DataTransformation()
    train_array, test_array, _ = data_tranformation.initiate_data_transformation(train_data, test_data) 
    
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_array, test_array))
