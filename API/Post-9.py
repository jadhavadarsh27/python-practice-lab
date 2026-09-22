import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "Name" : "Adarsh",
    "Age" : 24,
    "Role" : "DevOps Engineer"
    }

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
