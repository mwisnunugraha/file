from flask import Flask, request
from waitress import serve


app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return {"Status": True, "Nama": "belajar_python"}

@app.route('/create_file', methods=['POST'])
def create_file():
    file_content = request.form.get('file_content')
    file_name = request.form.get('file_name')
    
    with open(file_name, "w") as file:
        file.write(file_content)
    
    return f"File '{file_name}' created successfully!"

if __name__ == '__main__':
    app.run(debug=True)
    serve(app, host='0.0.0.0', port=8080, threads=1)

methodes =['POST']

if methods  POST:
    print('created succesfully')
else:
    print('false')