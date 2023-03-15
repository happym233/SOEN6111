from supervisor_cleaning import get_cleaned_supervisor_data
from incidents_cleaning import get_cleaned_incident_data, get_cleaned_incident_type_data

if __name__ == '__main__':
    cleaned_supervisor_data = get_cleaned_supervisor_data()
    cleaned_incident_data = get_cleaned_incident_data()
    cleaned_incident_type_data = get_cleaned_incident_type_data()
    cleaned_incident_data['incidentId'] = cleaned_incident_data['incidentId'].astype(int)
    cleaned_incident_type_data['incidentId'] = cleaned_incident_type_data['incidentId'].astype(int)
    print(cleaned_incident_type_data['incidentId'])
    cleaned_incident_data = cleaned_incident_data.join(cleaned_incident_type_data, on='incidentId', how="inner", lsuffix='_left', rsuffix='_right')
    cleaned_incident_data = cleaned_incident_data.join(cleaned_supervisor_data, on='per_id', how="inner")
    cleaned_incident_data.to_csv("cleaned_incident_data.csv")