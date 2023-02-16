from flask import Flask, request, json
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return {"Status": True, "Nama": "belajar_json"}

#buat buka file json
file_json = open("data_sekolah.json")

# prsing data json
data =  json.loads(file_json.read())


@app.route('/data_sekolah.json')
def tampilkan_json():
    return 'data_sekolah.json'

if __name__ == '__main__':
    app.run(debug=True)
    serve(app, host='0.0.0.0', port=8080, threads=1)