import ruble
while True:
    try:
        employees_num = int(input('Введите число сотруднников 1-1000:  '))
        assert 1 <= employees_num <= 1000
    except AssertionError:
        print('Число не в диапазоне!')
        break
    except ValueError:
        print('Введите ЧИСЛО!')
        break
    sum = 0
    distance_list = []
    price_list = []
    try:
        for i in range(employees_num):
            distance = int(input('Введите расстояние до дома {0}-го сотрудника(целое число): '.format(i+1)))
            distance_list.append(distance)
        for i in range(employees_num):
            price = int(input('Введите тариф {0}-го такси(целое число):  '.format(i+1)))
            price_list.append(price)
    except ValueError:
        print('Неверный ввод с клавиатуры')
        break
    c_distance_list = distance_list[:] #Создаём копии списков
    c_price_list = price_list[:]
    index_list_d = []                  #Создаём списки, где будут хранится индексы наших значений
    index_list_p = []
    #Заполняем списки индексами в порядке возр/убыв значений переменных
    max_distance = 0
    for i in range(employees_num):                              
        index = c_distance_list.index(max(c_distance_list))
        index_list_d.append(index)
        c_distance_list[index] = 0
    for i in range(employees_num):
        index = c_price_list.index(min(c_price_list))
        index_list_p.append(index)
        c_price_list[index] = 10**10
    #Для i-го клиента в паре списков с индексам (расстояние по убыванию/цена по возрастанию) ищем нужный индекс такси 
    print('Такси для клиента 1, 2, 3, ...:')
    for i in range(employees_num):
        taxi_num = index_list_p[index_list_d.index(i)]
        print(taxi_num+1)
    for i in range(employees_num):
        sum += distance_list[index_list_d[i]]*price_list[index_list_p[i]]
    print(sum)
    print('Необходимо заплатить:')
    ruble.out(sum)

