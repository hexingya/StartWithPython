import requests
import json

remote_data = requests.get("https://jsonplaceholder.typicode.com/todos")

# print(type(remote_data.text))

todos = json.loads(remote_data.text)  # list

# print(todos[:10])

for todo in todos[:10]:
    print(todo.get("id"))
    print(todo.get("title"))
    print(todo.get("completed"))
