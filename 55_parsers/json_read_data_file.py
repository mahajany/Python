import json
from pprint import pprint
INPUT_FILE='data_file.json'
data = json.load(open(INPUT_FILE))

print("---------------------------pprint(data)")
pprint(data)

print("===========================print(data)")
print(data)
print(data["maps"][0]["id"])
print(data["masks"]["id"])
print(data["om_points"])
print(data["parameters"]["id"])
