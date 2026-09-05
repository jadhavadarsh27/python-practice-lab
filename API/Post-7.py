import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "Name" : "Adarsh",
    "Age" : 24,
    "Mobile" : 9988776655
    }

response = requests.post(url, json = data)
print(response.status_code)
print(response.json())
