import requests

def make_delete_requests():
    try:
        response = requests.delete(url,  timeout=5)
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.ConnectionError:
        print("Connection error occurred")

    except requests.exceptions.Timeout:
        print("Request timed out")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")

    except ValueError:
        print("Error parsing JSON response")   

url = "https://jsonplaceholder.typicode.com/todos/1"


data = make_delete_requests()
print(f"✅ Todo deleted:\n{data}")

