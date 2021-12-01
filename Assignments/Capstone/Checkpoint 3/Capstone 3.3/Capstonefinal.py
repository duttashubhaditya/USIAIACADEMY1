from flask import Flask
from flask import render_template,jsonify,request
import pandas as pd
from sklearn import linear_model
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
app = Flask(__name__)
if __name__ == '__main__':
    @app.route('/capstone/test')
    def capstone_test():
        print(request.args)
        f1 = request.args['f1']
        f2 = request.args['f2']
        f3 = request.args['f3']
        f4 = request.args['f4']
        f5 = request.args['f5']
        f6 = request.args['f6']
        pkl_filename = './models/Capstone_model.pkl'
        with open(pkl_filename, 'rb') as file:
            pickle_model = pickle.load(file)            
        sample = [[f1, f2, f3, f4,f5,f6]]
        Ypredict = pickle_model.predict(sample)
        print("Ypredict", Ypredict)
        if Ypredict[0]==0:
            Ypredict='Not Default'
        else:
            Ypredict='Default'
        return str(Ypredict)        
    @app.route('/capstone/input')
    def iris_input():
        return render_template("Capstonefinal.html")
    app.run(host='0.0.0.0', debug=True, port=5000)
