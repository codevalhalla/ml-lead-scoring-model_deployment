#!/usr/bin/env python
# coding: utf-8

import pickle
from flask import Flask,request,jsonify

input_file = "pipeline_v1.bin"

#load the model
with open(input_file,'rb') as f_in:
    dv,model = pickle.load(f_in) 
    
#initialize the flask app
app = Flask("lead_scoring_app")

@app.route("/predict",methods=["POST"])
def predict():
    lead_data = request.get_json()
    X = dv.transform([lead_data])
    y_pred = model.predict_proba(X)[0,1]
    
    result = {
        'lead_conversion_probability': float(y_pred)
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=9696)

    