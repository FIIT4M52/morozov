from datetime import datetime


class Order:
    id = 0
    weight = 0
    size = 0
    loginCostumer = ""
    loginExecutor = ""
    price = 0
    status = ""
    addressPickup = ""
    addressDelivery = ""
    timePickup = datetime.now()
    timeDelivery = datetime.now()
    description = ""
    rejectionReason = ""

    def __init__(self, id, weight, size, loginCostumer, loginExecutor, price, status,
                 adressPickup, adressDelivery, timePickup, timeDelivery, description):
        self.id = id
        self.weight = weight
        self.size = size
        self.loginCostumer = loginCostumer
        self.loginExecutor = loginExecutor
        self.price = price
        self.status = status
        self.addressPickup = adressPickup
        self.addressDelivery = adressDelivery
        self.timePickup = timePickup
        self.timeDelivery = timeDelivery
        self.description = description
        self.rejectionReason = ""

    def setWeight(self, weight):
        self.weight = weight

    def setSize(self, size):
        self.size = size

    def setLoginCostumer(self, loginCostumer):
        self.loginCostumer = loginCostumer

    def setLoginExecutor(self, loginExecutor):
        self.loginExecutor = loginExecutor

    def setPrice(self, price):
        self.price = price

    def setStatus(self, status):
        self.status = status

    def setAddressPickup(self, addressPickup):
        self.addressPickup = addressPickup

    def setAddressDelivery(self, addressDelivery):
        self.addressDelivery = addressDelivery

    def setTimePickup(self, timePickup):
        self.timePickup = timePickup

    def setTimeDelivery(self, timeDelivery):
        self.timeDelivery = timeDelivery

    def setDescription(self, description):
        self.description = description

    def setRejectionReason(self, rejectionReason):
        self.rejectionReason = rejectionReason
