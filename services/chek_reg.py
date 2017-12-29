import random as rand
import string
import json

class chek_email():
    rand.seed()

    def __init__(self):
        #self.sum = int(rand.uniform(10000000,99999999))
        self.token = ''.join(rand.choice(string.ascii_lowercase + string.digits) for x in range(16))

    def send_key(self): #print key to user and user then write this key in def chek_control
        print(self.token)

    def chek_control(self, key, json_obj):
        parsed_string = json.loads(json_obj)
        if key == self.token:
            parsed_string['check'] = True
        else:
            parsed_string['check'] = False
        obj_js = json.dump(parsed_string)
        return obj_js #return json object to user
