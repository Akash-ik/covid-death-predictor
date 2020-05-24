import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
country = pickle.load(open('country.pkl','rb'))
rf = pickle.load(open('rf.pkl','rb'))

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    c,d,m,noc
    d,noc,c->model
    '''
    int_features = [x for x in request.form.values()]
    l1 = list()
    int_features[1]=int(int_features[1])
    int_features[2]=int(int_features[2])
    l1.append(int_features[1] + int_features[2]*30)
    l1.append(int_features[3])
    l1.append(country[int_features[0]])
    int_features
    final_features = [np.array(l1)]
    prediction = rf.predict(final_features)
    output = round(prediction[0], 2)

    return render_template('index1.html', prediction_text='The predicted number of deaths is : {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)