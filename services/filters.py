import xlrd

excel_data_file = xlrd.open_workbook('order_details.xlsx')
sheet = excel_data_file.sheet_by_index(0) # обратились к 1 листу
num_of_rows = sheet.nrows # считываем число строк

## СЧИТЫВАЕМ id ИЗ ТАБЛИЦЫ
id_list = [] # массив с id

if num_of_rows > 0:
    for row in range(1, num_of_rows):
        id_list.append(str(sheet.row(row)[0]).replace("text:", "").replace("number:", "").replace(".0", "")) #обращаемся к 2 столбцу
    print("id    : ", id_list)
else:
    print("Error: not such file found or file is empty")

## СЧИТЫВАЕМ РАЗМЕРЫ ИЗ ТАБЛИЦЫ
size_list = [] # массив с размерами
if num_of_rows > 0:
    for row in range(1, num_of_rows):
        size_list.append(str(sheet.row(row)[2]).replace("text:", "").replace("number:", "").replace("'", "")) #обращаемся к 3 столбцу
    print("size  : ", size_list)
else:
    print("Error: not such file found or file is empty")


## ФИЛЬТРУЕМ РАЗМЕРЫ ПО ПАРАМЕТРАМ, ВВЕДЕННЫМ ПОЛЬЗОВАТЕЛЕМ
size_filtered = [0,0,0,0,0,0,0,0,0,0] # отобранные размеры
id_filtered_size=[]
def filter_size ( s, m, l, xl, xxl ):
    for i in range(0, len(size_list)):  # i - это просто номер элемента
        s = int(s)
        m = int(m)
        l = int(l)
        xl = int(xl)
        xxl = int(xxl)
        id_filter = i + 1

        if  s == 1 :
            if size_list[i] == 's':
                size_filtered[i] = 's'
                id_filtered_size.append(id_filter)

        if  m == 1 :
            if size_list[i] == 'm':
                size_filtered[i] = 'm'
                id_filtered_size.append(id_filter)

        if  l == 1 :
            if size_list[i] == 'l':
                size_filtered[i] = 'l'
                id_filtered_size.append(id_filter)

        if  xl == 1 :
            if size_list[i] == 'xl':
                size_filtered[i] = 'xl'
                id_filtered_size.append(id_filter)


        if  xxl == 1 :
            if size_list[i] == 'xxl':
                size_filtered[i] = 'xxl'
                id_filtered_size.append(id_filter)

    print("chosen sizes    : ", size_filtered)
    print("chosen sizes id : ", id_filtered_size) # id, подошедие по фильтру


## СЧИТЫВАЕМ ВЕС ИЗ ТАБЛИЦЫ
weight_list = [] # массив с размерами
if num_of_rows > 0:
    for row in range(1, num_of_rows):
        weight_list.append(str(sheet.row(row)[1]).replace("text:", "").replace("number:", "").replace(".0", "")) #обращаемся к 2 столбцу
    print("weight: ", weight_list)
else:
    print("Error: not such file found or file is empty")


## ФИЛЬТРУЕМ ВЕС ПО ДИАПАЗОНУ, ВВЕДЕННОМУ ПОЛЬЗОВАТЕЛЕМ
weight_filtered = [] # отобранные веса
id_filtered_weight = [] # id отобранных весов
def filter_weight ( min, max ):
    for i in range(0, len(weight_list)):  # i - это просто номер элемента
        a = int(weight_list[i])
        id_filter = i + 1

        if min < a < max:
            weight_filtered.append(a)
            id_filtered_weight.append(id_filter)
        else:
            weight_filtered.append(0)
    print("chosen weight   : ", weight_filtered)
    print("chosen weight id: ", id_filtered_weight)# id, подошедие по фильтру


## СЧИТЫВАЕМ ЦЕНУ ИЗ ТАБЛИЦЫ
price_list = [] # массив с размерами
if num_of_rows > 0:
    for row in range(1, num_of_rows):
        price_list.append(str(sheet.row(row)[3]).replace("text:", "").replace("number:", "").replace(".0", "")) #обращаемся к 4 столбцу
    print("price : ", price_list)
else:
    print("Error: not such file found or file is empty")


## ФИЛЬТРУЕМ ВЕС ПО ДИАПАЗОНУ, ВВЕДЕННОМУ ПОЛЬЗОВАТЕЛЕМ
price_filtered = [] # отобранные цены
id_filtered_price = [] # id отобранных цен
def filter_price ( min, max ):
    for i in range(0, len(price_list)):  # i - это просто номер элемента
        a = int(price_list[i])
        id_filter = i + 1

        if min < a < max:
            price_filtered.append(a)
            id_filtered_price.append(id_filter)
        else:
            price_filtered.append(0)

    print("chosen prices   : ", price_filtered)
    print("chosen prices id: ", id_filtered_price)# id, подошедие по фильтру


print("type filter_all and all sizes, weights, prices")

## ВЫВОД id ПЕРЕСЕКАЮЩИХСЯ ПО ВСЕМ ФИЛЬТРАМ ЗАКАЗОВ
def filter_all( sz_s, sz_m, sz_l, sz_xl, sz_xxl, min_wght, max_wght, min_pr, max_pr ):
    filter_size(sz_s, sz_m, sz_l, sz_xl, sz_xxl)
    filter_weight(min_wght, max_wght)
    filter_price(min_pr, max_pr)
    result = list(set(id_filtered_size) & set(id_filtered_weight))
    print(result)
    id_all = list(set(result) & set(id_filtered_price))
    print("all filters together id: ", id_all)



