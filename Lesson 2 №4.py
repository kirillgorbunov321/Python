my_str = input("введите строку ")
my_word = []
num = 1
для el в диапазоне(my_str.count('') + 1):
    my_word = my_str.split()
    if len(str(my_word)) < = 10:
        print(f " {num} {my_word [el]}")
        num += 1
    остальное:
        print(f " {num} {my_word [el] [0:10]}")
        num += 1