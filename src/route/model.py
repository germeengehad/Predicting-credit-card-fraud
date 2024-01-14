import pickle
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import FunctionTransformer
from fastapi import FastAPI , Body
from fastapi import APIRouter
from data import  ModelInput
from pydantic import BaseModel


model_router = APIRouter()

# Load the saved GMM model
with open('gmm7_model.sav', "rb") as model_file:
    gmm_model = pickle.load(model_file)


@model_router.post("/predict")
def predict(item: ModelInput=Body()):
    
    input_data = item.dict()
    input_df = pd.DataFrame([input_data])  # Convert input data to DataFrame


    # Make predictions using the model directly
    prediction = gmm_model.predict(input_df)

    if prediction[0] == 0:
        return 'The transaction is not fraudulent'
    else:
        return 'The transaction is fraudulent'