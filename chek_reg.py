import random as rand
import string
from xlutils.copy import copy
import xlwt, xlrd

class chek_email():
    rand.seed()

    def __init__(self):
        #self.sum = int(rand.uniform(10000000,99999999))
        self.token = ''.join(rand.choice(string.ascii_lowercase + string.digits) for x in range(16))
    #send to user and chek_control

    def send_key(self):
        print(self.token)

    def chek_control(self, key, id):
        global control_sum
        if key == self.sum:
            read = xlrd.open_workbook("path")
            sheetr = read.sheet_by_index(0)
            wb_dst = copy(sheetr)
            ws_dst = wb_dst.get_sheet(0)
            for i in range(0,sheetr.ncols):
                if sheetr.cell(i,0).value == id:
                    ws_dst.write(i, 6, 'true')
                else:
                    ws_dst.write(i, 6, 'false')
        wb_dst.save("path")
