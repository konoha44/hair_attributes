from tensorflow.python.keras import backend as K
from tensorflow.python.keras.preprocessing import image
import sys
import numpy as np
import onnxruntime


def load_models():
    onnx_model = 'model.onnx'
    sess = onnxruntime.InferenceSession(onnx_model)
    return sess