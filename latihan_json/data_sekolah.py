from flask import Flask, jsonify
from waitress import serve
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return {"Status": True, "Nama": "belajar_json"}

#buat buka file json
file_json = open("data_sekolah.json")

# prsing data json
data =  json.loads(file_json.read())


@app.route('/data_sekolah', methods=["GET"])
def tampilkan_json():
    with open ("data_sekolah.json") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
    serve(app, host='0.0.0.0', port=8080, threads=1)