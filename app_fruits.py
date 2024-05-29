from flask import Flask, render_template, request, url_for, redirect
import pickle
import numpy as np

model=pickle.load(open('fruits.pkl','rb'))

app_ml = Flask(__name__)

@app_ml.route('/')
def man():
    return render_template('web_fruit.html')

@app_ml.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        sl=float(request.form['a'])
        sw=float(request.form['b'])
        pl=float(request.form['c'])
        pw=float(request.form['d'])
        arr=[[sl,sw,pl,pw]]
        pred=model.predict(arr)
        return render_template("after_pred-fruits.html", result=pred)

if __name__ == '__main__':
    app_ml.run(debug=True)