import sqlite3
from funny import filling

def append(data,delit):
    conn = sqlite3.connect('mydb.db', isolation_level=None)
    cursor = conn.cursor()
    if(delit == True):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM person")
        cursor.execute("VACUUM")
        cursor.close()
    else:
        cursor.executemany('INSERT INTO person VALUES (?,?,?,?,?,?,?)',data)
        conn.commit()

data = filling()
append(data,0) #params: data - данные для заполнения(массив), delit - если в значении True, то после записи всё удаляется
