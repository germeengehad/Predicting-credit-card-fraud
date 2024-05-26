   #  Predicting credit card fraud  :Project Overview
   ![credit card Image](https://github.com/germeengehad/Predicting-credit-card-fraud/blob/main/The-framework-of-credit-card-fraud-detection.png)
   

- This project aims to predict credit card fraud using data from transactions made by European cardholders in 2023. The dataset includes over 550,000 records and has been anonymized to protect cardholders' identities. The primary objective is to develop algorithms and models that can identify potentially fraudulent transactions effectively.
- I plan to conduct an exploratory data analysis (EDA) on my dataset, followed by feature engineering and selection, and then create pipelines for model training and prediction. Specifically, I have developed pipelines for both the KMeans and GaussianMixture models to predict labels for each data point. For each model.

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

# Feature Engineering And Feature Selection 
- Applying Filter Methods (correlation analysis)
- Applying Variance Threshold

# Creating Pipelines and making predictions
I made a pipeline for the Kmeans model and GaussianMixture model to be apple from predict labels for each data point, and for each model, I applied
 - Data Preprocessing using MinMax Scaler
 - handling missing values with means
 - Fitting the pipelines and predict labels

# Models Performance 
- Results for kmeans_pipeline_model: 
    Accuracy score: 90.01%

- Results for GaussianMixture_pipeline_model: 
    Accuracy score: 91.82%

# Pickel The Best Model
- Importing Pickle
- Saving the Model
- Loading the Model

 # Creating A Fast Api 
 - Develop My FastAPI Application
 - Run My FastAPI Application
 - Creat a readme file of My Api File 

    



  

  
  
  

