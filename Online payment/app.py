from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

def model_prediction(features):
    pickled_model = pickle.load(open('P:\\project 2024\\Online_payment_fraud_detection_randomforest.pkl', 'rb'))
    isFraud = list(pickled_model.predict(features))
    return f'The detection is {isFraud}'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    step = int(request.form['step'])
    typeup = int(request.form['typeup'])
    amount = float(request.form['amount'])
    nameOrig = int(request.form['nameOrig'])
    oldbalanceOrg = float(request.form['oldbalanceOrg'])
    newbalanceOrig = float(request.form['newbalanceOrig'])
    nameDest = int(request.form['nameDest'])
    oldbalanceDest = float(request.form['oldbalanceDest'])
    newbalanceDest = float(request.form['newbalanceDest'])
    isFlaggedFraud = int(request.form['isFlaggedFraud'])

    features = [[step, typeup, amount, nameOrig, oldbalanceOrg, newbalanceOrig, nameDest, oldbalanceDest, newbalanceDest, isFlaggedFraud]]
    result = model_prediction(features)
    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
