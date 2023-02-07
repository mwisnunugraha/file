from flask import Flask, request
from waitress import serve
from datetime import datetime
import datetime
<<<<<<< HEAD
import pandas as pd
import pathlib
=======
>>>>>>> 4de62534c0cbbfd7dc25db5dde9ccb03754c97ca

app = Flask(__name__)
current_time = datetime.datetime.now()
time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

<<<<<<< HEAD
current_time = datetime.datetime.now()
time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
df = pd.DataFrame({'date':['07/02/2023']})
file = pathlib.Path('file_name')
file.unlink

=======
>>>>>>> 4de62534c0cbbfd7dc25db5dde9ccb03754c97ca
@app.route('/', methods=['GET'])
def welcome():
    return {"Status": True, "Nama": "belajar_python", "Time": time_str}


@app.route('/create_file', methods=['POST','GET'])
def create_file():
    file_content = request.form.get('file_content')
    file_name = request.form.get('file_name')
    
    if request.method == 'GET' :
        return {'status': False}
        
    if request.method == 'POST' :
        with open(file_name, "w") as file:
            file.write(file_content)
    
<<<<<<< HEAD
        return f"File '{file_name}' created successfully!\n Time completion {time_str}"
=======
        return f"File '{file_name}' created successfully!\n Time completion: {time_str}"
>>>>>>> 4de62534c0cbbfd7dc25db5dde9ccb03754c97ca


if __name__ == '__main__':
    app.run(debug=True)
    serve(app, host='0.0.0.0', threads=1)
