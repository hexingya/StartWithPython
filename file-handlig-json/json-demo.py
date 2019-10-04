# json object

# json object (key -> "keyname", value -> jsonobject|array|string|number|true|false|null)

import json

json_object = '{"name": "John Doe", "phone": 98994545, "status": true, "values": [45, 5, 453, 3], "balance": null}'

print(json_object)

# to convert json object inot python object (dict)
py_object = json.loads(json_object)  # dict
print(py_object)
# print(py_object["balance"])

# print(json.loads('["one", "Two", 1, 2]'))
# print(json.loads('null'))

# python object (dict) into json object

person = {"name": "Rozer", "address": "21A Mohali", "balance": 3443434.34,
          "isSingle": True, "friends": ['Mike', 'Brian', 'Joy', 'Amol']}

print(type(person))  # dict

json_obj = json.dumps(person)

print(type(json_obj))  # str
print(json_obj)
