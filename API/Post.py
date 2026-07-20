import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "Name" : "Adarsh",
    "Age": 23,
    "Subject" : "Python"
    }

response= requests.post(url, json=data)
print(response.status_code)
print(response.json())
