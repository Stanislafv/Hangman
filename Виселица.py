import random
try:
    rejim = int(input("Введите режим игры(3 - 3 буквы, 4 - 4 буквы, 5 - 5 букв)"))
except ValueError:
    print("Вы точно ввели цифру?")
    try:
        rejim = int(input("Введите режим игры(3 - 3 буквы, 4 - 4 буквы, 5 - 5 букв)"))
    except ValueError:
        print("Вы ТОЧНО ввели цифру!?")
        try:
            rejim = int(input("Введите режим игры(3 - 3 буквы, 4 - 4 буквы, 5 - 5 букв)"))
        except ValueError:
            rejim = -256
if rejim == 3:
    while True:
        zagadka = random.choice(["лес","дом","час","ель","юла","лев","эхо","зло","кол","рот","еда","боб","бор","раб","око","мел","миг","ива"])
        bukva1 = "_"
        bukva2 = "_"
        bukva3 = "_"
        oshibki = 6
        used = []
        while True:
            if bukva1 == zagadka[0] and bukva2 == zagadka[1] and bukva3 == zagadka[2]:
                print("Вы выйграли!")
                break
            elif oshibki == 0:
                print("Вы проиграли!")
                print("Было загадано слово:",zagadka)
                break
            otvet = input("Введите букву:")
            if len(otvet) != 1:
                print("Вы точно ввели одну букву?")
                continue
            if otvet in used:
                print("Вы уже вводили эту букву!")
                continue
            else:
                used.append(otvet)
            if otvet == zagadka[0]:
                bukva1 = zagadka[0]
            elif otvet == zagadka[1]:
                bukva2 = zagadka[1]
            elif otvet == zagadka[2]:
                bukva3 = zagadka[2]
            else:
                oshibki -= 1
            print("У вас осталось",oshibki,"Жизней")
            print("Поле:")
            print(bukva1,bukva2,bukva3)            
elif rejim == 4:
    while True:
        zagadka = random.choice(["ночь","соль","каша","море","часы","рыба","мясо","пюре","язык","небо","лето","зима","ложь","рожь","гора","утка","рога","зной","волк","душа","луна"])
        bukva1 = "_"
        bukva2 = "_"
        bukva3 = "_"
        bukva4 = "_"
        oshibki = 6
        used = []
        while True:
            if bukva1 == zagadka[0] and bukva2 == zagadka[1] and bukva3 == zagadka[2] and bukva4 == zagadka[3]:
                print("Вы выйграли!")
                break
            elif oshibki == 0:
                print("Вы проиграли!")
                print("Было загадано слово:",zagadka)
                break
            otvet = input("Введите букву:")
            if len(otvet) != 1:
                print("Вы точно ввели одну букву?")
                continue
            if otvet in used:
                print("Вы уже вводили эту букву!")
                continue
            else:
                used.append(otvet)
            if otvet == zagadka[0]:
                bukva1 = zagadka[0]
            elif otvet == zagadka[1]:
                bukva2 = zagadka[1]
            elif otvet == zagadka[2]:
                bukva3 = zagadka[2]
            elif otvet == zagadka[3]:
                bukva4 = zagadka[3]
            else:
                oshibki -= 1
            print("У вас осталось",oshibki,"Жизней")
            print("Поле:")
            print(bukva1,bukva2,bukva3,bukva4)
elif rejim == 5:

    while True:
        zagadka = random.choice(["агент","алмаз","башня","груша","дверь","гараж","дубль","арбуз","дерби","голос","гроза","дождь","палец","добро","доска","дрель","жесть","земля","звено","знамя"])
        bukva1 = "_"
        bukva2 = "_"
        bukva3 = "_"
        bukva4 = "_"
        bukva5 = "_"
        oshibki = 6
        used = []
        while True:
            if bukva1 == zagadka[0] and bukva2 == zagadka[1] and bukva3 == zagadka[2] and bukva4 == zagadka[3] and bukva5 == zagadka[4]:
                print("Вы выйграли!")
                break
            elif oshibki == 0:
                print("Вы проиграли!")
                print("Было загадано слово:",zagadka)
                break
            otvet = input("Введите букву:")
            if len(otvet) != 1:
                print("Вы точно ввели одну букву?")
                continue
            if otvet in used:
                print("Вы уже вводили эту букву!")
                continue
            else:
                used.append(otvet)
            if otvet == zagadka[0]:
                bukva1 = zagadka[0]
            elif otvet == zagadka[1]:
                bukva2 = zagadka[1]
            elif otvet == zagadka[2]:
                bukva3 = zagadka[2]
            elif otvet == zagadka[3]:
                bukva4 = zagadka[3]
            elif otvet == zagadka[4]:
                bukva5 = zagadka[4]
            else:
                oshibki -= 1
            print("У вас осталось",oshibki,"Жизней")
            print("Поле:")
            print(bukva1,bukva2,bukva3,bukva4,bukva5)
elif rejim == -256:
    print("Перезапускай и вводи нормально")
elif rejim != 3 and rejim != 4 and rejim != 5:
    print("Вы ввели неправильное число букв, можно от 3 до 5")
