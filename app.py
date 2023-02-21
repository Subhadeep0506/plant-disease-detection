import numpy as np
import json
import os
import cv2

from keras.models import load_model
from flask import Flask, request, render_template


# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = 'models/my_best_model.h5'

# Loading the diseases json into a python dictionary
diseases_dict = None
with open("./diseases.json") as json_data:
    diseases_dict = json.load(json_data)

# Load your trained model
model = load_model(MODEL_PATH)

# model._make_predict_function()
print('Page is being served at http://127.0.0.1:5000/')


def model_predict(img_path, model):
    img = cv2.imread(img_path)
    new_arr = cv2.resize(img, (100, 100))
    new_arr = np.array(new_arr/255)
    new_arr = new_arr.reshape(-1, 100, 100, 3)

    preds = model.predict(new_arr)
    return preds


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', f.filename)
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)

        # Process your result for human
        pred_class = preds.argmax()
        
        CATEGORIES = ['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy',
                      'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
                      'Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight',
                      'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot',
                      'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot',
                      'Tomato__YellowLeaf__Curl_Virus', 'Tomato_mosaic_virus',
                      'Tomato_healthy']
        return diseases_dict[CATEGORIES[pred_class]]

    return None


if __name__ == '__main__':
    app.run(debug=True)
