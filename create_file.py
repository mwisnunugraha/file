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

app = Flask(__name__)

@app.route('/create_file', methods=['POST'])
def create_file():
    data = request.form['data']

    if data:
        # Menulis data ke file
        with open('file.txt', 'w') as f:
            f.write(data)
        return 'File created successfully'
    else:
        return 'Data not provided'

if __name__ == '__main__':
    app.run(debug=True)
