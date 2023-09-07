import requests
from datetime import datetime

pixela_endpoints = "https://pixe.la/v1/users"

TOKEN = "hviseuhirhe38y3ihi3hk"
USERNAME = "adityasaxena"
GRAPH_ID = "graph1"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}




graph_endpoint = f"{pixela_endpoints}/{USERNAME}/graphs"

graph_parameters = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


today = datetime.now()

post_pixela_endpoints = f"{pixela_endpoints}/{USERNAME}/graphs/{GRAPH_ID}"

post_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours you have studied today?")
}

response = requests.post(url=post_pixela_endpoints, json=post_parameters, headers=headers)
print(response.text)

url =f"{pixela_endpoints}/{USERNAME}/graphs/{GRAPH_ID}/20230720"
put_endpoints={
    "quantity":"10.0"
}




