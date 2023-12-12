from flask import Flask,render_template,request
import pandas as pd
import pickle

app=Flask(__name__)
data=pd.read_csv(r'C:\Users\ATHUL AKSHAY\Desktop\Employee\Employee.csv')
model=pickle.load(open('employee.pkl','rb'))

@app.route('/')
def data():
    return render_template('employee.html')
@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        age=int(request.form['age'])
        experience=int(request.form['experience'])
        education=request.form['education']
        joiningyear=int(request.form['joiningyear'])
        city=request.form['city']
        paymenttier=int(request.form['paymenttier'])
        gender=request.form['gender']
        everbenched=request.form['everbenched']

        prediction=model.predict([[age,experience,education,joiningyear,
        city,paymenttier,gender,everbenched]])
        prediction=prediction[0]
        # if prediction==0:
        #     lon='0'
        # elif prediction==1:
        #     lon='1'

        return render_template('employee.html',predict=prediction)

if __name__=='__main__':
    app.run(debug=True)
