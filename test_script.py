import requests

url = "https://catfact.ninja/fact"
try:
    response = requests.get(url,timeout=5)
    response.raise_for_status()
    data = response.json()
    print(data["fact"])
except requests.exceptions.ConnectionError:
    print("Connection error occurred")

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error: {http_err}")

except ValueError:
    print("Error parsing JSON response")    