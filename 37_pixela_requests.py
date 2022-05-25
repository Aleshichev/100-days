import requests

data_pixel = "https://pixe.la/@igorok "        # создали имя пользователя

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token" : "9i8u7y6t5r",
    "username" : "igorok",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)