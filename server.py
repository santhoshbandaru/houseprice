import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

    
#prediction function
def ValuePredictor(x):
    z=np.zeros(len(x.columns))
    z[0]=x[0]
    z[1]=x[1]
    z[2]=x[-1]
    loaded_model = pickle.load(open("house_price_model.pkl","rb"))
    result = loaded_model.predict([z])[0]

    return result[0]

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)

            
        return render_template("result.html",result=result)