import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

#creating instance of the class
app=Flask(__name__)
model = pickle.load(open("model.pkl","rb"))

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

    
#prediction function
def ValuePredictor(x):
    z=np.zeros(4)
    z[0]=x[0]
    z[1]=x[1]
    z[2]=x[2]
    z[3]=x[3]
    print(x)
    
    result = model.predict([z])[0]
    print(result)
    return result

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        result=round(result,2)
        s='yes'
        if result<0:
            result=-1
            s='not possible'

            
        return render_template("index.html", result=s+' value in lakhs $ {}'.format(result))
if __name__=="__main__":
    app.run()