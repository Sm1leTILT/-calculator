
from tkinter import *

# Функция для сложения двух чисел
def add(x, y):
    return x + y

# Функция для вычитания двух чисел
def subtract(x, y):
    return x - y

# Функция для умножения двух чисел
def multiply(x, y):
    return x * y

# Функция для деления двух чисел
def divide(x, y):
    return x / y

# Создаем экземпляр класса Tk
root = Tk()
root.title("Калькулятор")

# Создаем поле ввода
input_field = Entry(root, width=35, borderwidth=5)
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Функция для добавления цифр в поле ввода
def button_click(number):
    current = input_field.get()
    input_field.delete(0, END)
    input_field.insert(0, str(current) + str(number))

# Функция для очистки поля ввода
def button_clear():
    input_field.delete(0, END)

# Функция для выполнения операций
def button_operation(operation):
    global first_num
    first_num = float(input_field.get())
    input_field.delete(0, END)
    global math_operation
    math_operation = operation

# Функция для вывода результата
def button_equal():
    second_num = float(input_field.get())
    input_field.delete(0, END)

    if math_operation == 'addition':
        result = add(first_num, second_num)
        input_field.insert(0, result)

    elif math_operation == 'subtraction':
        result = subtract(first_num, second_num)
        input_field.insert(0, result)

    elif math_operation == 'multiplication':
        result = multiply(first_num, second_num)
        input_field.insert(0, result)

    elif math_operation == 'division':
        result = divide(first_num, second_num)
        input_field.insert(0, result)

# Создаем кнопки
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_operation('addition'))
button_subtract = Button(root, text="-", padx=41, pady=20, command=lambda: button_operation('subtraction'))
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: button_operation('multiplication'))
button_divide = Button(root, text="/", padx=41, pady=20, command=lambda: button_operation('division'))

button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# Размещаем кнопки на экране
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)

# Запускаем главный цикл
root.mainloop()
