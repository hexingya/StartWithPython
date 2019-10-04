import json

try:
    fd = open("record.json", "r")
    data = fd.read()  # json data ~ txt
    fd.close()

    py_data = json.loads(data)
    py_data["isOkay"] = True

    fd = open("record.json", "w")
    fd.write(json.dumps(py_data))
    fd.close()
except Exception as e:
    print("Error!", e)
