import requests

MY_LATITUDE = 53.865467
MY_LONGITUDE = 10.686559

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
}

url = "https://api.sunrise-sunset.org/json"
response = requests.get(url, params = parameters)
response.raise_for_status()
data = response.json()

sunrise = data ["results"] ["sunrise"]
sunset = data ["results"] ["sunset"]

print(f"Sunrise time is :", {sunrise})
print(f"Sunset time is :", {sunset})