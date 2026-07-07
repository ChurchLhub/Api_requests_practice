import requests



def make_put_requests(item):
    try:
        response = requests.put(url,json=item,timeout=5)
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


url = "https://jsonplaceholder.typicode.com/users/1"


email = input("Enter a new email address: ").strip()

user_email_update = {
    "email": email
}

data = make_put_requests(user_email_update)
print(f"✅ User email updated:\n{data}")


