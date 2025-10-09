import random

difficulty = ["1", "2", "3"]
difficulty = input("Выберите уровень сложности(1, 2 или 3): ")
if difficulty not in ["1", "2", "3"]:
        print("Выбрано неверное значение")


if difficulty == "1":
    random_number = random.randint(1, 10)
    print("Вам необходимо угадать цифру от 1 до 10")
elif difficulty == "2":
        random_number = random.randint(1, 50)
        print("Вам необходимо угадать цифру от 1 до 50")
elif difficulty == "3":
        random_number = random.randint(1, 100)
        print("Вам необходимо угадать цифру от 1 до 100")

attempts = 0
play = True
while play:
    attempts = attempts + 1

    answer = int(input("Ваша задача угадать её: "))
    if answer == random_number:
        print("Поздравляю! Вы угадали загаданную цифру!")
        print(f"Вы угадали за {attempts} попыток")
        play = False

        if difficulty == "1":
            if answer == random_number and 1 < attempts <= 3:
                print("У вас получилось достаточно быстро!")
            elif 3 < attempts <= 5:
                print("Вы управились за нормальное количество попыток")
            elif 5 < attempts <= 7:
                print("Надеюсь в следующий раз вам повезёт больше")
            else:
                print("Уверен в следующий раз у вас получится лучше!")

        elif difficulty == "2":
            if 3 <= attempts <= 5:
                print("У вас получилось достаточно быстро!")
            elif 5 < attempts <= 7:
                print("Вы управились за нормальное количество попыток")
            elif 7 < attempts <= 9:
                print("Надеюсь в следующий раз вам повезёт больше")
            else:
                print("Уверен в следующий раз у вас получится лучше!")

        elif difficulty == "3":
            if 5 < attempts <= 7:
                print("У вас получилось достаточно быстро!")
            elif 7 < attempts <= 9:
                print("Вы управились за нормальное количество попыток")
            elif 10 < attempts <= 11:
                print("Надеюсь в следующий раз вам повезёт больше")
            else:
                print("Уверен в следующий раз у вас получится лучше!")

    elif answer > random_number:
            print("К сожалению вы не угадали, попробуйте число поменьше")
    elif answer < random_number:
            print("К сожалению вы не угадали, попробуйте число побольше")




