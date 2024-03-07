import requests
from datetime import datetime
USER_NAME = "phucle96"
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "qwertyuahsnxmzb1918aj"
GRAPH_ID = "graph1"
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Books",
    "unit": "Page",
    "type": "int",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
# today = datetime.now()
# pixel_config = {
#     "quantity": input("How many kms did you run today?: "),
#     "date": today.strftime("%Y%m%d"),
# }
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

put_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/20230414"
put_data = {
    "quantity": "120.4",
}
put_response = requests.put(url=put_pixel_endpoint, json=put_data, headers=headers)
print(put_response.text)
# delete_response = requests.delete(url=f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/20230402", headers=headers)
# print(delete_response.text)
# delete_response = requests.delete(url=f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/20230405", headers=headers)
# print(delete_response.text)
