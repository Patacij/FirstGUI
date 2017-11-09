import Tkinter
import tkMessageBox

window = Tkinter.Tk()

x = Tkinter.Label(window, text="Izberi stevilo x!")
x.pack()

# first_number entry field
first_number = Tkinter.Entry(window)
first_number.pack()

operacija = Tkinter.Label(window, text="Izberi racunsko operacijo!")
operacija.pack()

# operation entry field
funkcija = Tkinter.Entry(window)
funkcija.pack()


y = Tkinter.Label(window, text="Izberi stevilo y!")
y.pack()

# second_number entry field
second_number = Tkinter.Entry(window)
second_number.pack()

def calculate():
    operation = funkcija.get()

    x = int(first_number.get())
    y = int(second_number.get())

    if operation == '+':
        # print(x + y)
        tkMessageBox.showinfo("Result", (x + y))
    elif operation == '-':
        # print(x - y)
        tkMessageBox.showinfo("Result", (x - y))
    elif operation == '*':
        # print(x * y)
        tkMessageBox.showinfo("Result", (x * y))
    elif operation == '/':
        # print(x / y)
        tkMessageBox.showinfo("Result", (x / y))
    else:
        tkMessageBox.showinfo("Wrong operation!")


#  submit window
submit = Tkinter.Button(window, text="Izracun", command=calculate)  # izracunaj()
submit.pack()


window.mainloop()

# print(x+y)