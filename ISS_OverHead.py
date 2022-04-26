import requests
import datetime as dt

# Fix the code below with your latitude and longitude
MY_LAT = 40.760780 # Your latitude
MY_LONG = -111.891045 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
# print(iss_latitude)
iss_longitude = float(data["iss_position"]["longitude"])
# print(iss_longitude)
iss_position = (iss_latitude,iss_longitude)

print(f"the ISS position is currently {iss_position} ")



parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

#figuring out when its dark using the datetime module
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
# print(sunrise)
# print(sunset)

now = dt.datetime.now()
now_hour = now.hour
# print(now_hour)

#If the ISS is close to my current position and it is currently dark
if MY_LAT - 2  <= iss_latitude <= MY_LAT  + 2 and MY_LONG - 2 <= iss_longitude <= MY_LONG + 2 and now_hour > 20 and now_hour < 6:
    print("this works, and go outside to look for the ISS")
else:
    print("this didn't work, or the ISS is not nearby. please wait")

#TODO Setup email or sms updates to the enduser.
