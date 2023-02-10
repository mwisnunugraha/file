from flask import Flask 
import json

x ={"sekolah1": "smk","name": "wisnu",
"sekolah2": "sma","name": "aldo"}

y = json.dumps(x, indent=4, sort_keys=True)

print(y)