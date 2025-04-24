from datetime import datetime

def save_data(result):
    with open("tempdb/AUTHORIZATION.txt", "w") as file:
        file.write(result["access_token"] + "\n")
        file.write(result["refresh_token"] + "\n")
        file.write(str(result["expiration_time"]) + "\n")
        file.write(result["client_SC"] + "\n")
        file.write(result["client_ID"] + "\n")
        file.write(str(result["id_iter"]) + "\n")
        file.write(str(result["king"]))

def load_data():
    result = {"access_token":"",
              "refresh_token":"",
              "expiration_time":datetime.today(),
              "client_ID":"",
              "client_SC":"",
              "id_iter":0,
              "king":-1}
    
    with open("tempdb/AUTHORIZATION.txt", "r") as file:
        result["access_token"] = file.readline()[:-1]
        result["refresh_token"] = file.readline()[:-1]
        result["expiration_time"] = datetime.strptime(file.readline()[:-1], "%Y-%m-%d %H:%M:%S.%f")
        result["client_SC"] = file.readline()[:-1]
        result["client_ID"] = file.readline()[:-1]
        result["id_iter"] = int(file.readline()[:-1])
        result["king"] = int(file.readline())

    return result

def generate_key():
    auth = load_data()
    auth['id_iter'] += 1
    save_data(auth)
    return auth['id_iter']