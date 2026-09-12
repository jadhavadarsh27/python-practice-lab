import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "Name": "Adarsh",
    "Age": 24,
    "Job_Role": "DevOps"
    }

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
