import tkinter as tk
import re
import CalculatorOperator






def click_button(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        prim = razbit()
        while (True):
            if ('!' in prim):
                i=prim.index("!")
                prim[i-1]=CalculatorOperator.factorial(int(prim[i-1]))
                prim.pop(i)
                continue
            elif ('√' in prim):
                i = prim.index("√")
                prim[i + 1] = CalculatorOperator.sqrt(float(prim[i + 1]))
                prim.pop(i)
                continue
            elif ('^' in prim):
                i=prim.index("^")
                print(float(prim[i - 1]))
                print(float(prim[i + 1]))
                print(float(prim[i-1])**float(prim[i+1]))
                prim[i-1]=CalculatorOperator.power(float(prim[i-1]),float(prim[i+1]))
                prim.pop(i+1)
                prim.pop(i)
                continue
            elif ('*' in prim):
                i=prim.index("*")
                prim[i-1]=CalculatorOperator.multiply(float(prim[i-1]),float(prim[i+1]))
                prim.pop(i+1)
                prim.pop(i)
                continue
            elif('/' in prim):
                i = prim.index("/")
                prim[i - 1] = CalculatorOperator.divide(float(prim[i - 1]), float(prim[i + 1]))
                prim.pop(i + 1)
                prim.pop(i)
                continue
            elif ('+' in prim):
                i = prim.index("+")
                prim[i - 1] = CalculatorOperator.plus(float(prim[i - 1]), float(prim[i + 1]))
                prim.pop(i + 1)
                prim.pop(i)
                continue
            elif ('-' in prim):
                i = prim.index("-")
                prim[i - 1] = CalculatorOperator.minus(float(prim[i - 1]), float(prim[i + 1]))
                prim.pop(i + 1)
                prim.pop(i)
                continue
            break


        result = prim[0]
        print(result)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        clear_display()
        display.insert(0, "Ошибка")



def parse_expression(expression):
    # Разбиение выражения на числа и операторы
    tokens = re.findall(r'[+\-*/^!√()]|\d*\.\d+|\d+', expression)
    return tokens
def razbit():
    # Пример использования функции
    expression = display.get()
    parsed_expression = parse_expression(expression)
    return parsed_expression


# Создаем главное окно приложения
root = tk.Tk()
root.title("Калькулятор")

# Экран калькулятора
display = tk.Entry(root, width=30, borderwidth=10, relief=tk.RIDGE, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Кнопки калькулятора
buttons = [
    '7', '8', '9', '/','*',
    '4', '5', '6', '+','-',
    '1', '2', '3','√','^',
    'C', '0', '.','=','!'
]

row = 1
col = 0
for button in buttons:
    action = lambda x=button: click_button(x) if x != "=" and x != "C" else clear_display() if x == "C" else calculate()
    tk.Button(root, text=button, width=3, height=3, command=action)\
        .grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 4:
        col = 0
        row += 1

# Конфигурация столбцов для равномерного распределения пространства
for i in range(5):
    root.grid_columnconfigure(i, weight=1)


# Запускаем главный цикл приложения
root.mainloop()


