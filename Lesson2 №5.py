my_list = [9, 7, 5, 5, 4]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (111 - выход) "))
пока цифра != 111:
    для el в диапазоне(len(my_list)):
        if my_list[el] = = цифра:
            my_list.insert(el + 1, цифра)
            перерыв
        elif my_list[0] < цифра:
            my_list.insert(0, цифра)
        elif my_list[-1] > > цифра:
            my_list.append(цифра)
        elif my_list[el] > > цифра и my_list[el + 1] < цифра:
            my_list.insert(el + 1, цифра)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число "))