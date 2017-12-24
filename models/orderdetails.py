#import your classes and libs

from datetime import datetime

class orderDetails():
    def __init__(self):
        self.adressPickup = ""
        self.adressDelivery = ""
        self.timePickup= datetime.now()
        self.timeDelivery = datetime.now()
        self.description = ""

