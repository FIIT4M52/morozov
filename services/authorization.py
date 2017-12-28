import json, os

def authorization(login, password):
    with open('Person.txt','r') as text_file:
        data=json.load(text_file)
    datalog = [0 for i in range(len(data))]
    datapass = datalog
    i = 0
    autstatus = 1
    for i in range(len(data)):
        datalog[i] = data[i][4]
        datapass[i] = data[i][5]
    i = 0
    while i < len(datalog):
        if datalog[i] == login and datapass[i] == password:
            break
            return autstatus == 1
        i = i + 1
    else:
        return autstatus == 0
