import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_graphviz
import pydot

if __name__ == '__main__':
    incident_data = pd.read_csv("../resources/incident_data.csv")
    '''
    incident_data = incident_data[(incident_data['incidentType'] == 'A') |
          (incident_data['incidentType'] == 'B') |
          (incident_data['incidentType'] == 'C') | (incident_data['incidentType'] == 'HPI')]
          '''
    print(incident_data.groupby(['incidentType'])['incidentType'].count())
    print(incident_data.shape[0])
    X = incident_data.drop(columns=['incidentType', 'per_enable', 'per_name', 'emp_pos_cnt', 'emp_site_cnt'])
    y = incident_data['incidentType']

    rf = RandomForestClassifier(criterion='entropy', n_estimators=50,  max_depth=4, random_state=42)

    # perform 5-fold cross validation
    scores = cross_val_score(rf, X, y, cv=4)
    for score in scores:
        print(score)
    print(f'Average accuracy score: {scores.mean()}')