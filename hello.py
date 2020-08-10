from flask import Flask, request, jsonify, abort, redirect, url_for, render_template, send_file
from sklearn.externals import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello, my very best friend!!!!!!!</h1>'