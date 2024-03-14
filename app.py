# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 23:34:05 2023

@author: UBED
"""
'''


from tensorflow.keras.preprocessing import image
from tensorflow.keras.utils import load_img
from keras.models import load_model
import os
from flask import Flask, flash, request, redirect, url_for,jsonify



from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image
from flask import Flask, render_template, request

result = {
          0: 'Amaranthus Green', 1: 'Amaranthus Red', 2: 'Balloon vine', 3: 'Betel Leaves', 4: 'Black Night Shade', 5: 'Celery', 6: 'Chinese Spinach', 7: 'Coriander Leaves', 8: 'Curry Leaf',
          9: 'Dwarf Copperleaf (Green)', 10: 'Dwarf copperleaf (Red)', 11: 'False Amarnath', 12: 'Fenugreek Leaves', 13: 'Giant Pigweed', 14: 'Gongura', 15: 'Indian pennywort', 16: 'Lagos Spinach',
          17: 'Lambs Quarters', 18: 'Lettuce Tree', 19: 'Malabar Spinach (Green)', 20: 'Mint Leaves', 21: 'Mustard', 22: 'Palak', 23: 'Siru Keerai', 24: 'Water Spinach'
        }

#Predicting Image
MODEL_PATH = 'CNN_model.h5'
model_dl = load_model(MODEL_PATH)


app = Flask(__name__)

@app.route("/")
def hello_world():
    
    return render_template("index.html")
    # return "<p>Hello, World!</p>"


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded.', 400

    file = request.files['file']
    if file.filename == '':
        return 'No file selected.', 400

    # Save the file to the "image" folder
    file.save(os.path.join('image', file.filename))

    temp_path = os.path.join('image',file.filename)

    # Preprocess the image for the model
    img = image.load_img(temp_path, target_size=(224, 224))
    img_arr = np.expand_dims(img, axis=0)
    img_arr = image.img_to_array(img)
    img_arr = np.vstack([img_arr])

    # Make a prediction with the model
    Result = model_dl.predict(img_arr)
    prediction_index = np.argmax(Result)
    # print(Result,prediction_index)
    prediction = result[prediction_index]

    # Remove the temporary file
    # os.remove(temp_path)

    # Return the prediction as a JSON response
    response = {'prediction': str(prediction)}
    return jsonify(response)


if __name__ == '__main__':
    app.run()

'''


from tensorflow.keras.preprocessing import image
from tensorflow.keras.utils import load_img
from keras.models import load_model
import os
from flask import Flask, flash, request, redirect, url_for,jsonify



from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image
from flask import Flask, render_template, request

import tempfile
app=Flask(__name__)

result  = {0: 'Amaranthus Green', 1: 'Amaranthus Red', 2: 'Balloon vine', 3: 'Betel Leaves', 4: 'Black Night Shade', 5: 'Celery', 6: 'Chinese Spinach', 7: 'Coriander Leaves', 8: 'Curry Leaf', 9: 'Dwarf Copperleaf (Green)', 10: 'Dwarf copperleaf (Red)', 11: 'False Amarnath', 12: 'Fenugreek Leaves', 13: 'Giant Pigweed', 14: 'Gongura', 15: 'Indian pennywort', 16: 'Lagos Spinach', 17: 'Lambs Quarters', 18: 'Lettuce Tree', 19: 'Malabar Spinach (Green)', 20: 'Mint Leaves', 21: 'Mustard', 22: 'Palak', 23: 'Siru Keerai', 24: 'Water Spinach'}
MODEL_PATH =   'CNN_model.h5'

model_dl = load_model(MODEL_PATH)
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        img_file = request.files['image']
        
        # Save the temporary file
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            img_file.save(temp.name)
            temp_path = temp.name
        
        # Preprocess the image for the model
        img = image.load_img(temp_path, target_size=(224, 224))
        img_arr = image.img_to_array(img)
        img_arr = np.expand_dims(img_arr, axis=0)
        img_arr = np.vstack([img_arr])
        
        # Make a prediction with the model
        Result = model_dl.predict(img_arr)
        prediction_index = np.argmax(Result)
        prediction = result[prediction_index]
        
        # Remove the temporary file
        os.remove(temp_path)
        
        # Return the prediction as a JSON response
        response = {'prediction': str(prediction)}
        return jsonify(response)
    else:
        return "No image passed UBED"


if __name__ == '__main__':
    app.run()

