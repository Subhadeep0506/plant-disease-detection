import numpy as np
import json
import os
import cv2

from keras.models import load_model
from flask import Flask, request, render_template


app = Flask(__name__)

# MODEL_PATH = 'models/latest_model.h5'
MODEL_PATH = 'models/model_dnet121.h5'

diseases_dict = None
with open("./diseases.json") as json_data:
    diseases_dict = json.load(json_data)

model = load_model(MODEL_PATH)

print('Page is being served at http://127.0.0.1:5000/')


def model_predict(img_path, model):
    """
        Takes in image path and the model being used and returns the predicted class-wise probabilities.

        `image_path` and `model` cannot be None.

        Parameters
        ----------
        image_path: str
            Actual path of uploaded image file that will be used for predicting.
        
        model: Any
            The Tensorflow model that will be used to predict the input image disease class.

        Returns
        -------
        pred: Any
            Returns the class-wise probabilities of the input image, as predicted by the given model.
    """
    img = cv2.imread(img_path)
    new_arr = cv2.resize(img, (128, 128))
    new_arr = np.array(new_arr/255)
    new_arr = new_arr.reshape(-1, 128, 128, 3)

    preds = model.predict(new_arr)
    return preds


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', f.filename)
        f.save(file_path)

        preds = model_predict(file_path, model)

        pred_class = preds.argmax()
        
        CATEGORIES = [
            'Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy',
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
