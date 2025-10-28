#!/usr/bin/env python
# coding: utf-8

from fastapi import FastAPI
from pydantic import BaseModel
import pickle

input_file = "pipeline_v1.bin"

with open(input_file, "rb") as f_in:
    dv, model = pickle.load(f_in)

app = FastAPI(title="fastapi_lead_scoring_app")

class LeadDetails(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

@app.post("/predict")
def predict(lead_data: LeadDetails):
    lead_dict = lead_data.dict()
    X = dv.transform([lead_dict])
    y_pred = model.predict_proba(X)[0, 1]

    result = {"lead_conversion_probability": float(y_pred)}
    return result
