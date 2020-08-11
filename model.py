from tensorflow.python.keras import backend as K
import tensorflow as tf
import glob
import numpy as np
import onnxruntime
import json
from tensorflow.keras.applications.xception import preprocess_input



def load_models():
    model_paths = glob.glob('*.onnx')
    model_dicts = {}
    for model_path in model_paths:
        print(model_path)
        model_dicts[model_path.replace('.onnx','').replace('model_','')] = onnxruntime.InferenceSession(model_path)
    return model_dicts

def predict(image, models, categ_dict):
    data = tf.image.resize(tf.image.decode_image(image,channels=3), (280,280))/255.
    x = np.expand_dims(data.numpy(), axis=0)
    # x = preprocess_input(x)
    x = x if isinstance(x, list) else [x] 
    list_atrs = []
    for name,model in models.items():
        feed = dict([(input.name, x[n]) for n, input in enumerate(model.get_inputs())])  
        prediction = model.run(None,feed)[0]   
        categ_to_predict = categ_dict[name]  
        list_atrs.append({categ_to_predict[str(i)]:float(j) for i,j in [*enumerate(prediction[0])]})
    return list_atrs

def load_categ():
    with open('categ.json', 'r', encoding='utf-8') as file:
        categ_dict = json.load(file)
    return categ_dict

def predicted_atr_html(list_atrs):
    list_atrs = [[f'<b>{atr}</b>  = {round(prob*100,3)}% <br>'
                    for atr,prob in atr_dict.items()] for atr_dict in list_atrs]
    list_atrs = ['<p>'+"\n".join(atr_list)+'</p>' for atr_list in list_atrs]
    return "\n\n".join(list_atrs)



