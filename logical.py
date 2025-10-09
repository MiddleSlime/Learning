
name = input("Введите ваше имя: ")
# result = name.find("A")
# result = name.rfind("m")
# name = name.capitalize()
name = name.replace(" ", "")

if not name.isalpha():
    print("В имени пользователя не должны присутствовать цифры")
elif len(name) < 2:
    print("Слишком малое количество букв")
elif len(name) > 12:
    print("Слишком большое количество букв")
else:
    print(name)
