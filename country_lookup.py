import requests
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