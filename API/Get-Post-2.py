import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("API failed...")


url = "https://jsonplaceholder.typicode.com/posts"

data2 = {
    "Name" : "Adarsh",
    "Age" : 23
    }

response2 = requests.post(url, json=data2)
print(response2.status_code)
print(response2.json())
