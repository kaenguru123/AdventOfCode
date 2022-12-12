with open('.\Day04\InputDay04.txt') as f:
    
    line = f.readline()
    fully_contain_cnt = 0

    while (line != ''):
        first_elv, second_elv = line.split(',', 1)
        first_elv_start, first_elv_end = first_elv.split('-', 1)
        second_elv_start, second_elv_end = second_elv.split('-', 1)

        first_elv_start = int(first_elv_start)
        first_elv_end = int(first_elv_end)
        second_elv_start = int(second_elv_start)
        second_elv_end = int(second_elv_end)

        if ((first_elv_start <= second_elv_start and first_elv_end >= second_elv_end)
            or (second_elv_start <= first_elv_start and second_elv_end >= first_elv_end)):
            fully_contain_cnt += 1
        
        if (first_elv_start == second_elv_start and first_elv_end == second_elv_end):
            pass

        line = f.readline()

    print(fully_contain_cnt)