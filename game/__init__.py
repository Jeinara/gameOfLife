# Правила игры Жизнь:
# 1. В пустой клетке, рядом с которой ровно три живые клетки, зарождается жизнь.
# 2. Если у живой клетки есть две или три живые соседки, она продолжает жить, в противном случае умирает.
# Игра прекращается, если:
# На поле не остается ни одной живой клетки
# Конфигурация на на очередном шаге в точности повторит себя на одном из более ранних шагов. ????
# При очередном шаге ни одна из клеток не меняет своего состояния


import random


def new_cell_list(n):
    # генерация нового поля размером n на n
    cell_list = []
    for i in range(n):
        row_list = list()
        for j in range(n):
            row_list.append(random.randint(0, 1))
        cell_list.append(row_list)
    return cell_list


def new_generation(cell_list):
    pass


def death(cell_list):
    pass


def next_step(death_list, life_list):
    pass


if __name__ == '__main__':
    print(new_cell_list(5))