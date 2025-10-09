import random

moves = {
    "камень": "ножницы",
    "ножницы": "бумага",
    "бумага": "камень"
}
game = True
while game:

    user_attack = input("камень, ножницы, бумага или 'выход': ")

    if user_attack == "выход":
        print("Спасибо что поиграли!")
        game = False
        continue
    elif user_attack not in moves:
        print("Вы можете ставить только данные вам атаки")

    else:
        enemy_attack = random.choice(list(moves))
        print(f"Противник выбрал {enemy_attack}")

        if user_attack == enemy_attack:
            print("Ничья!")
        elif moves[user_attack] == enemy_attack:
            print("Вы победили!")
        else:
            print("Вы проиграли!")