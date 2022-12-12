with open('.\Day10\Input10.txt') as f:
    line = f.readline()
    x = 1
    cycle = 1
    sum = 0
    
    while(line != ''):
        if (line[0:4] == 'addx'):
            for i in range(2):
                if (cycle in [20,60,100,140,180,220]): 
                    sum += x*cycle
                if (i == 1): x += int(line[4:len(line)])
                cycle += 1
        else:
            if (cycle in [20,60,100,140,180,220]): 
                sum += x*cycle
            cycle += 1
        line = f.readline()

    print(sum)