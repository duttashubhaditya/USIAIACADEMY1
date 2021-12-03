# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 13:30:58 2021

@author: shubdutta
"""

from flask import Flask,render_template,request
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import model_selection
import os 
import tensorflow as tf 
from tensorflow import keras 
import pickle
app = Flask(__name__)

if __name__ == '__main__':
    @app.route('/')
    def hello():
        return "Hello World!"
    @app.route('/home/dashboard')     
    def home():         
        return "You are in home page"          
    @app.route('/list', methods=["GET"])     
    def list():         
        names = ['amarnath', 'ram', 'goyal']         
        return str(names)      
    @app.route('/dic', methods=["GET", "POST"])     
    def dic():         
        names = {'id':1, 'name':'Amarnath', 'designation':'consultant'}
        return names
    @app.route('/dashboard')
    def dashboard():
        return render_template("home.html", title="Employee")
    @app.route('/train')     
    def train():         
        url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"         
        names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']         
        dataframe = pd.read_csv(url, names=names)         
        array = dataframe.values         
        X = array[:,0:8]         
        Y = array[:,8]         
        test_size = 0.33              
        X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size)         
        model = LogisticRegression()
        model.fit(X_train, Y_train)
        # save the model to disk
        filename = 'finalized_model.sav'
        pickle.dump(model, open(filename, 'wb'))
        return "trained"
        
    @app.route('/test')
    def test():
        filename = 'finalized_model.sav'
        loaded_model = pickle.load(open(filename, 'rb')) 
        url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv" 
        names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] 
        dataframe = pd.read_csv(url, names=names) 
        array = dataframe.values 
        X = array[:,0:8] 
        Y = array[:,8] 
        test_size = 0.33 
        X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size) 
        result = loaded_model.score(X_test, Y_test) 
        print(result) 
        return "tested"
    
    # @app.route('/iris/test')
    # def iris_test():
    #     pkl_filename = 'iris_model.pkl' 
    #     with open(pkl_filename, 'rb') as file: 
    #         pickle_model = pickle.load(file) 
    #     sample = [[6.4, 2.8, 5.6, 2.1]] 
    #     Ypredict = pickle_model.predict(sample) 
    #     print("Ypredict", Ypredict) 
    #     return str(Ypredict[0])
    
    @app.route('/iris/input')
    def iris_input():
        return render_template("iris_input.html")

    
    @app.route('/iris/test', methods=['GET'])    
    def iris_test_arg():
        print(request.args)        
        f1 = request.args["f1"]        
        f2 = request.args["f2"]        
        f3 = request.args["f3"]        
        f4 = request.args["f4"]        
        pkl_filename = 'iris_model.pkl'        
        with open(pkl_filename, 'rb') as file:
            pickle_model = pickle.load(file) 
        sample = [[f1, f2, f3, f4]]
        Ypredict = pickle_model.predict(sample) 

        print("Ypredict", Ypredict) 

        return str(Ypredict[0])
    
    # @app.route('/text/test2')
    # def text_test():
    #     pkl_filename = 'text_analysis.hdf5' 
    #     with open(pkl_filename, 'rb') as file: 
    #         pickle_model = pickle.load(file) 
    #     sample = ['I just had a knee surgery'] 
    #     Ypredict = pickle_model.predict(sample) 
    #     print("Ypredict", Ypredict) 
    #     return str(Ypredict[0])

    app.run(host='0.0.0.0', debug=True, port=5000)

    

