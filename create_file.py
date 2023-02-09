from flask import Flask, request
from flask import Flask, request, jsonify
from waitress import serve
from datetime import datetime
import datetime

import pandas as pd
import pathlib

import os

app = Flask(__name__)
current_time = datetime.datetime.now()
time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

current_time = datetime.datetime.now()
time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
df = pd.DataFrame({'date':['07/02/2023']})
file = pathlib.Path('file_name')
file.unlink

@app.route('/', methods=['GET'])
def welcome():
    return {"Status": True, "Nama": "belajar_python", "Time": time_str}


@app.route('/create_file', methods=['POST','GET'])
def create_file():
    file_content = request.form.get('file_content')
    file_name = request.form.get('file_name')
    message = "File {} has been created".format(file_name)
    
    if request.method == 'GET' :
        return {'status': False}
        
    if request.method == 'POST' :
        with open(file_name, "w") as file:
            file.write(file_content)
    
        return f"File '{file_name}' created successfully!\n Time completion {time_str}"
try:
    if request.method == "POST" :
        with open(file_name, "w") as file:
            file.write(file_content)
        return jsonify({"Error": str(e)}), 500

@app.route('/delete_file', methods=['POST'])
def delete_file():
    file_name = request.form.get('file_name')
    message = "File {} has been deleted".format(file_name)
    try:
        os.remove(file_name)
        return jsonify({"message": message, "Timestamp": time_str}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
    serve(app, host='0.0.0.0', threads=1)
    serve(app, host='0.0.0.0', port=8080, threads=1)
 