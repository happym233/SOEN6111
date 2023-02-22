# Project Summary
## Introduction
The selected initiative involves collaborating with Sofvie Inc. on an industrial project that centers around the utilization of machine learning algorithms for analyzing incident data and enhancing the incident resolution process. The primary aim of this project is to employ machine learning algorithms to categorize incidents according to their respective supervisors, thereby facilitating the identification of patterns and trends.

The input of the project is the dataset which is provided by Sofvie Inc., in the form of a MySQL database, which comprises a wide range of information, not limited to the data required for the above-mentioned goal. The output of the algorithms and analysis will take the form of JSON data, as it is necessary to integrate this data into the current systems to facilitate further analysis and decision-making.

## Dataset Introduction
We need to obtain and extract the dataset from a MySQL database that comprises seven schemas and over 20 tables relevant to our task. To obtain the necessary data for our training task, we must query these tables, including essential ones like Incidents, RootCauseAnalysis, Person, Employee, and linking tables between them. For the classification task, the RootCauseAnalysis table provides the label.

The dataset contains diverse data formats, with most being discrete, such as site level, job site name, sign-off type, etc. The dataset also has continuous attributes, like incident duration, and includes time series, such as incident date and employee creation date. Additionally, the dataset has missing values and redundant attributes across tables.

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

## Feature Engineering
Feature engineering is a crucial step in machine learning aimed at simplifying and accelerating data transformations while also improving model accuracy. It involves a range of processes, including feature creation, transformations, feature extraction, exploratory data analysis, and benchmarking, among others.

In this study, we will mainly focus on two critical aspects of feature engineering: transformations and extraction. These processes involve three main tasks: data removal, filling missing values, and replacing values.

Data removal is an essential step to ensure that only relevant and useful information is included in our models. We need to carefully examine the data and remove any columns that are not related to or do not fit our model. By doing so, we can reduce the dimensionality of the dataset and improve the model's performance.

Filling missing values is another crucial task in feature engineering. Missing data can arise due to various reasons, such as measurement errors, data corruption, or incomplete data collection. We need to address missing values by filling them with an appropriate value manually in terms of the model we are using. For instance, we can use the mean or median of the available data points to fill in the missing values.

Replacing values is also an important part of feature engineering. In some cases, the values we receive from the database are in text or label format, which may not be directly usable in our models. In such cases, we need to convert them into a format that our model can understand. For instance, for label values, we can use the one-hot encoding approach, while for numerical values, we may need to normalize or standardize them to ensure that they have the same scale and distribution.

Overall, by performing these tasks effectively, we can enhance the accuracy of our models and obtain meaningful insights from our data.

## Model Description
We are using supervised machine learning models to classify incidents, utilizing the incident label (type) provided. The dataset mainly consists of discrete values, with some missing values and redundant attributes. Based on the dataset, we have selected Random Forest and SVM to perform the task.

Random Forest is well-suited for this task due to its ability to handle discrete and missing values. Our project will involve tuning hyperparameters, such as the number of trees in the forest, max depth, and min sample leaves, to optimize classification performance.

In addition to Random Forest, we will also test the performance of the SVM model on this dataset. We plan to experiment with different kernels, including linear, poly, and rbf, as well as define regularization and gamma parameters to evaluate the SVM's performance.

To assess the effectiveness of our models, we will utilize several metrics, including accuracy, precision, recall, f1-score, and confusion matrix. Additionally, we will explore the possibility of using ensemble methods to combine models in order to improve overall performance.
