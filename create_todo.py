import requests

url = "https://jsonplaceholder.typicode.com/todos"

todo = input ("Enter a new todo item: ").strip()



todo_item = {
    "title": todo,
}

response = requests.post(url, json=todo_item)
code = response.status_code
data = response.json()
print(data)





