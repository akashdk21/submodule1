import requests
import json

def switch():
    choice=int(input("choose Action\n1.Create\n2.Read\n3.update\n4.delete\n5.exit\n"))
    list1={1:create1,2:read1,3:update1,4:delete1,5:exit1}
    list1[choice]()

        
def create1():
    headers = {"Authorization": "Bearer sl.A_hdsvrhs6_7L_rNPJBJa6F8gybrWbBMvdrTFXadg6zh7UdAOUtbH8G8btBLStZ1iHRisqTvyoZ_qFHTkfP0xuoonBVaxSTOnDRA8STnpMd3L16TOfVAtyjWO0af2XgXlHqzQEjrKCLW" ,
           "Content-Type": "application/json" 
           }
    r = requests.post(
        "https://api.dropboxapi.com/2/file_requests/create",
        headers=headers,
        data="{\"title\": \"Homework submission\",\"destination\": \"/Home/Akash\",\"open\": true}"
        )
    print(r.json().get("url"))

    
def read1():
    headers = {"Authorization": "Bearer sl.A_BLmwgbC7pbSgQfC8_3hdM_7fDAcEwgkCeiKf2AmzQlBPwEQCQ2I8CFpYYRpDR4HQxBGdAEkjDcUXrjS4MruUlAJk8pAYF6C5NliUNu85lhCWZnkOlN-ysH4xbQlZv86GRtSYkhEEQh" ,
           "Dropbox-API-Arg": "{\"path\": \"/Home/Akash/File1.txt\"}"
               }
    r = requests.post(
        "https://content.dropboxapi.com/2/files/download",
        headers=headers
        )
    return r.text
    
    
def update1():
    res=read1()
    file1=open("File1.txt","w")
    content=res+"File is updated\n"
    file1.write(content)
    file1.close()
    headers = {"Authorization": "Bearer sl.A_BLmwgbC7pbSgQfC8_3hdM_7fDAcEwgkCeiKf2AmzQlBPwEQCQ2I8CFpYYRpDR4HQxBGdAEkjDcUXrjS4MruUlAJk8pAYF6C5NliUNu85lhCWZnkOlN-ysH4xbQlZv86GRtSYkhEEQh" ,
           "Dropbox-API-Arg": "{\"path\": \"/Home/Akash/File1.txt\",\"mode\": \"overwrite\",\"autorename\": true,\"mute\": false,\"strict_conflict\": false}" ,
           "Content-Type": "application/octet-stream" \
               }
    files = {
        'file': open("C:/Users/akash_kurund/Documents/Dropbox crud/File1.txt", "rb")
        }
    r = requests.post(
        "https://content.dropboxapi.com/2/files/upload",
        headers=headers,
        files=files
        )
    print(r.text)

    
def delete1():
    headers = {"Authorization": "Bearer sl.A_BLmwgbC7pbSgQfC8_3hdM_7fDAcEwgkCeiKf2AmzQlBPwEQCQ2I8CFpYYRpDR4HQxBGdAEkjDcUXrjS4MruUlAJk8pAYF6C5NliUNu85lhCWZnkOlN-ysH4xbQlZv86GRtSYkhEEQh" ,
               "Content-Type": "application/json"
               }
    r = requests.post(
        "https://api.dropboxapi.com/2/files/delete_v2",
        headers=headers,
        data="{\"path\": \"/Home/Akash/keys.txt\"}"
        )
    print(r.text)
    
def exit1():
    exit()
    
if __name__=="__main__":
    while(True):
        switch()
    


