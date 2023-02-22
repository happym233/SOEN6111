### Relevant Database Schema and Explanation For Analysis
1. **Incidents(size: 1259):**  
   ID: the id for each incident  
   IncidentNumber: incident number  
   inc_is_quick_signoff: identify if the incident is signed off  
   CreationDate: incident record creation date  
   CreatedBy: the name of person who creates the incident

2. **incident_signoffs(size: 3799):**  
   iso_id: record id  
   iso_incident_id: the corresponding incident id  
   iso_role_id: the role id of the person who signs off the incident  
   iso_per_id: the person id for the one who signs off the incident  
   iso_signoff_datetime: the date and time when the incident is signed off  
   iso_created_date: the creation date when the record is created  
   iso_created_by_per_id: the person id for the one who created the record

3. **incident_quick_signoff_note(size: 30):**   
   iqn_id: record id  
   iqn_incident_id: the corresponding incident id  
   iqn_note: the note content for each incident  
   iqn_created_date: creation date for the quick note  
   iqn_created_by_per_id: the person id who creates the note  
   Note: for each incident there may be non or multiple notes

4. **IncidentAttachments(size: 10865):**  
   ID: record id  
   IncidentID: the corresponding incident id  
   FileName: attachment file name  
   FileType: attachment file type  
   LastModifiedBy: the person who last modifies the record

5. **IncidentSubmissions(size: 5414):**
   id: record id  
   IncidentID: the corresponding incident id  
   SubmissionHeaderID: submission header id

6. **SubmissionHeader(size: 144741):**  
   ID: record id  
   FormDescriptionID: form description id  
   SubmissionID: the submission id  
   Workplace: ?  
   Supervisor: the supervisor id  
   SubmittedBy_SupervisorID: the supervisor id who submitted the header

7. **IncidentSignoffs(size: 3402):**  
   IncidentID: the corresponding incident id  
   EmployeeID: the employee id  
   Type: employee type  
   Timestamp: timestamp for recording the signoff

8. **RootCauseAnalysis: the analysis for each incident**  
   ID: record id  
   IncidentID: the id for each incident  
   PotentialLossID: potential loss record id  
   ActualTypeID: actual type record id  
   EventDetails: the detailed description for the incident  
