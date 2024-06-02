from typing import Any, List
import email
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
import schemas

    
router = APIRouter(
    prefix="/GMM model", 
    tags=["GMM model"]
    )

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
from schemas import  ModelInput
from pydantic import BaseModel
from schemas import ExceptionHandler


# Load the saved GMM model
with open('gmm7_model.sav', "rb") as model_file:
    gmm_model = pickle.load(model_file)



@router.post("/predict")
def predict(item: ModelInput=Body()):
    
    input_data = item.dict()
    input_df = pd.DataFrame([input_data])  # Convert input data to DataFrame


    # Make predictions using the model directly
    prediction = gmm_model.predict(input_df)

    if prediction[0] == 0:
        return 'The transaction is not fraudulent'
    else:
        return 'The transaction is fraudulent'