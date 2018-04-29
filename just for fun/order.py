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