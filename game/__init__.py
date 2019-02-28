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


def born_and_death(cell_list):
    born_list = []
    death_list = []
    for i in range(len(cell_list)):
        born_row_list = list()
        death_row_list = list()
        for j in range(len(cell_list[0])):
            c = 0
            for i1 in range(i-1, i+2):
                for j1 in range(j-1, j+2):
                    if ((i1 != i) and (j1 != j)) or (i1 != i) or(j1 != j):
                        k = len(cell_list[0])-1 if i1 == -1 else 0 if i1 == len(cell_list[0]) else i1
                        d = len(cell_list[0])-1 if j1 == -1 else 0 if j1 == len(cell_list[0]) else j1
                        c += cell_list[k][d]
            if (c >= 3) and (cell_list[i][j] == 0):
                born_row_list.append(1)
            else:
                born_row_list.append(0)
            if (c in range(2, 3)) and (cell_list[i][j] == 1):
                death_row_list.append(1)
            else:
                death_row_list.append(0)
        born_list.append(born_row_list)
        death_list.append(death_row_list)
    return born_list, death_list


def next_step(born_list, death_list):
    cell_list = list()
    for i in range(len(born_list)):
        cell_row_list = list()
        for j in range(len(born_list[0])):
            cell_row_list.append(born_list[i][j]+death_list[i][j])
        cell_list.append(cell_row_list)
    return cell_list


if __name__ == '__main__':
    cell_list = new_cell_list(5)
#    cell_list = [[1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 1, 0], [0, 0, 1, 1, 0]]
    for i in range(len(cell_list)):
        print(cell_list[i])
    ce = born_and_death(cell_list)
    cell_list = next_step(ce[0], ce[1])
    print('_____________________')
    for i in range(len(cell_list)):
        print(cell_list[i])