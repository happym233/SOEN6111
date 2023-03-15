import pandas as pd

def aggregate_to_list(x, remove_words=[]):
    list = []
    for i in x:
        removeI = False
        for r in remove_words:
            if r in i:
                removeI = True
                break
        if i not in list and not removeI:
            list.append(i)
    return ','.join([str(i) for i in list])


def clear_wordList_from_column(data, column_name, word_list):
    return data[data[column_name].map(lambda x: x not in word_list)]

def clean_incident_data(incident_data):
    incident_data = clear_wordList_from_column(incident_data, "site", [
        'Safety & Training Supervisor Sign Off',
        'Mechanisms, Accessories and PPE required',
        'decisions. Undoing this will require IT support. Are you sure?',
        'lessons. Undoing this will require IT support. Are you sure?',
        'Person reporting incident',
        'You are about to delete',
        'Other 1 (not included in list)',
        'You are about to archive',
        'Onaping Depth Project',
        'Loading lessons learned. Please wait.',
        'Other 2 (not included in list)',
        'New Preliminary Incident',
        'You have already acknowledged this Lesson',
        'New Employee Discipline',
        'Loading data...',
        'Business Development',
        'CSV',
        'Anmar Mechanical',
        'If you did not request a password reset, please ignore this email.',
        'New Positive Recognition',
        'submissions. Undoing this will require IT support. Are you sure?',
        'Only Pictures can be attached',
        'Support',
        'We have received a request to reset your Sofvie account password.',
        'Reporting Period',
        'Lockout / Tagout Procedure']
    )
    return incident_data

def get_cleaned_incident_data():
    incidents_data = pd.read_csv("../resources/incidents.csv")
    # print(incidents_data["site"].unique())
    # print(incidents_data["jobNumber"].unique())
    # incidents_data["Workplace"].unique())
    incidents_data = clean_incident_data(incidents_data)
    return incidents_data

def get_cleaned_incident_type_data():
    incidents_type_data = pd.read_csv("../resources/incidents_type.csv")
    return incidents_type_data

if __name__ == '__main__':
    incidents_data = pd.read_csv("../resources/incidents.csv")
    # print(incidents_data["site"].unique())
    # print(incidents_data["jobNumber"].unique())
    # incidents_data["Workplace"].unique())
    incidents_data = clean_incident_data(incidents_data)
    incidents_data.to_csv("incidents.csv")