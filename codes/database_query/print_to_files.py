from database_connection import DatabaseConnection
from table_sql_generator import TableNode


def generate_incident_sql():
    incident_table = TableNode({'ID': 'incidentId', 'IncidentNumber': None, 'CreationDate': 'IncidentCreationDate'},
                               'Incidents', 'incidents', {})
    incident_submission_table = TableNode({}, 'IncidentSubmissions', 'incidentSubmissions', {})
    submission_header_table = TableNode(
        {'Site': ('site',),
         'SubmittedBy_SupervisorID': 'per_id'}, 'SubmissionHeader', 'submissionHeaders', {})
    incident_table.children = [(("ID", "IncidentId"), incident_submission_table)]
    incident_submission_table.children = [(("SubmissionHeaderId", "ID"), submission_header_table)]
    return incident_table.to_sql()


def generate_incident_type_sql():
    incident_table = TableNode({'ID': 'incidentId'},
                               'Incidents', 'incidents', {})
    root_cause_analysis_table = TableNode({'PreliminaryTypeId': ('PreliminaryType',),
                                           'PotentialLossID': ('PotentialLoss',),
                                           'ActualTypeId': ('actualType',),
                                           'IncidentTypeId': ('incidentType',)},
                                          'RootCauseAnalysis', 'rca', {})
    incident_table.children = [(("ID", "IncidentId"), root_cause_analysis_table)]
    return incident_table.to_sql()


def generate_supervisor_sql():
    incident_table = TableNode({},
                               'Incidents', 'incidents', {})
    incident_submission_table = TableNode({}, 'IncidentSubmissions', 'incidentSubmissions', {})
    submission_header_table = TableNode({}, 'SubmissionHeader', 'submissionHeaders', {})
    person_table = TableNode(
        {'per_id': None, 'per_dob': None, 'per_first_name': None, 'per_middle_name': None, 'per_last_name': None,
         'per_sin': None,
         'per_gender': ('per_gender',), 'per_enable': None}, 'person', 'person', {})
    emp_table = TableNode({'emp_pos_id': ('emp_pos',), 'emp_start_date': None}, 'employee', 'emp', {})
    emp_job_table = TableNode({'ejo_job_id': ('emp_job',)}, 'employee_job', 'emp_job', {})
    emp_site_table = TableNode({'esi_sit_id': ('emp_site',)}, 'employee_site', 'emp_site', {})
    emp_training_table = TableNode({'etr_training_type_id': ('etr_training_type',),
                                    'etr_training_institution_id': ('etr_training_institution',),
                                    'etr_training_code_id': ('etr_training_code',), 'etr_completion_date': None,
                                    'etr_training_status_id': ('etr_training_status',)}, 'employee_training',
                                   'emp_train', {})
    incident_table.children = [(("ID", "IncidentId"), incident_submission_table)]
    incident_submission_table.children = [(("SubmissionHeaderId", "ID"), submission_header_table)]
    submission_header_table.children = [(("SubmittedBy_SupervisorID", "per_id"), person_table)]
    person_table.children = [(("per_id", "emp_per_id"), emp_table)]
    emp_table.children = [(("emp_id", "ejo_emp_id"), emp_job_table), (
        ("emp_id", "esi_emp_id"), emp_site_table)]  # , ("emp_id", "etr_emp_id"): emp_training_table}
    return incident_table.to_sql()


if __name__ == '__main__':
    incident_sql = generate_incident_sql()
    incident_type_sql = generate_incident_type_sql()
    supervisor_sql = generate_supervisor_sql()
    database = DatabaseConnection()
    print(incident_sql)
    print(incident_type_sql)
    print(supervisor_sql)
    data = database.run_sql(incident_sql)
    data.to_csv('../resources/incidents.csv', encoding='utf-8', index=False)
    data = database.run_sql(incident_type_sql)
    data.to_csv('../resources/incidents_type.csv', encoding='utf-8', index=False)
    data = database.run_sql(supervisor_sql)
    data.to_csv('../resources/supervisor.csv', encoding='utf-8', index=False)
