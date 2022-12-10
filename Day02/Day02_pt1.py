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

        if player == opponent:
            score += player + 3
        elif (player == 1 and opponent == 3) or (player == 2 and opponent == 1) or (player == 3 and opponent == 2):
            score += player + 6
        else:
            score += player

        line = f.readline()

    print(score)