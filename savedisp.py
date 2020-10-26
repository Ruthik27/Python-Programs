import pymysql
from tkinder import *
from tkinder import messagebox

def clear():
    rollno.set('')
    name.set('')
    age.set('')

def save():
    try:
        con = pymysql.connect(user = 'root', password = '8500', hoast ='localhost',database ='db1')
        cur = con.cursor()
        sql = "insert into student values ('%s', '%s', '%s')" %(rollno.get(),name.get(), age.get())
        cur.execute(sql)
        con.commit()
        messagebox.showinfo('Success','Record Saved...')

    except:
        messagebox.showinfo('Error','Error in data entry...')
    finally:
        clear()

def displayall():
    try:
        con = pymysql.connect(user = 'root', password = '8500', hoast ='localhost',database ='db1')
        cur = con.cursor()
        sql = 'select * from student'
        cur.execute(sql)
        result = cur.fetchall()

        f =open('details.txt','w')
        for data in result:
            f.write(str(data)+'\n')
        f.close()
        con.close()

        import subprocess as sp
        pName='notepad.exe'
        fName='details.txt'
        sp.Popen([pName,fName])

    except:
        messagebox.showinfo('No Data','No such data available...' )
