'''в головном файле не забыть обьявить import xlrd, xlwt, xlutils, os 
структура по ячейкам строк: id,name,lastName,phone,login,password'''
def registration(name,lastName,phone,login,password):
	try:
		file = open('users.xls')
	except IOError as e:
		book = xlwt.Workbook('utf8')
		sheet = book.add_sheet('sheetname')
		sheet.row(1).height = 2500
		sheet.col(0).width = 20000
		book.save('users.xls')
	else:
		with file:
			print(u'найден файл с данными об аккаунтах')
		
	file = xlrd.open_workbook('users.xls',formatting_info=True)
	sheet = rb.sheet_by_index(0)
	vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
	id_temp = 00001
	
	wb = xlwt.Workbook()
	ws = wb.add_sheet('works')
	i = 0
	for rec in vals:
		ws.write(i,0,rec[1])
		ws.write(i,1,rec[1])
		ws.write(i,2,rec[2])
		ws.write(i,3,rec[3])
		ws.write(i,4,rec[4])
		ws.write(i,5,rec[5])
		id_temp = ws.row_values(i)[0]
		i =+ i
		
	ws.write(i,0,id_temp)
	ws.write(i,1,name)
	ws.write(i,2,lastName)
	ws.write(i,3,phone)
	ws.write(i,4,login)
	ws.write(i,5,password)
	
	wb.save('users_temp.xls')
	os.replace('users_temp.xls', 'users.xls', *, None, None)
