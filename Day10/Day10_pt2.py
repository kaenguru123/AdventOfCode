with open('.\Day10\Input10.txt') as f:
    line = f.readline()
    x = 1
    cycle = 1
    pixel = 0
    is_in_add_x = 0
    
    while(line != ''):
        debug = [cycle, pixel, x, line[5:len(line)-1]]
        print('#', end='') if (x-1 == pixel or x == pixel or x+1 == pixel) else print('.', end='')
        if (pixel==39): 
            print('')
            pixel = 0
        else:
            pixel += 1
        
        cycle += 1

        if (line[0:4] == 'addx' and is_in_add_x != 1):
            is_in_add_x = 1
        elif (line[0:4] == 'addx'):
            x += int(line[5:len(line)-1])
            is_in_add_x = 0

        if (is_in_add_x == 0): 
            line = f.readline()