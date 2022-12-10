def get_biggest_value(list_of_values):
    biggest_value = 0
    for value in list_of_values:
        if value > biggest_value:
            biggest_value = value
    return biggest_value

with open('.\InputDay01.txt') as f:
    line = f.readline()
    
    list_of_sums = []

    while (line != ''):
        sum = 0
        while (line != '\n' and line != ''):
            sum += int(line)
            line = f.readline()
        list_of_sums.append(sum)
        line = f.readline()
    
    res = 0
    biggest = get_biggest_value(list_of_sums)
    res += biggest
    list_of_sums.remove(biggest)
    biggest = get_biggest_value(list_of_sums)
    res += biggest
    list_of_sums.remove(biggest)
    biggest = get_biggest_value(list_of_sums)
    res += biggest
    
    print(res)