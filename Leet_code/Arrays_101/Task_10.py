# def replacement(x):
#     for i in x[:]: #запуск цикла по всем элементам
#         if i % 2 != 0:
#             x.remove(i) # удаляем i-тый элемент так как нечет
#             x.append(i) # добавляем тот же элемент в конец
#     return x
#
#
#
# a = [3,1,2,4]
# print(zam(a))

def rep(x):
    return [i for i in x if i % 2 == 0] + [i for i in x if  i % 2 != 0]#генерируем массивы четных и нечетных элементов
                                                                       #из массива x и складываем их
d = [3,1,2,4]
print(rep(d))
