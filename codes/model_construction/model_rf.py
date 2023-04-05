import os.path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from KFoldTraining import k_fold_train
from sklearn.model_selection import cross_validate, KFold
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score, confusion_matrix

class RandomForest:

    def __init__(self, hyperparam_dicts, model_output_path='../resources',
                 performance_lst=pd.DataFrame(columns=['model', 'hyperparam', 'acc', 'precision', 'recall', 'f1-score'])):
        self.best_acc = 0
        self.hyperparam_dicts = hyperparam_dicts
        self.model = None
        self.hyperparam_dict = None
        self.model_output_path = model_output_path
        self.performance_lst = performance_lst

    def select_columns(self, incident_data):
        X = incident_data.drop(columns=['incidentType', 'per_enable', 'per_name', 'emp_pos_cnt', 'emp_site_cnt'])
        y = incident_data['incidentType']
        return X.to_numpy(), y.to_numpy()

    def create_instance(self, hyperparam_dict):
        criterion = 'entropy'
        n_estimators = 20
        max_depth = 4
        min_samples_leaf = 1
        if 'critertion' in hyperparam_dict:
            criterion = hyperparam_dict['critertion']
        else:
            hyperparam_dict['critertion'] = criterion
        if 'n_estimators' in hyperparam_dict:
            n_estimators = hyperparam_dict['n_estimators']
        else:
            hyperparam_dict['n_estimators'] = n_estimators
        if 'max_depth' in hyperparam_dict:
            max_depth = hyperparam_dict['max_depth']
        else:
            hyperparam_dict['max_depth'] = max_depth
        if 'min_sample_leaf' in hyperparam_dict:
            min_samples_leaf = hyperparam_dict['min_samples_leaf']
        else:
            hyperparam_dict['min_samples_leaf'] = min_samples_leaf
        self.hyperparam_dict = hyperparam_dict
        self.model = RandomForestClassifier(criterion=criterion, n_estimators=n_estimators,
                                            max_depth=max_depth, min_samples_leaf=min_samples_leaf)
        return self.model

    def normalize(self, X_train, X_test):
        return X_train, X_test

    def get_model(self):
        return self.model

    def train(self, data):
        X, y = self.select_columns(data)
        for hyperparam_dict in self.hyperparam_dicts:
            self.model = self.create_instance(hyperparam_dict)
            print("training for hyperparameter: " + str(self.hyperparam_dict) + "\n")
            k_fold_train(self, X, y)

    def add_result(self, res):
        print(res['acc'])
        self.performance_lst = pd.concat([self.performance_lst, pd.DataFrame([{
            'model': 'random forest',
            'hyperparam': str(self.hyperparam_dict),
            'accuracy': res['acc'],
            'precision': res['pre'],
            'recall': res['rec'],
            'f1-score': res['f1']
        }])], ignore_index=True)

    def save(self, acc):
        if (acc > self.best_acc):
            self.best_acc = acc
            joblib.dump(self.model, os.path.join(self.model_output_path, 'model_rf.joblib'))


if __name__ == '__main__':
    incident_data = pd.read_csv("../resources/incident_data.csv")
    incident_data = incident_data[(incident_data['incidentType'] == 'A') |
          (incident_data['incidentType'] == 'B') |
          (incident_data['incidentType'] == 'C') | (incident_data['incidentType'] == 'HPI')]

    randomForest = RandomForest([{}])
    randomForest.train(incident_data)
    '''
    print(incident_data.groupby(['incidentType'])['incidentType'].count())
    print(incident_data.shape[0])
    X = incident_data.drop(columns=['incidentType', 'per_enable', 'per_name', 'emp_pos_cnt', 'emp_site_cnt'])
    y = incident_data['incidentType']

    rf = RandomForestClassifier(criterion='entropy', n_estimators=20,  max_depth=4, random_state=42)
    '''
    # perform 4-fold cross validation
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(y)
    '''

    '''
    rf = RandomForestClassifier(n_estimators=100, random_state=42)

    # define 5-fold cross-validation
    cv = KFold(n_splits=5, shuffle=True, random_state=42)

    # define metrics to evaluate model performance
    scoring = {'precision': 'precision',
               'recall': 'recall',
               'accuracy': 'accuracy',
               'f1_score': 'f1'}

    # train model and evaluate performance using 5-fold cross-validation
    results = cross_validate(rf, X, y, cv=cv, scoring=scoring)

    # print results for each fold
    for i in range(5):
        print(f'Fold {i + 1} results:')
        print(f'Precision: {results["test_precision"][i]}')
        print(f'Recall: {results["test_recall"][i]}')
        print(f'Accuracy: {results["test_accuracy"][i]}')
        print(f'F1-score: {results["test_f1_score"][i]}')
        print(f'Confusion matrix:\n{confusion_matrix(y[cv.split(X)[i][1]], rf.predict(X[cv.split(X)[i][1]]))}\n')
'''
