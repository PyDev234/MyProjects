# Gui Calculator in Python using Tkinter
from tkinter import *

# global variable exp stores the given by user 
exp = ""
 
# update the expression
def press(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)
 
 
def evaluate():
    # in case any error occurs
    try:
        global exp
        op = str(eval(exp))
        equation.set(op)
        exp = ""
 
    except:
        equation.set(" error ")
        exp = ""
 
 
# To clear the expression
def clear():
    global exp
    exp = ""
    equation.set("")
 

if __name__ == "__main__":
    # Tk method for Gui window
    window = Tk()
 
    # setting the background color 
    window.configure(background="#415d73")
 
    # to set the title of the window
    window.title("PyCalculator")
 
    # set the Geometry of Gui window
    window.geometry("400x250")
 
    # Python String can't be change after assigning so we will use the tkinter stringvar class to manipulate the user input
    equation = StringVar()
 
    # expression will contain the expression
    expression = Entry(window, textvariable=equation, bg="#b7d5ed")
 
    # For placing in a table like structure grid method is used
    expression.grid(columnspan=4, ipadx=138, ipady=10)
 
    # create a Buttons in the root window
    # command will call the function given in command when that button is pressed
    button1 = Button(window, text=' 1 ', fg='black', bg='#869db0',
                    command=lambda: press(1), height=2, width=12)
    # specifing the position of button
    button1.grid(row=2, column=0)
 
    button2 = Button(window, text=' 2 ', fg='black', bg='#869db0',
                    command=lambda: press(2), height=2, width=12)
    button2.grid(row=2, column=1)
 
    button3 = Button(window, text=' 3 ', fg='black', bg='#869db0',
                    command=lambda: press(3), height=2, width=12)
    button3.grid(row=2, column=2)
 
    button4 = Button(window, text=' 4 ', fg='black', bg='#869db0',
                    command=lambda: press(4), height=2, width=12)
    button4.grid(row=3, column=0)
 
    button5 = Button(window, text=' 5 ', fg='black', bg='#869db0',
                    command=lambda: press(5), height=2, width=12)
    button5.grid(row=3, column=1)
 
    button6 = Button(window, text=' 6 ', fg='black', bg='#869db0',
                    command=lambda: press(6), height=2, width=12)
    button6.grid(row=3, column=2)
 
    button7 = Button(window, text=' 7 ', fg='black', bg='#869db0',
                    command=lambda: press(7), height=2, width=12)
    button7.grid(row=4, column=0)
 
    button8 = Button(window, text=' 8 ', fg='black', bg='#869db0',
                    command=lambda: press(8), height=2, width=12)
    button8.grid(row=4, column=1)
 
    button9 = Button(window, text=' 9 ', fg='black', bg='#869db0',
                    command=lambda: press(9), height=2, width=12)
    button9.grid(row=4, column=2)
 
    button0 = Button(window, text=' 0 ', fg='black', bg='#869db0',
                    command=lambda: press(0), height=2, width=12)
    button0.grid(row=5, column=0)
 
    plus = Button(window, text=' + ', fg='black', bg='#869db0',
                command=lambda: press("+"), height=2, width=12)
    plus.grid(row=2, column=3)
 
    minus = Button(window, text=' - ', fg='black', bg='#869db0',
                command=lambda: press("-"), height=2, width=12)
    minus.grid(row=3, column=3)
 
    multiply = Button(window, text=' * ', fg='black', bg='#869db0',
                    command=lambda: press("*"), height=2, width=12)
    multiply.grid(row=4, column=3)
 
    divide = Button(window, text=' / ', fg='black', bg='#869db0',
                    command=lambda: press("/"), height=2, width=12)
    divide.grid(row=5, column=3)
 
    equal = Button(window, text=' = ', fg='black', bg='#869db0',
                command=evaluate, height=2, width=12)
    equal.grid(row=5, column=2)
 
    clear = Button(window, text='Clear', fg='black', bg='#869db0',
                command=clear, height=2, width=12)
    clear.grid(row=5, column='1')
 
    Decimal= Button(window, text='.', fg='black', bg='#869db0',
                    command=lambda: press('.'), height=2, width=12)
    Decimal.grid(row=6, column=0)
    # for preventing the gui window from disappearing
    window.mainloop()