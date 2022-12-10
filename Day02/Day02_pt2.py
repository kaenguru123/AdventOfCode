r_p_s = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'X' : 1,
    'Y' : 2,
    'Z' : 3,
    }

with open('.\Day02\InputDay02.txt') as f:
    line = f.readline()

    score = 0

    while (line != ''):
        player = r_p_s[line[2]]
        opponent = r_p_s[line[0]]

        match player:
            case 1:
                match opponent:
                    case 1:
                        score += 3
                    case 2:
                        score += 1
                    case 3:
                        score += 2
            case 2:
                score += opponent + 3
            case 3: 
                match opponent:
                    case 1:
                        score += 8
                    case 2:
                        score += 9
                    case 3:
                        score += 7

        line = f.readline()

    print(score)