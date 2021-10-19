from flask import Flask, render_template,request
from config import *
from work_order import * 


app = Flask(__name__)

@app.route("/")
def index():
  print('done')
  return render_template('index.html', **dict_default)

@app.route("/get_probability", methods=['POST'])
def get_probability():
    input_values = {
        'age'       : request.form['value_age'],
        'employment': request.form['value_employment'],
        'graduate'  : request.form['value_graduate'],
        'income'    : request.form['value_income'], 
        'family'    : request.form['value_family'], 
        'disease'   : request.form['value_disease'],  
        'frequent'  : request.form['value_frequent'],  
        'abroad'    : request.form['value_abroad'],
        'model'     : request.form['value_model']
    }
    return render_template('index.html',**post_values_to_page(**input_values))