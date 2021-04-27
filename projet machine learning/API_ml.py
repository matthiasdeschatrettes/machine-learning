#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
from flask import Flask, request, jsonify, render_template
import pandas as pd

DATAsim = pd.read_csv("DATAsim.csv")


api = Flask(__name__)


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/predict',methods=['POST'])
def predict():

    int_predict = [int(x) for x in request.form.values()]
    final_predict = [np.array(int_predict)]
    prediction = DATAsim.predict(final_predict)

    output = round(prediction[0], 2)

    return render_template('homepage.html', prediction_text='risque :'.format(output))


@app.route('/results',methods=['POST'])
def results():

    dt = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:





# In[ ]:




