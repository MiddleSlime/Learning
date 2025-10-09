import math

while True: #Позволяет бесконечно использовать программу
    operation = input("Выберите операцию(+, -, /, *, кр, ст, %) или введите 'выход': ")
    if operation == "выход":
        print("Конец работы")
        break
    if operation not in ["+", "-", "/", "*", "кр", "ст", "%"]:
        print("Выбрано недопустимое действие")
        continue
    try:
        a= float(input("Введите первое число: "))
        if operation != "кр":
            b = float(input("Введите второе число: "))
    except ValueError:
        print("Выбрано неверное значение")
        continue

    result= None

    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "/":
        if b != 0:
            result = a / b
        else:
            print("Ошибка: деление на ноль!")
    elif operation == "*":
        result = a * b
    elif operation == "кр":
        if a >= 0:
            result = math.sqrt(a)
        else:
            print("Введено отрицательное значение. Операция отменена")
    elif operation == "ст":
        
        result = a ** b
    elif operation == "%":
        result = a % b


    print("Ответ:", result)
    continue


