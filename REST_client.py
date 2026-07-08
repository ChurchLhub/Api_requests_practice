import requests

def send_request(request_function, url, **kwargs):
    try:
        response = request_function(url, timeout=5, **kwargs)
        response.raise_for_status()
        return response
    except requests.exceptions.ConnectionError:
        print("Connection error occurred")

    except requests.exceptions.Timeout:
        print("Request timed out")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")

    except ValueError:
        print("Error parsing JSON response") 


def get_data():
    return send_request(requests.get, 
    "https://httpbin.org/get")


def send_data(item):
    return send_request(requests.post, 
    "https://httpbin.org/post", json=item)




def update_data(item):
    return send_request(requests.put,
     "https://httpbin.org/put", json=item)



def delete_data():
    return send_request(requests.delete, 
    "https://httpbin.org/delete")


def display_response(response):
    if response is not None:
        print(f"✅ Response:\n{response.json()}")
        print(f"✅ Status code: {response.status_code}")
    else:
        print("No response received.")

# response = requests.get("https://httpbin.org/get")
# response.raise_for_status()
# data = response.json()
# print(data)

def show_menu():
        return (input("\n====== REST CLIENT ======\nChoose an option:\n1. Retrieve Data (GET)\n2. Create Data (POST)\n3. Update Data (PUT)\n4. Delete Data (DELETE)\n5. Exit\n"))



while True:
    choice = show_menu()

    if choice == "1":
        data = get_data()
        display_response(data)


    elif choice == "2":
        title = input("Enter title: ")

        item = {
            "title" : title
        }
        data = send_data(item)
        display_response(data)


    elif choice == "3":
        email = input("Enter a new email address: ").strip()

        user_email_update = {
            "email": email
        }

        data = update_data(user_email_update)
        display_response(data)
        


    elif choice == "4":
        data = delete_data()
        display_response(data)


    elif choice == "5":
        print("Exiting the REST client.")
        break


    else:
        print("Invalid choice. Please try again.")


