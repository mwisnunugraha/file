from flask import Flask 
import json

#buat buka file json
file_json = open("data_sekolah.json")

# prsing data json
data =  json.loads(file_json.read())

# menampilkan isi data json
print(data)