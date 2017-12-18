'''в головном файле не забыть обьявить import xlrd, xlutils'''
def authorization(login, password):
    rb = xlrd.open_workbook('users.xls', formatting_info=True)
    sheet = rb.sheet_by_index(0)
    i = 0
    autstatus = 1
    datalog = [0, 0, 0, 0, 0, 0]
    datapass = [0, 0, 0, 0, 0, 0]
    row = sheet.nrows
    print(row)
    print(datapass, datalog)
    print(login, password)
    while i < row:
        datalog[i] = sheet.cell_value(i, 3)
        datapass[i] = sheet.cell_value(i, 4)
        print(i)
        i = i + 1
    print(datapass, datalog)
    i = 0
    while i < row:
        if datalog[i] == login and datapass[i] == password:
            break
            return autstatus == 1
        i = i + 1
    else:
        return autstatus == 0
