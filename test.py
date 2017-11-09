import Tkinter
import random
import tkMessageBox

# novejsa knjiznica za GUI je PyQt

window = Tkinter.Tk()
# greeting text
greeting = Tkinter.Label(window, text="Ugani skrito stevilko!")
greeting.pack()

secret = random.randint(1, 100)

# guess entry field
guess = Tkinter.Entry(window)
guess.pack()

# check guess
def check_guess():
    if int(guess.get()) == secret:
        result_text = "CORRECT"
    elif int(guess.get())> secret:
        result_text = "WRONG! Your guess is too high"
    else:
        result_text = "WRONG! Your guess is to low"

    tkMessageBox.showinfo("Result", result_text)

#  submit window
submit = Tkinter.Button(window, text="Submit", command=check_guess)  # check_guess, not check_guess()
submit.pack()




window.mainloop()
