#!/usr/bin/env python
# coding: utf-8

import requests

url = "http://0.0.0.0:9696/predict"

client={
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

response = requests.post(url, json=client)

if response.status_code == 200:
    print("Lead Conversion Probability:", response.json()["lead_conversion_probability"])
else:
    print("Error:", response.status_code, response.text)
