import requests

# basic level url
BASE = "http://127.0.0.1:5000/"

# making GET requests
response = requests.get(BASE + "helloworld/Mahmoud").json()
print(response)

# # Making post requests for security
# response = requests.post(BASE + "helloworld") 
# print(response.json()['data'])