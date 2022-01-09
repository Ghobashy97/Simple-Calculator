from tkinter import *

root = Tk()
root.title("Simple Calculator")


#..............................Display box..............................................

entry1 = Entry(root, width=35, borderwidth= 5)
entry1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)





#.................................Buttons.........................................   

def buttonClick(number):
    current = entry1.get()
    entry1.delete(0, END)
    entry1.insert(0, str(current) + str(number))


def buttonClear():
    entry1.delete(0,END)


def buttonAdd():
    first_number = entry1.get()
    global f_num 
    global math
    math = "Addition" 
    f_num = int(first_number)
    entry1.delete(0, END)



def buttonSub():
    first_number = entry1.get()
    global f_num 
    global math
    math = "Subtraction" 
    f_num = int(first_number)
    entry1.delete(0, END)

def buttonMul():
    first_number = entry1.get()
    global f_num 
    global math
    math = "Multiplication" 
    f_num = int(first_number)
    entry1.delete(0, END)

def buttonDiv():
    first_number = entry1.get()
    global f_num 
    global math
    math = "Division" 
    f_num = int(first_number)
    entry1.delete(0, END)


def buttonEqual():
    second_number = entry1.get()
    entry1.delete(0, END)
    if math == "Addition":
        entry1.insert(0, f_num + int(second_number))
    elif math== "Subtraction":
        entry1.insert(0, f_num - int(second_number))
    elif math== "Multiplication":
        entry1.insert(0, f_num * int(second_number))
    elif math== "Division":
        entry1.insert(0, f_num / int(second_number))





button_1 = Button(root, text="1", padx=40, pady=20, command = lambda:buttonClick(1))
button_2 = Button(root, text="2", padx=40, pady=20, command = lambda:buttonClick(2))
button_3 = Button(root, text="3", padx=40, pady=20, command = lambda:buttonClick(3))

button_4 = Button(root, text="4", padx=40, pady=20, command = lambda:buttonClick(4))
button_5 = Button(root, text="5", padx=40, pady=20, command = lambda:buttonClick(5))
button_6 = Button(root, text="6", padx=40, pady=20, command = lambda:buttonClick(6))

button_7 = Button(root, text="7", padx=40, pady=20, command = lambda:buttonClick(7))
button_8 = Button(root, text="8", padx=40, pady=20, command = lambda:buttonClick(8))
button_9 = Button(root, text="9", padx=40, pady=20, command = lambda:buttonClick(9))
button_0 = Button(root, text="0", padx=40, pady=20, command = lambda:buttonClick(0))

button_add = Button(root, text="+", padx=39, pady=20, command = buttonAdd)

button_sub = Button(root, text="-", padx=40, pady=20, command = buttonSub)
button_mul = Button(root, text="*", padx=40, pady=20, command = buttonMul)
button_div = Button(root, text="/", padx=40, pady=20, command = buttonDiv)

button_eq = Button(root, text="=", padx=90, pady=20, command = buttonEqual)
button_clr = Button(root, text="Clear", padx=79, pady=20, command = buttonClear)



button_1.grid(row=3, column =0 )
button_2.grid(row=3, column =1 )
button_3.grid(row=3, column =2 )

button_4.grid(row=2, column =0 )
button_5.grid(row=2, column =1 )
button_6.grid(row=2, column =2 )

button_7.grid(row=1, column =0 )
button_8.grid(row=1, column =1 )
button_9.grid(row=1, column =2 )

button_0.grid(row=4, column =0 )
button_clr.grid(row=4, column =1, columnspan=2)
button_add.grid(row=5, column =0 )
button_eq.grid(row=5, column =1, columnspan=2)

button_sub.grid(row = 6, column=0)
button_mul.grid(row = 6, column=1)
button_div.grid(row = 6, column=2)




root.mainloop()