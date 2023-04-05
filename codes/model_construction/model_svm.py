import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import cross_validate, KFold
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from KFoldTraining import k_fold_train
import os
import joblib

class ModelSVM:
    def __init__(self, hyperparam_dicts, model_output_path='../resources',
                 performance_lst=pd.DataFrame(columns=['model', 'hyperparam', 'accuracy', 'precision', 'recall', 'f1-score'])):
        self.best_acc = 0
        self.hyperparam_dicts = hyperparam_dicts
        self.model = None
        self.scaler = None
        self.hyperparam_dict = None
        self.model_output_path = model_output_path
        self.performance_lst = performance_lst

    def select_columns(self, incident_data):
        X = incident_data.drop(columns=['incidentType', 'IncidentCreationYear', 'per_enable', 'per_name', 'emp_pos_cnt', 'emp_site_cnt'])
        y = incident_data['incidentType']
        self.labels = y.unique()
        return X.to_numpy(), y.to_numpy()

    def create_instance(self, hyperparam_dict):
        kernel = 'rbf'
        C = 1.0
        gamma = 'scale'
        if 'kernel' in hyperparam_dict:
            kernel = hyperparam_dict['kernel']
        else:
            hyperparam_dict['kernel'] = kernel
        if 'C' in hyperparam_dict:
            C = hyperparam_dict['C']
        else:
            hyperparam_dict['C'] = C
        if 'gamma' in hyperparam_dict:
            gamma = hyperparam_dict['gamma']
        else:
            hyperparam_dict['gamma'] = gamma
        self.hyperparam_dict = hyperparam_dict
        self.model = SVC(kernel=kernel, C=C, gamma=gamma)
        return self.model

    def normalize(self, X_train, X_test):
        self.scaler = StandardScaler()
        X_train = self.scaler.fit_transform(X_train)
        X_test = self.scaler.transform(X_test)
        return X_train, X_test

    def get_model(self):
        return self.model

    def train(self, data):
        X, y = self.select_columns(data)
        for hyperparam_dict in self.hyperparam_dicts:
            print("===========================================================================")
            print("training for hyperparameter: " + str(self.hyperparam_dict) + "\n")
            self.model = self.create_instance(hyperparam_dict)
            k_fold_train(self, X, y)

    def add_result(self, res):
        self.performance_lst = pd.concat([self.performance_lst, pd.DataFrame([{
            'model': 'SVM',
            'hyperparam': str(self.hyperparam_dict),
            'accuracy': res['acc'],
            'precision': res['pre'],
            'recall': res['rec'],
            'f1-score': res['f1']
        }])], ignore_index=True)

    def get_performance_lst(self):
      return self.performance_lst

    def save(self, acc):
        if (acc > self.best_acc):
            self.best_acc = acc
            joblib.dump(self.scaler, os.path.join(self.model_output_path, 'scaler_svm.pkl'))
            joblib.dump(self.model, os.path.join(self.model_output_path, 'model_svm.pkl'))


if __name__ == '__main__':
    incident_data = pd.read_csv("../resources/incident_data.csv")
    incident_data = incident_data[(incident_data['incidentType'] == 'A') |
                                  (incident_data['incidentType'] == 'B') |
                                  (incident_data['incidentType'] == 'C') | (incident_data['incidentType'] == 'HPI')]

    randomForest = ModelSVM([{}])
    randomForest.train(incident_data)
