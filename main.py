from nested_list import my_list_hard, my_list_simple
from generator import flat_generator
from iterator import FlatIterator

if __name__ == '__main__':
    print('Задача 1')
    for item in FlatIterator(my_list_simple):
        print(item)
    print('*' * 25)

    print('Задача 2')
    for item in flat_generator(my_list_simple):
        print(item)
    print('*' * 25)

    print('Задача 3')
    for item in FlatIterator(my_list_hard):
        print(item)
    print('*' * 25)

    print('Задача 4')
    for item in flat_generator(my_list_hard):
        print(item)
    print('*' * 25)
