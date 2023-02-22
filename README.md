# Project Summary
## Introduction
The selected topic involves collaborating with Sofvie Inc. on an industrial project that utilizing machine learning algorithms to classify the types of incidents based on the provided data. 
 Our approach to this project will involve key steps, including data querying, feature engineering, and constructing machine learning models including Support Vector Machine (SVM) and Random Forest. We will also perform a comparison of the performance of these two models to identify differences. Additionally, we will investigate the impact of fine-tuning on the performance of the machine learning models.
## Dataset Introduction
We need to obtain and extract the dataset from a MySQL database that comprises seven schemas and over 20 tables relevant to our task with SQL query. For the classification task, the RootCauseAnalysis table provides the label.
The dataset contains diverse data formats, with most being discrete, such as site level, job site name, sign-off type, etc. The dataset also has continuous attributes, like incident duration, and includes time series, such as incident date and employee creation date. Additionally, the dataset has missing values and redundant attributes across tables.

- [introduction of database schema](documents/database_schema.md)
## Feature Engineering
In order to enhance the performance of our model, we will carry out several operations on the provided data. Firstly, we will remove irrelevant data from the given schema that is either unrelated or does not align with our model. This will help to reduce the dimensionality of the dataset. Additionally, we will address missing values by filling them with appropriate values that are suitable for our model.

Furthermore, we will replace certain values in the given data, such as labels, text, or time series, by converting them to a format that our model can comprehend. For numerical values, we may need to normalize or standardize the data to ensure that they have the same scale and distribution.
## Model Description
We are using supervised machine learning models to classify incidents, utilizing the incident label (type) provided. Based on the dataset, we have selected Random Forest and SVM to perform the task.

- Random Forest is well-suited for this task due to its ability to handle discrete and missing values. Our project will involve tuning hyperparameters, such as the number of trees in the forest, max depth, and min sample leaves, to optimize classification performance.

- SVM would also be applied to this task. We plan to experiment with different kernels, as well as define regularization and gamma parameters to evaluate the SVM's performance.

To assess the effectiveness of our models, we will utilize several metrics, including accuracy, precision, recall, f1-score, and confusion matrix. Additionally, we will explore the possibility of using ensemble methods to combine models in order to improve overall performance.
