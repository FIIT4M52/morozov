from services.orderservise import OrderService
import json
import os

def ChangeOrderStatus(orderId, status):
	order = getOrderById(orderId)
	order.status = status
	saveOrder(orderId, order)
