import pandas as pd
import os
from sklearn.model_selection import train_test_split
from rampwf.workflows import Classifier
import rampwf as rw
import numpy as np
from sklearn.model_selection import StratifiedKFold

def get_cv(X, y):
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    return cv.split(X, y)

problem_title = "Prédiction de la gravité des accidents de la route"
_target_column_name = "y"
_prediction_label_names = [0, 1, 2]

workflow = rw.workflows.Classifier()
Predictions = rw.prediction_types.make_multiclass(label_names=_prediction_label_names)
score_types = [rw.score_types.Accuracy(name="accuracy", precision=4),]

def get_train_data(path="./"):
    """ Charge X_train et y_train pour l'entraînement """
    train_data = pd.read_csv(os.path.join(path, "X_train.csv"))
    y_train = train_data[_target_column_name].values
    X_train = train_data.drop(columns=[_target_column_name]).values
    return X_train, y_train

def get_test_data(path="./"):
    """ Charge X_test et y_test pour l'évaluation """
    X_test = pd.read_csv(os.path.join(path, "X_test.csv")).values
    y_test = pd.read_csv(os.path.join(path, "y_test.csv"))[_target_column_name].values
    return X_test, y_test