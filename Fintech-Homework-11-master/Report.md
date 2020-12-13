# Risk Business Report

![ML](Images/ml_bg.jpeg)

## Report Overview

This report summarizes the experiments performed in both resampling and ensemble learning sections. In addition, questions for each section will be answered in the report.

### Resampling </br>

#### Breakdown

This section covered the data encoding, different types of data sampling techniques as well as performance evaluation in multiple fields.

* Data encoding using LabelEncoder:

    In the original dataframe, both `homeowner` and `loan_status` fields were categorical data, which could not be evaulated with numeric data directly. Therefore, LabelEncoder was applied to convert them to numeric values. Particularly, `loan_status` was encoded in the sense that low risk was marrked as `0`, and  high risk was marked as `1`.

* Data Oversampling Techniques applied:

    1. Naive Random Oversampling
    2. SMOTE Oversampling

* Data Undersampling Techniques applied: Cluster Centroids algorithm
    
* Data Combination Sampling: SMOTEENN algorithm

#### Q&A

__Q1__: Which model had the best balanced accuracy score ? </br>
__A__:  Naive Random Oversampling,  SMOTE Oversampling and Cluster Centroids algorithm produced the same balanced accuracy score: 0.9936781215845847.

__Q2__: Which model had the best recall score? </br>
__A__: SMOTEENN algorithm, Naive Random Oversampling,  SMOTE Oversampling and Cluster Centroids algorithm all had the same average recall score: 0.99.

__Q3__: Which model had the best geometric mean score? </br>
__A__:  SMOTEENN algorithm, Naive Random Oversampling,  SMOTE Oversampling and Cluster Centroids algorithm all had the same geometric mean score: 0.99.


### Ensemble Learning </br>

#### Breakdown

This section covered the data encoding via LabelEncoder, the balanced random forest classifier as well as the easy ensemble classifier. 

#### Q&A

__Q1__: Which model had the best balanced accuracy score ? </br>
__A__: Easy ensemble classifier.

__Q2__: Which model had the best recall score ? </br>
__A__: Easy ensemble classifier and the balanced random forest classifier have the same recall score: 0.99.

__Q3__: Which model had the best geometric mean score ? </br>
__A__: Easy ensemble classifier and the balanced random forest classifier have the same geometric mean score: 0.99.

__Q4__: What are the top three features ? </br>
__A__: debt_to_income, interest_rate and borrower_income. 


