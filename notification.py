import xlutils.filter as xls
import xlwt, xlrd


class toast():

    def __init__(self):
        self.weight = 0
        self.area = "" #лучше тут конечно же что бы выбиралось из списка

    def send_to_user(self):
        pass

    def get_request(self, start, end):
        i = 0
        mas=[]
        read = xlrd.open_workbook("path")
        sheetr = read.sheet_by_index(0)
        for i in range(start, end):
            if i <=10:
                if self.weight < sheetr.cell(i,3).value or self.area == sheetr.cell(i,4).value: #пока нет таблицы заказов я рандомно указал столбцы
                    mas.append(sheetr.sheet_by_index(0).cell(i,0).value)
                    i+=1
        return mas
