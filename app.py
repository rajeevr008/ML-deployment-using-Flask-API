import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    '''
    For rendering POST method and giving result back to html
    '''
    #convert all input to int
    int_features = [int(x) for x in request.form.values()]
    #convert input features to np array
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0],2)
    
    return render_template('index.html', prediction_text = "Predicted Salary should $ {}".format(output))

if __name__ == "__main__":
    app.run(debug=True)