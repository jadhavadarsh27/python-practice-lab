import requests

response1 = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response1.status_code == 200:
    data = response1.json()
    print(data)
else:
    print("API failed" )



url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "Name" : "Adarsh",
    "Age" : 24,
    "Role" : "DevOps Engineer"
    }

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
