import requests
import json

headers = {"Authorization": "Bearer sl.A_C54ueKEuuzP-gJCxKiRInW5RlrAuMUp_7CVubYQwATsXm0roK6SEoIlzO9EOmI62It2onvUi1Vt1zhTx85k019ZtLfEBc8xPxEwZlvgSnFMlN2DBjWKdbaUq-dPH5D5YeOUrTtu_88" ,
           "Content-Type": "application/json" 
           }
r = requests.post(
    "https://api.dropboxapi.com/2/file_requests/update",
    headers=headers,
    data="{\"id\": \"DD4Z7i8L7uFMmONQNDBO\",\"title\": \"Homework submission\",\"destination\": \"/Home/NewAkash\",\"open\": true}"
)
print(r.json().get("url"))


