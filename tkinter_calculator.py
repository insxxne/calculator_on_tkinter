import tkinter as tk
from tkinter import messagebox
win = tk.Tk()
def add_number(number):
    value = calc.get()
    if value[0] == '0' and len(value)==1:
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value+number)

def add_operation(operation):
        value = calc.get()
        if value[-1] in '-+/*':
            value = value[:-1]
        elif '+' in value or '-' in value or '*' in value or '/' in value:
            calculate()
            value = calc.get()
        calc.delete(0, tk.END)
        calc.insert(0, value+operation)

def clear():
    calc.delete(0,tk.END)
    calc.insert(0, '0')
def calculate():
    value = calc.get()
    if value[-1] in '-+/*':
        operation = value[-1]
        value = value[:-1] + operation + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0,eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo("Внимание", "Вы ввели неправильные символы, вводите только цифры!")
        calc.insert(0, '0')
    except ZeroDivisionError:
        messagebox.showinfo("Внимание", "На ноль делить нельзя!")
def make_button(number):
    return tk.Button(text=number, font=("Arial", 15), bd=5,command= lambda : add_number(number))

def make_operation_button(operation):
    return tk.Button(text=operation, font=("Arial", 15), bd=5,command= lambda : add_operation(operation))

def make_calc(operation):
    return tk.Button(text=operation, font=("Arial", 15), bd=5,command=calculate)

def make_clear_button(operation):
    return tk.Button(text=operation, font=("Arial", 15), bd=5,command=clear)
win.title("Калькулятор")
win.geometry("220x260+100+200")
photo = tk.PhotoImage(file="calculator.png")
win.iconphoto(False, photo)
win["bg"]="#B00000"

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0,'0')
calc.grid(row=0, column=0, columnspan=4, stick="we", padx=5)
make_button('1').grid(row=1, column=0, stick="wesn", padx=5, pady=5)
make_button('2').grid(row=1, column=1, stick="wesn", padx=5, pady=5)
make_button('3').grid(row=1, column=2, stick="wesn", padx=5, pady=5)
make_button('4').grid(row=2, column=0, stick="wesn", padx=5, pady=5)
make_button('5').grid(row=2, column=1, stick="wesn", padx=5, pady=5)
make_button('6').grid(row=2, column=2, stick="wesn", padx=5, pady=5)
make_button('7').grid(row=3, column=0, stick="wesn", padx=5, pady=5)
make_button('8').grid(row=3, column=1, stick="wesn", padx=5, pady=5)
make_button('9').grid(row=3, column=2, stick="wesn", padx=5, pady=5)
make_button('0').grid(row=4, column=0, stick="wesn", padx=5, pady=5)

make_operation_button("+").grid(row=1, column=3, stick="wesn", padx=5, pady=5)
make_operation_button("-").grid(row=2, column=3, stick="wesn", padx=5, pady=5)
make_operation_button("/").grid(row=3, column=3, stick="wesn", padx=5, pady=5)
make_operation_button("*").grid(row=4, column=3, stick="wesn", padx=5, pady=5)

make_calc("=").grid(row=4, column=2, stick="wesn", padx=5, pady=5)
make_clear_button("С").grid(row=4, column=1, stick="wesn", padx=5, pady=5)

win.grid_columnconfigure(0,minsize=50)
win.grid_columnconfigure(1,minsize=50)
win.grid_columnconfigure(2,minsize=50)
win.grid_columnconfigure(3,minsize=50)

win.grid_rowconfigure(0,minsize=50)
win.grid_rowconfigure(1,minsize=50)
win.grid_rowconfigure(2,minsize=50)
win.grid_rowconfigure(3,minsize=50)
win.grid_rowconfigure(4,minsize=50)

win.mainloop()