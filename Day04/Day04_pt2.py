with open('.\Day04\InputDay04.txt') as f:
    
    line = f.readline()
    contain_cnt = 0

    while (line != ''):
        first_elv, second_elv = line.split(',', 1)
        first_elv_start, first_elv_end = first_elv.split('-', 1)
        second_elv_start, second_elv_end = second_elv.split('-', 1)

        first_ass = range(int(first_elv_start), int(first_elv_end)+1)
        second_ass = range(int(second_elv_start), int(second_elv_end)+1)

        for i in first_ass:
            if (i in second_ass):
                contain_cnt+=1
                break

        line = f.readline()

    print(contain_cnt)