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
    return ', '.join([str(i) for i in list])

def clean_supervisor_data(supervisor_data):
    supervisor_data.drop(['per_sin', 'per_gender'], axis=1)
    emp_pos_dict = {
        'Safety and Training Supervisor': 'Safety Supervisor, Training Supervisor',
        'Safety Supervisor 01': 'Safety Supervisor',
        'Safety Supervisor 02': 'Safety Supervisor',
        'Junior Miner B': 'Miner',
        'Mid Miner B': 'Miner',
        'Mid Miner C': 'Miner',
        'Construction Miner C': 'Miner'
    }
    supervisor_data["emp_pos"] = supervisor_data["emp_pos"].apply(lambda x: emp_pos_dict[x] if x in emp_pos_dict.keys() else x)
    supervisor_data = supervisor_data.groupby('per_id').agg({
        'per_dob': 'first',
        'per_first_name': 'first',
        'per_middle_name': 'first',
        'per_last_name': 'first',
        'emp_start_date': 'first',
        'per_enable': lambda x: aggregate_to_list(x),
        'emp_pos': lambda x: aggregate_to_list(x, remove_words=['Severity of Loss',
            'You have <b>1 Open Action</b> that requires your attention and it is <b class="text-danger">overdue</b>.',
            'Recent Positive Recognitions',
            'New Employee Departure',
            'Actions by Role',
            'Special Projects',
            'Loading general actions page. Please wait.',
            'Safety Supervisor 03',
            'A&M Shift\xa0Report',
            'Archive ORA?',
            'You do not have permission to manage Incidents',
            'At My Site',
            'Positive Recognition Count by Month and Year',
            'Do not write down your password and do not share it with anybody else.',
            'Other 3 (not included in list)',
            'Archive JRA?',
            'Files from computer',
            'Loading hazard action grid. Please wait.',
            'Password Reset Success',
            'You are about to archive this job risk assessment. Undoing this will require IT support. Are you sure?',
            'Photos Available',
            'for current month',
            'Mobile Supervisor Surface',
            'Craven Arms',
            'Licensed HDET',
            'Sign off',
            'TOP 10',
            'No Comment',
            'Dayr-al-Balah',
            'Debub',
            'Positive Recognitions vs. Hazards',
            'Archive PRA?',
            'If you think you might forget your password, consider using a password manager application.',
            'Follow Up Attachments Count',
            'ORA Controls',
            'Special Projects #8',
            'Positive Recognition vs. Incident Counts',
            '<b>Exceeds Expectations:</b> Easily adjusts priorities, activities, and attitude to meet new deadlines; anticipates and responds with enthusiasm to new challenges; keeps an open mind and shows willingness to learn new methods, procedures, and techniques; encourages others to keep calm during stressful times.',
            'New Employee Performance Evaluation',
            'You are confirming that you have reviewed this assessment. This cannot be undone. Continue?',
            'Well done!',
            'Other Info',
            'You have successfully reset your password.']),
        'emp_site': lambda x: aggregate_to_list(x, remove_words=[
            'submissions. Undoing this will require IT support. Are you sure?',
            'Lockout / Tagout Procedure',
            'You have already acknowledged this Lesson',
            'Technica Training',
            'You are about to delete',
            'Onaping Depth Project',
            'Loading lessons learned. Please wait.',
            'Only Pictures can be attached',
            'lessons. Undoing this will require IT support. Are you sure?',
            'Field Service and Rental',
            'Person reporting incident',
            'You are about to archive',
            'Click the button below to set up a new password.',
            'New Preliminary Incident',
            'Safety & Training Supervisor Sign Off',
            'decisions. Undoing this will require IT support. Are you sure?',
            'Other 1 (not included in list)',
            'Reporting Period',
            'Loading data...',
            'We have received a request to reset your Sofvie account password.',
            'Electrical Projects',
            'Website',
            'Surface Division 2023',
            'Surface Drill and Blast'
        ])
    })
    return supervisor_data

def get_cleaned_supervisor_data():
    supervisor_data = pd.read_csv("../resources/supervisor.csv")
    supervisor_data = clean_supervisor_data(supervisor_data)
    return supervisor_data

if __name__ == '__main__':
    supervisor_data = pd.read_csv("../resources/supervisor.csv")
    print(supervisor_data.head())
    print(supervisor_data['emp_start_date'])
    supervisor_data = clean_supervisor_data(supervisor_data)
    print(supervisor_data['emp_start_date'])
    # print(supervisor_data['per_enable'])