# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

my_list = [2, 2, 3, 3, 4, 5, 8, 8]
double_elem = []
for i in my_list:
    if i > 1 not in double_elem:
        double_elem.count(i)
double_elem = set(filter(lambda x: my_list.count(x) > 1, my_list))
print(f'{double_elem = }')
