import os
import sys
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object,evaluate_models

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, BaggingClassifier

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            x_train, y_train, x_test, y_test = (train_array[:,:-1], train_array[:,-1], test_array[:,:-1], test_array[:,-1])
            logging.info("Splitting train and test data")
            models = {
                "Logistic Regression": LogisticRegression(),
                "K Nearest Neighbors": KNeighborsClassifier(),
                "Decision Tree": DecisionTreeClassifier(),
                "Gaussian Naive Bayes": GaussianNB(),
                "Random Forest": RandomForestClassifier(),
                "Support Vector": SVC(),
                "Gradient Boost": GradientBoostingClassifier(),
                "BaggingClassifier": BaggingClassifier(),
                "BernoulliNB": BernoulliNB() 
            }
            params = {
                "Logistic Regression": {
                    "solver": ['lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'],
                },
                "K Nearest Neighbors": {
                    "algorithm": ['auto', 'ball_tree', 'kd_tree', 'brute']
                },
                "Decision Tree": {
                    "splitter": ["best", "random"],
                    "criterion": ["gini", "entropy", "log_loss"]
                },
                "Gaussian Naive Bayes": {},
                "Random Forest": {
                    "criterion": ["gini", "entropy", "log_loss"],
                    "min_samples_split": [2,3,4, 10, 20, 30, 100, 200, 300],
                    "max_features":["sqrt", "log2", None]
                },
                "Support Vector": {
                    "gamma": ['scale', 'auto'],
                    "decision_function_shape": ['ovo', 'ovr'],
                    "break_ties": [False]
                },
                "Gradient Boost": {
                    "loss": ["log_loss", "deviance", "exponential"]
                },
                "BaggingClassifier": {
                    "n_estimators": [1,10,100,500,1000]
                },
                "BernoulliNB": {
                    "force_alpha": [True, False],
                    "fit_prior": [True, False]
                }
            }
            model_report:dict=evaluate_models(x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test, models=models, params=params)
            logging.info("Generated model report")
            print(model_report)

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]
            logging.info("Identified best model & score")
            if best_model_score < 0.6:
                raise CustomException("No best model found", sys)

            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )
            
            predicted = best_model.predict(x_test)
            AccuracyScore = accuracy_score(y_test, predicted)
            return AccuracyScore
        except Exception as e:
            raise CustomException(e,sys)
