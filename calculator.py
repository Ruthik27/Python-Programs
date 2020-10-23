from tkinter import *

def perform(op):
    pass

w1 = Tk()
w1.title('My App')

l1 = Label(w1, text = 'Number-1')
n1 = StringVar()
e1 = Entry(w1, textvariable = n1, justify = 'center')
e1.focus()

l2 = Label(w1, text = 'Number-2')
n2 = StringVar()
e2 = Entry(w1, textvariable = n2, justify = 'center')

l3 = Label(w1, text = 'Result')
n3 = StringVar()
e3 = Entry(w1, textvariable = n3, justify = 'center', state = 'disabled')

b1 = Button(w1,  text = 'ADD' , command = lambda: perform('add'))
b2 = Button(w1,  text = 'SUB' , command = lambda: perform('SUB'))
b3 = Button(w1,  text = 'MUL' , command = lambda: perform('mul'))
b4 = Button(w1,  text = 'DIV' , command = lambda: perform('div'))

l1.grid(row = 0, column = 0)
e1.grid(row = 0, column = 1)
l2.grid(row = 1, column = 0)
e2.grid(row = 1, column = 1)
l3.grid(row = 2, column = 0)
e3.grid(row = 2, column = 1)

b1.grid(row = 3, column = 0)
b2.grid(row = 3, column = 1)
b3.grid(row = 4, column = 0)
b4.grid(row = 4, column = 1)

w1.mainloop()
