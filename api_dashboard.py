import requests

def random_cat_fact():
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        print(f"🐱 Random Cat Fact\n------------------\n{data['fact']}")
    except requests.exceptions.ConnectionError:
        print("Connection error occurred")

    except requests.exceptions.Timeout:
        print("Request timed out")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")

    except ValueError:
        print("Error parsing JSON response")
    
def country_lookup():
    try:
        country = input("Enter a country name: ").strip()
        url = f"https://countries.dev/name/{country}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        official_name = data[0]["name"]
        capital = data[0]["capital"]
        population = data[0]["population"]
        region = data[0]["region"]
        currency_name = data[0]["currencies"][0]["name"]

        print(f"🌍 Country Information\n----------------------\nCountry   : {official_name}\nCapital   : {capital}\nPopulation: {population}\nRegion    : {region}\nCurrency  : {currency_name}")
       
    except requests.exceptions.ConnectionError:
        print("Connection error occurred")

    except requests.exceptions.Timeout:
        print("Request timed out")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")

    except ValueError:
        print("Error parsing JSON response")

def random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        print(f"😂 Random Joke\n------------------\n{data['setup']}\n{data['punchline']}")
    except requests.exceptions.ConnectionError:
        print("Connection error occurred")

    except requests.exceptions.Timeout:
        print("Request timed out")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")

    except ValueError:
        print("Error parsing JSON response")


while True:
    
    choice = (input("\n===== API DASHBOARD =====\n\n1. Random Cat Fact\n2. Country Information\n3. Random Joke\n4. Exit\n")).strip()
    if choice == "1":
        random_cat_fact()

    elif choice == "2":
        country_lookup()

    elif choice == "3":
        random_joke()

    elif choice == "4":
        print("Exiting..........\nGoodbye")
        break
    else:
        print("Invalid operation")
    