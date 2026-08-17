import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "Name" : "Adarsh",
    "Subject" : "Cloud",
    }

response = requests.post(url, json= data)
print(response.status_code)
print(response.json())
