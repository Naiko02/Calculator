def plus(n1,n2):
    if (type(n1) != int and type(n1) != float) or (type(n2) != int and type(n2) != float):
        return "Вводите только числа"
    else:
        return n1+n2
def minus(n1,n2):
    if (type(n1) != int and type(n1) != float) or (type(n2) != int and type(n2) != float):
        return "Вводите только числа"
    else:
        return n1-n2
def divide(n1,n2):
    if (type(n1) != int and type(n1) != float) or (type(n2) != int and type(n2) != float):
        return "Вводите только числа"
    elif n2==0:
        return "Нельзя делить на 0"
    else:
        return n1/n2
def multiply(n1,n2):
    if (type(n1) != int and type(n1) != float) or (type(n2) != int and type(n2) != float):
        return "Вводите только числа"
    else:
        return n1*n2
def power(n1,n2):
    if (type(n1) != int and type(n1) != float) or (type(n2) != int and type(n2) != float):
        return "Вводите только числа"
    else:
        return n1**n2
def sqrt(n1):
    if type(n1) != int and type(n1) != float:
        return "Вводите только числа"
    elif n1<=0:
        return "Вводите под корень положительные числа"
    else:
        return n1**(1/2)
def factorial(n1):

    if type(n1) != int and type(n1) != float:
        return "Вводите только числа"
    elif n1<=0:
        return "Вводите в факториал положительные числа"
    elif type(n1) != int:
        return "Вводите в факториал целые числа"
    else:
        result = 1
        for i in range(1, n1 + 1):
            result = result * i
        return result
