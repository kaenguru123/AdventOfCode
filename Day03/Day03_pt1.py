with open('.\Day03\InputDay03.txt') as f:
    
    line = f.readline()

    sum = 0

    while (line != ''):
        l = len(line)
        if line[l-1] == '\n':
            line = line[0:l-1]
        l = len(line)
        if ( l/2%1 != 0):
            pass
        comp_one = line[0:int(l/2)]
        comp_two = line[int(l/2):l]
        
        for item in comp_one:
            if (item in comp_two):
                value = ord(item)
                sum += value - 96 if item.islower() else value - 38
                break
        
        line = f.readline()

    print(sum)