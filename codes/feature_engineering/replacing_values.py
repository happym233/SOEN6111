import pandas as pd


if __name__ == '__main__':
    incident_data = pd.read_csv("cleaned_incident_data.csv")
    # print(incident_data)
    incident_data['IncidentCreationDateTimestamp'] = pd.to_datetime(incident_data['IncidentCreationDate'], format="%Y-%m-%d %H:%M:%S")
    incident_data['per_dob_timestamp'] = pd.to_datetime(incident_data['per_dob'], format="%Y-%m-%d %H:%M:%S")
    incident_data['emp_start_date_timestamp'] = pd.to_datetime(incident_data['emp_start_date'], format="%Y-%m-%d %H:%M:%S")
    incident_data['per_middle_name'] = incident_data['per_middle_name'].fillna("")
    incident_data['per_name'] = incident_data['per_first_name'] + " " + incident_data['per_middle_name'] + " " + incident_data['per_last_name']
    site_dict = {
        'CCM South - Development': 'CCM South',
        'CCM South - Shaft': 'CCM South'
    }
    incident_data["site"] = incident_data["site"].apply(lambda x: site_dict[x] if x in site_dict.keys() else x)
    print(incident_data['IncidentCreationDateTimestamp'])
    incident_data['IncidentCreationYear'] = incident_data['IncidentCreationDateTimestamp'].dt.year
    incident_data['IncidentCreationMonth'] = incident_data['IncidentCreationDateTimestamp'].dt.month
    incident_data['IncidentCreationWeekday'] = incident_data['IncidentCreationDateTimestamp'].dt.weekday
    print(incident_data['IncidentCreationMonth'])
    print(incident_data['IncidentCreationDateTimestamp'].dt.weekday)
    incident_data['incidentDobDayBetween'] = (incident_data["IncidentCreationDateTimestamp"] - incident_data['per_dob_timestamp']).dt.days
    incident_data['incidentEmpStartDayBetween'] = (incident_data["IncidentCreationDateTimestamp"] - incident_data['emp_start_date_timestamp']).dt.days
    incident_data['DobEmpStartDayBetween'] = (incident_data["emp_start_date_timestamp"] - incident_data['per_dob_timestamp']).dt.days
    incident_data['emp_pos_cnt'] = incident_data['emp_pos'].apply(lambda x: len(str(x).split(',')) if x is not None else 1)
    incident_data['emp_site_cnt'] = incident_data['emp_site'].apply(lambda x: len(str(x).split(',')) if x is not None else 1)
    print(incident_data["site"].unique())
    #site_one_hot = pd.get_dummies(incident_data["site"])
    #incident_data = pd.concat([incident_data, site_one_hot], axis=1)
    print(incident_data["emp_pos"].unique())
    incident_data = incident_data.drop(['IncidentNumber', 'IncidentCreationDate', 'site', 'per_id', 'PotentialLoss', 'PreliminaryType', 'actualType', 'per_dob',
                        'per_dob', 'per_first_name', 'per_middle_name', 'per_last_name', 'emp_start_date', 'emp_pos', 'emp_site',
                        'IncidentCreationDateTimestamp', 'per_dob_timestamp', 'emp_start_date_timestamp'], axis=1)
    incident_data = incident_data.drop_duplicates()
    incident_data.to_csv("../resources/incident_data.csv", encoding='utf-8', index=False)

