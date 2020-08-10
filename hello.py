from flask import Flask, request, jsonify, abort, redirect, url_for, render_template, send_file
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.xception import preprocess_input
from load_model import load_models
import time
import json

with open('categ.json', 'r', encoding='utf-8') as file:
    categ_dict = json.load(file)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

start = time.time()
model = load_models()
end = time.time()-start
print(f'модель загрузилась  {end}')

@app.route('/')
def hello_world():
    return '<h1>Hello, my very best friend!!!!!!!</h1>'

@app.route('/predict_atr', methods=['POST'])
def add_message():

    try:
        content = request.files
        
        image = content['image'].read()
        data = tf.image.resize(tf.image.decode_image(image,channels=3), (280,280))/255.
        x = np.expand_dims(data.numpy(), axis=0)
        x = x if isinstance(x, list) else [x] 
        feed = dict([(input.name, x[n]) for n, input in enumerate(model.get_inputs())])  
        categ_to_predict = categ_dict['Сухость']  
        prediction = model.run(None,feed)[0]   
        to_return = {categ_to_predict[str(i)]:float(j) for i,j in [*enumerate(prediction[0])]}
        print(to_return)
    

    except Exception as e:
        return str(e)

    return jsonify(to_return)