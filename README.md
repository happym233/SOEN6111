# Project Summary
## Introduction
The selected topic involves collaborating with Sofvie Inc. on an industrial project that utilizing machine learning algorithms to classify the types of incidents based on the provided data. The primary aim of this project is to employ machine learning algorithms to categorize incidents according to data in given 
MySQL database. The input of the project comprises a wide range of information, not limited to the data required for the above-mentioned goal and the output of the algorithms and analysis will take the form of JSON data to facilitate further analysis.

The initial challenge we will tackle in this project is addressing the issue of dealing with a dataset that has a vast number of columns. In order to enhance the effectiveness of our model, we will need to implement methods that help to reduce the dimensions of the dataset.

The second challenge we will address is the comparison of the performance of Random Forest and SVM, specifically when most of the data in the dataset is discrete. We will investigate the possibility of utilizing ensemble methods to boost the accuracy of our models.

## Dataset
The given MySQL database include 7 schemas and 30 tables relevant to our task. Incidents are classified into 11 types, with their supervisor, potential cause, sign-off information are provided.
The dataset contains diverse data formats, with most being text. The dataset also has discrete values and includes time series. Additionally, the dataset has missing values and redundant attributes across tables.

- [introduction of database schema](documents/database_schema.md)
## Feature Engineering
Firstly, we will remove irrelevant data from the given schema that is either unrelated or does not align with our model. Additionally, we will address missing values by filling them with appropriate values.

Furthermore, we will replace certain values in the given data, such as labels, text, or time series, by converting them to a format that our model can comprehend. For numerical values, we may need to normalize or standardize the data to ensure that they have the same scale and distribution.
## Model Description
We are using supervised machine learning models to classify incidents, utilizing the incident label (type) provided. Based on the dataset, we have selected Random Forest and SVM to perform the task.

- Random Forest is well-suited for this task due to its ability to handle discrete and missing values. Our project will involve tuning hyperparameters, such as the number of trees in the forest, max depth, and min sample leaves, to optimize classification performance.

- SVM would also be applied to this task. We plan to experiment with different kernels, as well as define regularization and gamma parameters to evaluate the SVM's performance.

To assess the effectiveness of our models, we will utilize several metrics, including accuracy, precision, recall, f1-score, and confusion matrix. Additionally, we will explore the possibility of using ensemble methods to combine models in order to improve overall performance.
