from datetime import datetime

def save_data(result):
    with open("tempdb/AUTHORIZATION.txt", "w") as file:
        file.write(result["access_token"] + "\n")
        file.write(result["refresh_token"] + "\n")
        file.write(result["expiration_time"])
    with open("tempdb/CLIENT_ID.txt", "w") as file:
        file.write(result["client_ID"])
    with open("tempdb/CLIENT_SC.txt", "w") as file:
        file.write(result["client_SC"])

def load_data():
    result = {"access_token":"",
              "refresh_token":"",
              "expiration_time":datetime.today(),
              "client_ID":"",
              "client_SC":""}
    
    with open("tempdb/AUTHORIZATION.txt", "r") as file:
        result["access_token"] = file.readline()[:-1]
        result["refresh_token"] = file.readline()[:-1]
        result["expiration_time"] = datetime.strptime(file.readline(), "%Y-%m-%d %H:%M:%S.%f")
    with open("tempdb/CLIENT_ID.txt", "r") as file:
        result["client_ID"] = file.readline()
    with open("tempdb/CLIENT_SC.txt", "r") as file:
        result["client_SC"] = file.readline()

    return result