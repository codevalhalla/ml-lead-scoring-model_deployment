#!/usr/bin/env python
# coding: utf-8

import requests

url='http://localhost:9696/predict'

lead_details = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}


response = requests.post(url,json=lead_details).json()
print(response['lead_conversion_probability'])



