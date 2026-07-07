import requests

def make_post_requests(item):
    try:
        response = requests.post(url,json=item,timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("Connection error occurred")

    except requests.exceptions.Timeout:
        print("Request timed out")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")

    except ValueError:
        print("Error parsing JSON response")   


url = "https://jsonplaceholder.typicode.com/todos"

todo = input ("Enter a new todo item: ").strip()



todo_item = {
    "title": todo,
}

data =make_post_requests(todo_item)
print(f"✅ New todo item created:\n{data}")

