from flask import Flask, render_template, request
from PIL import Image
#import pickle 
from tensorflow.keras.models import load_model
import numpy as np
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'


class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")

@app.route('/file:///Users/Desktop/TSF%20Machine%20Learning/')
#load machine learning model
model = load_model('model.py')

class_names = ['MildDementia', 'ModerateDementia', 'NonDementia', 'VeryMildDementia']

#define flask route
@app.route('/file:///Users/mel/Desktop/TSF%20Machine%20Learning/templates/home.html')
def home():
    return render_template('/file:///Users/mel/Desktop/TSF%20Machine%20Learning/templates/home.html')

@app.route('/file:///Users/mel/Desktop/TSF%20Machine%20Learning/templates/prediction.html', methods=['GET','POST'])
def predict():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        return "File has been uploaded."
    """input_data = request.files['image']
    image = Image.open(input_data)"""
   """ #make a prediction with model
    prediction = model.predict(np.array(image).reshape(1, -1))
    label_index = np.argmax(prediction, axis=1)[0]
    label = class_names[label_index]"""
    return render_template('/file:///Users/mel/Desktop/TSF%20Machine%20Learning/templates/prediction.html', label=label, `form=form)`

"""@app.route('/file:///Users/Desktop/TSF%20Machine%20Learning/predictionResults.html', methods=['POST'])
def predict_results():
    return render_template('predictionResults.html')"""

@app.route('/file:///Users/Desktop/TSF%20Machine%20Learning/TSF%20Machine%20Learning/templates/predictionResults', methods = ['GET','POST'])
def upload():
    image = request.files['image']
    image.save('/file:///Users/mel/Desktop/TSF%20Machine%20Learning/upload/image.jpg', methods = ['POST'])
    return render_template('/file:///Users/Desktop/TSF%20Machine%20Learning/templates/predictionResults.html')
    
#run flask app
#run with python app.py
if __name__ == '__main__':
    app.run(debug=True)