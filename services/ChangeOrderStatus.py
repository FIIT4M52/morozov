from services.orderservise import OrderService
from xlrd import open_workbook
import json
import os
import xlrd, xlwt

def ChangeOrderStatus(orderId, status):
	order = getOrderById(orderId)
	order.status = status
	saveOrder(orderId, order)


	rb = open_workbook('../xls/orders.xls')
	sheet = rb.sheet_by_index(0)
	value = orderId
	for ii in range(sheet.nrows):
		data = sheet.cell_value(ii, 0)
		if int(value) == int(data):
			sheet.ceil(row=li, column=6).value = json.dumps	({'status':order.status})

