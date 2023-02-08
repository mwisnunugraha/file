from flask import Flask, request, jsonify
from waitress import serve
import datetime
import os

# global variable used by all function that call it
app = Flask(__name__)
current_time = datetime.datetime.now()
time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

# Get status if this function and route been called
@app.route('/', methods=['GET'])
def welcome():
    return {"Status": True, "Nama": "belajar_python", "Time": time_str}

# create file name with content file write after post it
# and adding error if something doesn't right
@app.route('/create_file', methods=['POST','GET'])
def create_file():
    file_content = request.form.get('file_content')
    file_name = request.form.get('file_name')
    message = "File {} has been created".format(file_name)
    
    if request.method == 'GET' :
        return {'status': False}
    
    try:
        if request.method == 'POST' :
            with open(file_name, "w") as file:
                file.write(file_content)
            return jsonify({"message": message, "Timestamp": time_str}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500


# delete file name with extension, return with message if success
# and return false with error if file doesn't exist
@app.route('/delete_file', methods=['POST'])
def delete_file():
    file_name = request.form.get('file_name')
    message = "File {} has been deleted".format(file_name)
    try:
        os.remove(file_name)
        return jsonify({"message": message, "Timestamp": time_str}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

# main function
# it means that code enclosed  in if __name__ == "__main__": block will only be executed if the file is run as the main program
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080, threads=1)
