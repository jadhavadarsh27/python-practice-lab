import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "Name" : "Adarsh",
    "Designation" : "DevOps Engineer",
    "Salary" : "25 LPA"
    }

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
