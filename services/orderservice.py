from models.order import Order
import json
import os


class OrderService:
    lastOrderId = 0

    def createNewOrder(self, weight, size, loginCostumer, loginExecutor, price,
                       adressPickup, adressDelivery, timePickup, timeDelivery, description):
        self.lastOrderId += 1
        order = Order(self.lastOrderId, weight, size, loginCostumer, loginExecutor, price, "created",
                      adressPickup, adressDelivery, timePickup, timeDelivery, description)
        jsonString = json.dumps(order)
        with open("Order" + str(order.id) + ".txt", "w") as text_file:
            text_file.write(jsonString)
        return order

    def getOrderById(self, orderId):
        with open("Order" + str(orderId) + ".txt", "r") as text_file:
            jsonString = text_file.read()
        return json.loads(jsonString)

    def saveOrder(self, orderId, order):
        jsonString = json.dumps(order)
        with open("Order" + str(orderId) + ".txt", "w") as text_file:
            text_file.write(jsonString)

    def getOrderStatusById(self, orderId):
        order = self.getOrderById(orderId)
        return order.status

    def deleteOrder(self, orderId):
        with open("Order" + str(orderId) + ".txt", "w") as text_file:
            os.remove(os.path.abspath(text_file.name))

    def dissmissOrderById(self, orderId):
        order = self.getOrderById(orderId)
        order.status = "dissmiss"
        self.saveOrder(self, orderId, order)