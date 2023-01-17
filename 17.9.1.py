#Бинарный поиск
def binary_search(values_list, input_value, left, right):
    #try:
        if left > right:
            return False
        middle = (right + left)//2
        if values_list[middle] == input_value:
            print('Позиция предыдущего индекса введенного числа списка:',middle-1)
            print('Позиция следующего индекса введенного числа списка:',middle+1)
            return middle
        elif input_value < values_list[middle]:
            return binary_search(values_list, input_value, left, middle-1)
        else:
            return binary_search(values_list, input_value, middle+1, right)

#Добавление
def values_add(values_list,input_value):       
    if any(input_value == x for x in values_list) is False:
        if input_value % 1 == 0:
            values_list.append(input_value)
    else:
        return print('Добавляемое значение есть в списке.')
    return values_list
        
#Сортировка        
def values_sort(values_list):  
    return values_list.sort()

#Ввод и обработка исключений
values_list = input("Введите список целых чисел, разделенных пробелом:").split()
try:    
    if len(values_list) > 0:
        try:
            values_list = [int(i) for i in values_list]
            input_value = int(input('Введите добавляемое целое число :'))
            #Проверка вхождения в диапазон values_list
            if min(values_list, key=lambda i : int(i)) <= input_value and max(values_list, key=lambda i : int(i)) >= input_value:
                values_add(values_list,input_value)
                values_sort(values_list)
                print('Список отсортированный по возрастанию :', values_list)
                print('Индекс введенного числа - ',
                  binary_search(values_list,input_value,0,len(values_list)))
            else:
                print("Выход за пределы значений списка")   
        except ValueError:
            print("Ошибка ввода. Введите 'целые' числа через пробел.")
    else:    
        raise EOFError
except EOFError:            
    print("Пустое поле ввода")
     


    
    
    
