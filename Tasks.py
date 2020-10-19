import pymsql   #for database
from tkinter import *    # for cursor
from tkinter import messagebox  # same for window operation

def search():
    try:
        con = pymsql.connect(user='root', password='', host='localhost', database='db')  #connection
        cur = con.cursor()    #same
        sql = "select * from student where Rollno='%s'"%Rollno.get()   #querry tht should be performed
        cur.execute(sql)     #execution
        result = cur.fetchone()   #getting one value
        name.set(result[1])
        age.set(result[2])
        e1.configure(state = 'disabled')
        con.close()
    except:
        messagebox.showinfo('No Data','No such data available')
        clear()

def clear():   # to clear values
    Rollno.set('') #setting to null
    name.set('')
    age.set('')
    e1.configure(state='normal')

def add():  # using the same just changing querry and messagebox info
    try:
        con = pymsql.connect(user='root', password='', host='localhost', database='db')
        cur = con.cursor()
        sql = "insert into student values('%s','%s','%s')" %(Rollno.get(),name.get(),age.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Success','Rrcord saved...')
    except:
        messagebox.showinfo('Error','Error in data entry...')

def update(): # using the same just changing querry and messagebox info
    try:
        con = pymsql.connect(user='root', password='', host='localhost', database='db')
        cur = con.cursor()
        sql = "update student set name = '%s', age = '%s' where Rollno = '%s'" %(name.get(), age.get(), Rollno.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Success','Rrcord updated...')
    except:
        messagebox.showinfo('Error','Error occured...')

def delete(): # using the same just changing querry and messagebox info
    try:
        con = pymsql.connect(user='root', password='', host='localhost', database='db')
        cur = con.cursor()
        sql = "delete from student where Rollno = '%s'" %(Rollno.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Success','Rrcord deleted...')
    except:
        messagebox.showinfo('Error','Error occured...')



# FOR GUI
w1 = Tk()
w1.title('My App')
w1.geometry('500*200')
ptitle = lable(w1, text '''Program to add , delete & modify records from the student table''')
ptitle.grid(row = 0 , column = 0, columnspace =2 )

Rollno = StringVar()
name = StringVar()
age = StringVar()

l1 = lable (w1 , text = 'RollNo')
e1 = Entry(w1 , text variable = Rollno)
l2 = lable (w1 , text = 'Name')
e2 = Entry(w1 , text variable = name )
l3 = lable (w1 , text = 'Age')
e3 = Entry(w1 , text variable = age )

b1 = Button (w1, text = 'Search', command = Search)
b2 = Button (w1, text = 'Add', command = add)
b3 = Button (w1, text = 'Update', command = update)
b4 = Button (w1, text = 'Delete', command = delete)
b5 = Button (w1, text = 'Clear', command = clear)

l1.grid(row =1 , column =0)
c1.grid(row =1, column =1)
b1.grid(row =1, column =2)

l2.grid(row =2 , column =0)
c2.grid(row =2, column =1)
l3.grid(row =3 , column =0)
c3.grid(row =3, column =1)

b2.grid(row =4, column =0)
b3.grid(row =4, column =1)
b4.grid(row =5, column =0)
b5.grid(row =5, column =1)

w1.mainloop()
