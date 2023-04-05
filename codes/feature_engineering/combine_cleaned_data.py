from supervisor_cleaning import get_cleaned_supervisor_data
from incidents_cleaning import get_cleaned_incident_data, get_cleaned_incident_type_data
import pandas as pd
import random

def list_contains(item, lis):
    for i in lis:
        if item == i:
            return True
    return False

def select_type(incidents, type_list=[]):
    return incidents[incidents['incidentType'].isin(type_list)]

def data_augmentaion(incidents_data):
    counts = incidents_data['incidentType'].value_counts()
    duplicated_data = []
    for label in counts.index:
        label_data = incidents_data[incidents_data['incidentType'] == label]
        n_samples = int(0.9 * (max(counts) - len(label_data)))
        if n_samples > 0:
            for i in range(n_samples):
                duplicated_data.append(label_data.iloc[random.randint(0, len(label_data)) % len(label_data)])
    augmented_df = pd.concat([incidents_data, pd.DataFrame(duplicated_data)], ignore_index=True)
    augmented_df = augmented_df.sample(frac=1)
    return augmented_df

if __name__ == '__main__':
    cleaned_supervisor_data = get_cleaned_supervisor_data()
    cleaned_incident_data = get_cleaned_incident_data()
    cleaned_incident_type_data = get_cleaned_incident_type_data()
    cleaned_incident_data['incidentId'] = cleaned_incident_data['incidentId'].astype(int)
    cleaned_incident_type_data['incidentId'] = cleaned_incident_type_data['incidentId'].astype(int)
    cleaned_incident_data = cleaned_incident_data.set_index('incidentId').join(
        cleaned_incident_type_data.set_index('incidentId'), on='incidentId', how="inner")
    cleaned_incident_data = cleaned_incident_data.join(cleaned_supervisor_data, on='per_id', how="inner")
    cleaned_incident_data = select_type(cleaned_incident_data, ['A', 'B', 'C', 'HPI'])
    print(cleaned_incident_data.shape)
    cleaned_incident_data = select_type(cleaned_incident_data, ['A', 'B', 'C', 'HPI'])
    cleaned_incident_data = data_augmentaion(cleaned_incident_data)
    cleaned_incident_data.to_csv("cleaned_incident_data.csv", encoding='utf-8', index=False)
