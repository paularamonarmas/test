import requests
endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = { "q" : "London,UK" , "units" : "metric" , "appid" : "f3f22ff0914d7726acb8527b6786f5c4" }
response = requests.get(endpoint, params = payload)
data = response.json()
print (data 'main')
print (response.url)
print (response.status_code)
print (response.headers[ "content-type" ])
print (response.text)
