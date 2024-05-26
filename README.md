   #  Predicting credit card fraud  :Project Overview
   ![credit card Image](https://github.com/germeengehad/Predicting-credit-card-fraud/blob/main/The-framework-of-credit-card-fraud-detection.png)
   

- This project aims to predict credit card fraud using data from transactions made by European cardholders in 2023. The dataset includes over 550,000 records and has been anonymized to protect cardholders' identities. The primary objective is to develop algorithms and models that can identify potentially fraudulent transactions effectively.
- I plan to conduct an exploratory data analysis (EDA) on my dataset, followed by feature engineering and selection, and then create pipelines for model training and prediction. Specifically, I have developed pipelines for both the KMeans and GaussianMixture models to predict labels for each data point. For each model, the pipeline includes the following steps:

- 1) Data Preprocessing: Applying a MinMax Scaler to normalize the data.
- 2) Handling Missing Values: Imputing missing values with the mean of the respective features.
- 3) Model Fitting and Prediction: Fitting the pipeline to the data and predicting labels using the respective models.

# The Data Set
This dataset contains credit card transactions made by European cardholders in the year 2023. It comprises over 550,000 records, and the data has been anonymized to protect the cardholders' identities. The primary objective of this dataset is to facilitate the development of fraud detection algorithms and models to identify potentially fraudulent transactions.

id: Unique identifier for each transaction
V1-V28: Anonymized features representing various transaction attributes (e.g., time, location, etc.)
Amount: The transaction amount
Class: Binary label indicating whether the transaction is fraudulent (1) or not (0)
  

# EDA
- I researched methods for handling missing values and identified duplicates in the dataset.
- I generated histograms to visualize the data distribution.
- I conducted an analysis to detect outliers in the dataset.
- I checked for multicollinearity among the features.

  
  
  

