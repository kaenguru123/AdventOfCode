with open('.\Day03\InputDay03.txt') as f:
    sum = 0
    comps = True

    while (comps):
        comp_one = f.readline()
        comp_two = f.readline()
        comp_three = f.readline()

        comps = not (comp_one == '' or comp_two == '' or comp_three == '')
        if not comps: break

        comp_one = comp_one.removesuffix('\n')
        comp_two = comp_two.removesuffix('\n')
        comp_three =comp_three.removesuffix('\n')

        
        for item in comp_one:
            if (item in comp_two and item in comp_three):
                value = ord(item)
                sum += value - 96 if item.islower() else value - 38
                break
        
    print(sum)