from database_connection import DatabaseConnection

class TableNode:
    def __init__(self, selected_columns, table_name, table_as_name, children):
        self.selected_columns = selected_columns
        self.table_name = table_name
        self.table_as_name = table_as_name
        self.children = children

    def get_select_part(self):
        str = ""
        # (column_name, None)
        # (column_name, column_as_name)
        # require translation: (column_name, (column_as_name))
        for key in self.selected_columns:
            value = self.selected_columns[key]
            if isinstance(value, tuple):
                str += "lt_" + value[0] + ".ltr_text as " + value[0] + ",\n"
            else:
                if value is None:
                    str += self.table_as_name + "." + key + ",\n"
                else:
                    str += self.table_as_name + "." + key + " as " + value + ",\n"
        return str[:-2]

    def get_from_head(self):
        return self.table_name + " " + self.table_as_name + "\n"

    def get_from_following(self):
        str = ""
        for key in self.selected_columns:
            value = self.selected_columns[key]
            if isinstance(value, tuple):
                str += "JOIN ref_list_detail rld_" + value[0] + "\n"
                str += "ON " + self.table_as_name + "." + key + " = rld_" + value[0] + ".rld_id\n"
                str += "JOIN ref_list_header rlh_" + value[0] + "\n"
                str += "ON rld_" + value[0] + ".rld_rlh_id = rlh_" + value[0] + ".rlh_id\n"
                str += "JOIN language_translation lt_" + value[0] + "\n"
                str += "ON rld_" + value[0] + ".rld_name = lt_" + value[0] + ".ltr_tag\n"
        return str

    def get_from_part(self):
        return self.get_from_head() + self.get_from_following()

    def get_where_part(self, add_and=False):
        i = 0
        str = ""
        for key in self.selected_columns:
            value = self.selected_columns[key]
            if isinstance(value, tuple):
                if i != 0 or add_and:
                    str += "and "
                i = i + 1
                str += "lt_" + value[0] + ".ltr_lng_id = 1\n"
        return str

    def to_sql(self):
        queue = [self]
        select_str = ""
        from_str = self.get_from_part()
        where_str = ""
        i = 0
        while len(queue) != 0:
            node = queue.pop(0)
            # print(node.table_name)
            if i != 0 and len(node.selected_columns) != 0:
                select_str += ',\n'
            add_and = False
            if len(where_str) != 0:
                add_and = True
            select_str += node.get_select_part()
            where_str += node.get_where_part(add_and)
            for child in node.children:
                child_node = child[1]
                queue.append(child_node)
                from_str += "JOIN " + child_node.get_from_head()
                from_str += "on " + node.table_as_name + "." + child[0][0] + "=" \
                            + child_node.table_as_name + "." + child[0][1] + "\n"
                from_str += child_node.get_from_following()
            i += 1
        return "select " + select_str + "\nfrom " + from_str + "where " + where_str

def generate_sql():
    incident_table = TableNode({'ID': 'IncidentId', 'IncidentNumber': None, 'CreationDate': 'IncidentCreationDate'}, 'Incidents', 'incidents', {})
    root_cause_analysis_table = TableNode({'PreliminaryTypeId': ('PreliminaryType',),
                                           'PotentialLossID': ('PotentialLoss', ),
                                           'ActualTypeId': ('actualType', ),
                                           'IncidentTypeId': ('incidentType', )},
                                          'RootCauseAnalysis', 'rca', {})
    incident_submission_table = TableNode({}, 'IncidentSubmissions', 'incidentSubmissions', {})
    submission_header_table = TableNode({'Site': ('site',), 'SiteLevel': ('SiteLevel', ), 'JobNumber': ('jobNumber',), 'Workplace': None}, 'SubmissionHeader', 'submissionHeaders', {})
    person_table = TableNode({'per_dob': None, 'per_first_name':None, 'per_middle_name': None, 'per_last_name': None, 'per_sin': None, 'per_gender': ('per_gender',), 'per_enable': None}, 'person', 'person', {})
    emp_table = TableNode({'emp_pos_id': ('emp_pos', ), 'emp_start_date': None}, 'employee', 'emp', {})
    emp_job_table = TableNode({'ejo_job_id': ('emp_job',)}, 'employee_job', 'emp_job', {})
    emp_site_table = TableNode({'esi_sit_id': ('emp_site',)}, 'employee_site', 'emp_site', {})
    emp_training_table = TableNode({'etr_training_type_id': ('etr_training_type',), 'etr_training_institution_id': ('etr_training_institution', ),
                                    'etr_training_code_id': ('etr_training_code',), 'etr_completion_date': None, 'etr_training_status_id': ('etr_training_status',)}, 'employee_training', 'emp_train', {})
    incident_table.children = [(("ID", "IncidentId"), root_cause_analysis_table)]
    # incident_table.children = [(("ID", "IncidentId"), incident_submission_table)]
    incident_submission_table.children = [(("SubmissionHeaderId", "ID"), submission_header_table)]
    submission_header_table.children = [(("SubmittedBy_SupervisorID", "per_id"), person_table)]
    person_table.children = [(("per_id", "emp_per_id"), emp_table)]
    emp_table.children = [(("emp_id", "ejo_emp_id"), emp_job_table), (("emp_id", "esi_emp_id"), emp_site_table)]#, ("emp_id", "etr_emp_id"): emp_training_table}
    return incident_table.to_sql()


if __name__ == '__main__':
    sql = generate_sql()
    print(sql)
    emp_training_table = TableNode({'etr_training_type_id': ('etr_training_type',), 'etr_training_institution_id': ('etr_training_institution', ),
                                    'etr_training_code_id': ('etr_training_code',), 'etr_completion_date': None, 'etr_training_status_id': ('etr_training_status',)}, 'employee_training', 'emp_train', {})
    #print(emp_training_table.to_sql())
    emp_site_table = TableNode({'esi_sit_id': ('emp_site',)}, 'employee_site', 'emp_site', {})
    # print(emp_site_table.to_sql())
    emp_job_table = TableNode({'ejo_job_id': ('emp_job',)}, 'employee_job', 'emp_job', {})
    # print(emp_job_table.to_sql())
    database = DatabaseConnection()
    data = database.run_sql(sql)
    data.to_csv('incidents_type.csv', encoding='utf-8', index=False)
