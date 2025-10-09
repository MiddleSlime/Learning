import random
from tabnanny import check

# Камень ножницы бумага написанные лично мной из интереса


moves = ["камень", "ножницы" , "бумага"]
game = True
while game:
    user_attack = input("Выберите в этом раунде: камень, ножницы, бумага или выход: ")

    if user_attack == "выход":
        print("Спасибо что поиграли!")
        game = False
        continue
    if user_attack not in moves:
        print("Вы можете ставить только данные вам атаки")
        continue

    enemy_attack = random.choice(moves)
    print(f"Противник выбрал {enemy_attack}")

    if user_attack == enemy_attack:
        print("Ничья!")
    elif user_attack == "камень" and enemy_attack == "ножницы":
        print("Вы победили!")
    elif user_attack == "камень" and enemy_attack == "бумага":
        print("Оппонент победил!")
    elif user_attack == "ножницы" and enemy_attack == "камень":
        print("Оппонент победил!")
    elif user_attack == "ножницы" and enemy_attack == "бумага":
        print("Вы победили!")
    elif user_attack == "бумага" and enemy_attack == "камень":
        print("Вы победили!")
    elif user_attack == "бумага" and enemy_attack == "ножницы":
     print("Оппонент победил!")


