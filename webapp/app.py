from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')