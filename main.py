import os
from flask import Flask, json, jsonify, request, render_template
import tensorflow as tf
import pandas as pd
import numpy as np
import six 
import random

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
model_sequential = tf.keras.models.load_model("sequential")

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/prediction')
def prediction_form():
    return render_template('prediction_form.html')



@app.route('/prediction_result', methods=['POST'])
def submit():
    
    #Model Features
    Pclass = int(request.values.get('Pclass'))
    Cabin = int(request.values.get('Cabin'))
    Age = int(request.values.get('Age'))
    Gender = int(request.values.get('Sex'))
    P_Embarkation = int(request.values.get('Embarkation'))
    Name_Title = int(request.values.get('NameTitle'))
    Trav_Aln = int(request.values.get('TravelAlone'))
         
    if Trav_Aln == 1:
        Travel_Relative = 0
    else:
        Travel_Relative = int(request.values.get('TravelNum'))
    
    ### Model Prediction 
    features = np.array([Pclass, Cabin, Age, Gender, P_Embarkation, Name_Title, Trav_Aln, Travel_Relative]).reshape(1,8)
    prediction_sequential = round(model_sequential.predict(features)[0][0], 4)
    round_pred = round(100*prediction_sequential)
    response = {'Surv_pred': prediction_sequential}
    resp_main = ("You will Survive!") if prediction_sequential > 0.5 else ("You will not Survive!")
    resp_sec = ("Your chances to Survive are high enough with " + u"\u2248 " + str(round_pred) + "%") if prediction_sequential > 0.5 else ("Your chances to Survive are not high enough with " + u"\u2248 " + str(round_pred) + "%") if prediction_sequential < 0.5 else ("Your chances to Survive are even with " + u"\u2248 " + str(round_pred) + "%")
    
    d_Pclass = "First Class" if Pclass == 1 else "Second Class" if Pclass == 2 else "Third Class"
    d_Cabin = "Yes" if Cabin == 0 else "No"
    d_Age = str(Age) + " years old"
    d_Gender = "Female" if Gender == 0 else "Male"
    d_P_Embarkation = "Cherbourg" if P_Embarkation == 0 else "Queenstown" if P_Embarkation == 1 else "Southampton"
    d_Name_Title = "Mr." if Name_Title == 0 else "Miss." if Name_Title == 1 else "Mrs." if Name_Title == 2 else "Master." if Name_Title == 3 else "Other Title"
    d_Trav_Aln = "No" if Trav_Aln == 0 else "Yes"
    d_Travel_Relative = str(Travel_Relative) + " relative(s)" if Travel_Relative > 1 else str(Travel_Relative) + " relative"
    
    data = {"Pclass": d_Pclass,
            "Cabin": d_Cabin,
            "Age": d_Age,
            "Gender": d_Gender,
            "P_Embarkation": d_P_Embarkation, 
            "Name_Title": d_Name_Title,
            "Trav_Aln": d_Trav_Aln,
            "Travel_Relative": d_Travel_Relative}
    
    return render_template('result_pred.html', pred_val = response, data=data, resp_main = resp_main, resp_sec = resp_sec)

@app.route('/prediction_result')
def random_submit():
       
    #Model Features
    Pclass = random.randint(1, 3)
    Cabin = random.randint(0, 1)
    Age = random.randint(1, 75)
    Gender = random.randint(0, 1)
    P_Embarkation = random.randint(0, 2)
    Name_Title = random.randint(0, 4)
    Trav_Aln = random.randint(0, 1)
    
    if Pclass == 1 or Pclass == 2:
        if Gender == 0:
            if Age > 21:
                Name_Title = random.choice([1, 2, 4])
            else:
                Name_Title = random.choice([1, 2])
        elif Gender == 1:
                Name_Title = random.choice([0, 3, 4])
    if Pclass == 3:
        if Gender == 0:
            if Age > 21:
                Name_Title = random.choice([1, 2])
            else:
                Name_Title = random.choice([1])
        elif Gender == 1:
                Name_Title = random.choice([0, 3])
        
    if Age < 16:
        Trav_Aln = 0
    else: 
        Trav_Aln = random.randint(0, 1)

    if Trav_Aln == 1:
        Travel_Relative = 0
    else:
        Travel_Relative = random.randint(1, 6)
    
    ### Model Prediction 
    features = np.array([Pclass, Cabin, Age, Gender, P_Embarkation, Name_Title, Trav_Aln, Travel_Relative]).reshape(1,8)
    prediction_sequential = round(model_sequential.predict(features)[0][0], 4)
    round_pred = round(100*prediction_sequential)
    response = {'Surv_pred': prediction_sequential}
    resp_main = ("You will Survive!") if prediction_sequential > 0.5 else ("You will not Survive!")
    resp_sec = ("Your chances to Survive are high enough with " + u"\u2248 " + str(round_pred) + "%") if prediction_sequential > 0.5 else ("Your chances to Survive are not high enough with " + u"\u2248 " + str(round_pred) + "%") if prediction_sequential < 0.5 else ("Your chances to Survive are even with " + u"\u2248 " + str(round_pred) + "%")
    
    d_Pclass = "First Class" if Pclass == 1 else "Second Class" if Pclass == 2 else "Third Class"
    d_Cabin = "Yes" if Cabin == 0 else "No"
    d_Age = str(Age) + " years old"
    d_Gender = "Female" if Gender == 0 else "Male"
    d_P_Embarkation = "Cherbourg" if P_Embarkation == 0 else "Queenstown" if P_Embarkation == 1 else "Southampton"
    d_Name_Title = "Mr." if Name_Title == 0 else "Miss." if Name_Title == 1 else "Mrs." if Name_Title == 2 else "Master." if Name_Title == 3 else "Other Title"
    d_Trav_Aln = "No" if Trav_Aln == 0 else "Yes"
    d_Travel_Relative = str(Travel_Relative) + " relative(s)" if Travel_Relative > 1 else str(Travel_Relative) + " relative"
    
    data = {"Pclass": d_Pclass,
            "Cabin": d_Cabin,
            "Age": d_Age,
            "Gender": d_Gender,
            "P_Embarkation": d_P_Embarkation, 
            "Name_Title": d_Name_Title,
            "Trav_Aln": d_Trav_Aln,
            "Travel_Relative": d_Travel_Relative}
    
    return render_template('result_pred.html', pred_val = response, data=data, resp_main = resp_main, resp_sec = resp_sec)
 
@app.route('/prediction_result_firstclass')
def random_firstclass():
       
    #Model Features
    Pclass = 1
    Cabin = random.randint(0, 1)
    Age = random.randint(1, 75)
    Gender = random.randint(0, 1)
    P_Embarkation = random.randint(0, 2)
    Trav_Aln = random.randint(0, 1)
    

    if Gender == 0:
        if Age > 21:
            Name_Title = random.choice([4])
        else:
            Name_Title = random.choice([1, 2])
    elif Gender == 1:
            Name_Title = random.choice([3, 4])
        
    if Age < 16:
        Trav_Aln = 0
    else: 
        Trav_Aln = random.randint(0, 1)

    if Trav_Aln == 1:
        Travel_Relative = 0
    else:
        Travel_Relative = random.randint(1, 6)
    
    ### Model Prediction 
    features = np.array([Pclass, Cabin, Age, Gender, P_Embarkation, Name_Title, Trav_Aln, Travel_Relative]).reshape(1,8)
    prediction_sequential = round(model_sequential.predict(features)[0][0], 4)
    round_pred = round(100*prediction_sequential)
    response = {'Surv_pred': prediction_sequential}
    resp_main = ("You will Survive!") if prediction_sequential > 0.5 else ("You will not Survive!")
    resp_sec = ("Your chances to Survive are high enough with " + u"\u2248 " + str(round_pred) + "%") if prediction_sequential > 0.5 else ("Your chances to Survive are not high enough with " + u"\u2248 " + str(round_pred) + "%") if prediction_sequential < 0.5 else ("Your chances to Survive are even with " + u"\u2248 " + str(round_pred) + "%")
    
    d_Pclass = "First Class"
    d_Cabin = "Yes" if Cabin == 0 else "No"
    d_Age = str(Age) + " years old"
    d_Gender = "Female" if Gender == 0 else "Male"
    d_P_Embarkation = "Cherbourg" if P_Embarkation == 0 else "Queenstown" if P_Embarkation == 1 else "Southampton"
    d_Name_Title = "Mr." if Name_Title == 0 else "Miss." if Name_Title == 1 else "Mrs." if Name_Title == 2 else "Master." if Name_Title == 3 else "Other Title"
    d_Trav_Aln = "No" if Trav_Aln == 0 else "Yes"
    d_Travel_Relative = str(Travel_Relative) + " relative(s)" if Travel_Relative > 1 else str(Travel_Relative) + " relative"
    
    data = {"Pclass": d_Pclass,
            "Cabin": d_Cabin,
            "Age": d_Age,
            "Gender": d_Gender,
            "P_Embarkation": d_P_Embarkation, 
            "Name_Title": d_Name_Title,
            "Trav_Aln": d_Trav_Aln,
            "Travel_Relative": d_Travel_Relative}
    
    return render_template('result_pred.html', pred_val = response, data=data, resp_main = resp_main, resp_sec = resp_sec)
 

@app.route('/prediction_result_secondclass')
def random_secondclass():
       
    #Model Features
    Pclass = 2
    Cabin = random.randint(0, 1)
    Age = random.randint(1, 75)
    Gender = random.randint(0, 1)
    P_Embarkation = random.randint(0, 2)
    Trav_Aln = random.randint(0, 1)
    
    if Gender == 0:
        if Age > 21:
            Name_Title = random.choice([1, 2, 4])
        else:
            Name_Title = random.choice([1, 2])
    elif Gender == 1:
            Name_Title = random.choice([0, 3, 4])
    
    if Age < 16:
        Trav_Aln = 0
    else: 
        Trav_Aln = random.randint(0, 1)

    if Trav_Aln == 1:
        Travel_Relative = 0
    else:
        Travel_Relative = random.randint(1, 6)
    
    ### Model Prediction 
    features = np.array([Pclass, Cabin, Age, Gender, P_Embarkation, Name_Title, Trav_Aln, Travel_Relative]).reshape(1,8)
    prediction_sequential = round(model_sequential.predict(features)[0][0], 4)
    round_pred = round(100*prediction_sequential)
    response = {'Surv_pred': prediction_sequential}
    resp_main = ("You will Survive!") if prediction_sequential > 0.5 else ("You will not Survive!")
    resp_sec = ("Your chances to Survive are high enough with " + u"\u2248 " + str(round_pred) + "%") if prediction_sequential > 0.5 else ("Your chances to Survive are not high enough with " + u"\u2248 " + str(round_pred) + "%") if prediction_sequential < 0.5 else ("Your chances to Survive are even with " + u"\u2248 " + str(round_pred) + "%")
    
    d_Pclass = "Second Class"
    d_Cabin = "Yes" if Cabin == 0 else "No"
    d_Age = str(Age) + " years old"
    d_Gender = "Female" if Gender == 0 else "Male"
    d_P_Embarkation = "Cherbourg" if P_Embarkation == 0 else "Queenstown" if P_Embarkation == 1 else "Southampton"
    d_Name_Title = "Mr." if Name_Title == 0 else "Miss." if Name_Title == 1 else "Mrs." if Name_Title == 2 else "Master." if Name_Title == 3 else "Other Title"
    d_Trav_Aln = "No" if Trav_Aln == 0 else "Yes"
    d_Travel_Relative = str(Travel_Relative) + " relative(s)" if Travel_Relative > 1 else str(Travel_Relative) + " relative"
    
    data = {"Pclass": d_Pclass,
            "Cabin": d_Cabin,
            "Age": d_Age,
            "Gender": d_Gender,
            "P_Embarkation": d_P_Embarkation, 
            "Name_Title": d_Name_Title,
            "Trav_Aln": d_Trav_Aln,
            "Travel_Relative": d_Travel_Relative}
    
    return render_template('result_pred.html', pred_val = response, data=data, resp_main = resp_main, resp_sec = resp_sec)
 

@app.route('/prediction_result_thirdclass')
def random_thirdclass():
       
    #Model Features
    Pclass = 3
    Cabin = random.randint(0, 1)
    Age = random.randint(1, 75)
    Gender = random.randint(0, 1)
    P_Embarkation = random.randint(0, 2)
    Trav_Aln = random.randint(0, 1)
    
    if Gender == 0:
        if Age > 21:
            Name_Title = random.choice([1, 2])
        else:
            Name_Title = random.choice([1])
    elif Gender == 1:
            Name_Title = random.choice([0])
            
    if Age < 16:
        Trav_Aln = 0
    else: 
        Trav_Aln = random.randint(0, 1)

    if Trav_Aln == 1:
        Travel_Relative = 0
    else:
        Travel_Relative = random.randint(1, 6)
    
    ### Model Prediction 
    features = np.array([Pclass, Cabin, Age, Gender, P_Embarkation, Name_Title, Trav_Aln, Travel_Relative]).reshape(1,8)
    prediction_sequential = round(model_sequential.predict(features)[0][0], 4)
    round_pred = round(100*prediction_sequential)
    response = {'Surv_pred': prediction_sequential}
    resp_main = ("You will Survive!") if prediction_sequential > 0.5 else ("You will not Survive!")
    resp_sec = ("Your chances to Survive are high enough with " + u"\u2248 " + str(round_pred) + "%") if prediction_sequential > 0.5 else ("Your chances to Survive are not high enough with " + u"\u2248 " + str(round_pred) + "%") if prediction_sequential < 0.5 else ("Your chances to Survive are even with " + u"\u2248 " + str(round_pred) + "%")
    
    d_Pclass = "Third Class"
    d_Cabin = "Yes" if Cabin == 0 else "No"
    d_Age = str(Age) + " years old"
    d_Gender = "Female" if Gender == 0 else "Male"
    d_P_Embarkation = "Cherbourg" if P_Embarkation == 0 else "Queenstown" if P_Embarkation == 1 else "Southampton"
    d_Name_Title = "Mr." if Name_Title == 0 else "Miss." if Name_Title == 1 else "Mrs." if Name_Title == 2 else "Master." if Name_Title == 3 else "Other Title"
    d_Trav_Aln = "No" if Trav_Aln == 0 else "Yes"
    d_Travel_Relative = str(Travel_Relative) + " relative(s)" if Travel_Relative > 1 else str(Travel_Relative) + " relative"
    
    data = {"Pclass": d_Pclass,
            "Cabin": d_Cabin,
            "Age": d_Age,
            "Gender": d_Gender,
            "P_Embarkation": d_P_Embarkation, 
            "Name_Title": d_Name_Title,
            "Trav_Aln": d_Trav_Aln,
            "Travel_Relative": d_Travel_Relative}
    
    return render_template('result_pred.html', pred_val = response, data=data, resp_main = resp_main, resp_sec = resp_sec)
 

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google Cloud
    # Run, a webserver process such as Gunicorn will serve the app.
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8082)))