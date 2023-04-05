import pandas as pd


def aggregate_to_list(x, remove_words=[]):
    lst = []
    for i in x:
        removeI = False
        for r in remove_words:
            if r in i:
                removeI = True
                break
        if i not in lst and not removeI:
            lst.append(i)
    return ', '.join([str(i) for i in lst])


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
    supervisor_data["emp_pos"] = supervisor_data["emp_pos"].apply(
        lambda x: emp_pos_dict[x] if x in emp_pos_dict.keys() else x)
    supervisor_data = supervisor_data.groupby('per_id').agg({
        'per_dob': 'first',
        'per_first_name': 'first',
        'per_middle_name': 'first',
        'per_last_name': 'first',
        'emp_start_date': 'first',
        'per_enable': lambda x: aggregate_to_list(x),
        'emp_pos': lambda x: aggregate_to_list(x),
        'emp_site': lambda x: aggregate_to_list(x)
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
