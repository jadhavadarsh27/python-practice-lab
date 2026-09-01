import requests

#creating data

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "Name" : "adarsh",
    "Age" : 23,
    "Job Role" : "DevOps Engineer",
    "Package" : "45 LPA"
    }
response_post = requests.post(url, json = data)
print(response_post.status_code)
print(response_post.json())

#Fetching data

response_get = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response_get.status_code == 200:
    data2 = response_get.json()
    print(data2)
else:
    print("API failed...")
