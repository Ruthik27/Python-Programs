import pymysql
from tkinter import *
from tkinter import messagebox

def clear():
    rollno.set('')
    name.set('')
    age.set('')

def save():
    try:
        con = pymysql.connect(user = 'root', password = '8500', host ='localhost',database ='db1')
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
        con = pymysql.connect(user = 'root', password = '8500', host ='localhost',database ='db1')
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

w1=Tk()
w1.title('My App')
w1.geometry('500x300')

rollno = StringVar()
name=StringVar()
age=StringVar()

l1=Label(w1, text ='RollNo ' )
e1=Entry(w1, textvariable = rollno)
l2=Label(w1, text ='Name ' )
e2=Entry(w1, textvariable = name)
l3=Label(w1, text ='Age ' )
e3=Entry(w1, textvariable = age)

b1=Button(w1, text = 'Save', command =save)
b2=Button(w1, text = 'DispalyAll', command = displayall)
b3=Button(w1, text = 'Clear', command = clear)

l1.grid(row=1, column = 0)
e1.grid(row =1, column = 1)
l2.grid(row=2, column = 0)
e2.grid(row =2, column = 1)
l3.grid(row=3, column = 0)
e3.grid(row =3, column = 1)

b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=1, column=2)

w1.mainloop()
