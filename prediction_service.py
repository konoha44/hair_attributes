from flask import Flask, request, jsonify, abort, redirect, url_for, render_template, send_file
import numpy as np
import tensorflow as tf
from model import load_models, predict,load_categ, predicted_atr_html
import time
import json
from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

categ_dict = load_categ()

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
app.config['JSON_AS_ASCII'] = False
UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

start = time.time()
models = load_models()
end = time.time()-start
print(f'модель загружены в память  {end}',models.keys())

@app.route('/predict_atrs', methods=['POST'])
def predict_atrs():
    try:
        content = request.files
        image = content['image'].read()
        
        predicted_atrs = predict(image, models, categ_dict)

    except Exception as e:
        return jsonify({'status':['FAILED'],'description':str(e)})

    predicted_atrs.append({'status':'OK'})
    return jsonify(predicted_atrs)

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    file = FileField()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            image = file.read()
        
            predicted_atrs = predict(image, models, categ_dict)
            output = f"""
            <!doctype html>
            <title>Предсказание атрибутов по фотографии</title>
            <center><h1>Предсказанные атрибутов по фотографии</h1></center>
            {predicted_atr_html(predicted_atrs)}
            """
            return output
            
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>