import random

def labyrinthOut(labyrinth, n):
    for i in range(0, n):
        print("")
        for j in range(0, n):
            print("{:4s}".format(str(labyrinth[i][j])), end="")
    print('')

def labyrinthCleaning(labyrinth, n):
    for i in range(1, n):
        for j in range(1, n):
            if (type(labyrinth[i][j]) == int):
                labyrinth[i][j] = '.'
    return labyrinth

def findDaWae(x, y, step, labyrinth, n):
    labyrinth[x][y] = step

    while labyrinth[x][y] != 'E':
        if (labyrinth[x][y+1] == '.') or (labyrinth[x][y+1] == 'M') or (type(labyrinth[x][y+1]) == int) and (labyrinth[x][y+1] > step):
            findDaWae(x, y+1, step+1, labyrinth, n)
        if (labyrinth[x+1][y] == '.') or (labyrinth[x+1][y] == 'M') or (type(labyrinth[x+1][y]) == int) and (labyrinth[x+1][y] > step):
            findDaWae(x+1, y, step+1, labyrinth, n)
        if (labyrinth[x-1][y] == '.') or (labyrinth[x-1][y] == 'M') or (type(labyrinth[x-1][y]) == int) and (labyrinth[x-1][y] > step):
            findDaWae(x-1, y, step+1, labyrinth, n)
        if (labyrinth[x][y-1] == '.') or (labyrinth[x][y-1] == 'M') or (type(labyrinth[x][y-1]) == int) and (labyrinth[x][y-1] > step):
            findDaWae(x, y-1, step+1, labyrinth, n)    
        return labyrinth                               

def findClosestSchool(labyrinth, min, entersList, clFirst, neiList):
    i = clFirst
    while entersList[i][0] < clFirst: i += 1
    while (i < len(entersList)) and (entersList[i][0] == clFirst):
        if (type(labyrinth[entersList[i][1] + 1][entersList[i][2]]) == int) and (labyrinth[entersList[i][1] + 1][entersList[i][2]] < min):
            min = labyrinth[entersList[i][1] + 1][entersList[i][2]]
            dist = labyrinth[entersList[i][1] + 1][entersList[i][2]] + 2
            closestSch = entersList[i][0]
        if (type(labyrinth[entersList[i][1] - 1][entersList[i][2]]) == int) and (labyrinth[entersList[i][1] - 1][entersList[i][2]] < min):
            min = labyrinth[entersList[i][1] - 1][entersList[i][2]]
            dist = labyrinth[entersList[i][1] - 1][entersList[i][2]] + 2
            closestSch = entersList[i][0]
        if (type(labyrinth[entersList[i][1]][entersList[i][2] + 1]) == int) and (labyrinth[entersList[i][1]][entersList[i][2] + 1] < min):
            min = labyrinth[entersList[i][1]][entersList[i][2] + 1]
            dist = labyrinth[entersList[i][1]][entersList[i][2] + 1] + 2
            closestSch = entersList[i][0]
        if (type(labyrinth[entersList[i][1]][entersList[i][2] - 1]) == int) and (labyrinth[entersList[i][1]][entersList[i][2] - 1] < min):
            min = labyrinth[entersList[i][1]][entersList[i][2] - 1]
            dist = labyrinth[entersList[i][1]][entersList[i][2] - 1] + 2
            closestSch = entersList[i][0]
        i += 1

    for neiSch in neiList:
        i = neiSch
        while entersList[i][0] < neiSch: i += 1
        while (i < len(entersList)) and (entersList[i][0] == neiSch):
            if (type(labyrinth[entersList[i][1] + 1][entersList[i][2]]) == int) and (labyrinth[entersList[i][1] + 1][entersList[i][2]] < min):
                min = labyrinth[entersList[i][1] + 1][entersList[i][2]]
                dist = labyrinth[entersList[i][1] + 1][entersList[i][2]] + 2
                closestSch = entersList[i][0]
            if (type(labyrinth[entersList[i][1] - 1][entersList[i][2]]) == int) and (labyrinth[entersList[i][1] - 1][entersList[i][2]] < min):
                min = labyrinth[entersList[i][1] - 1][entersList[i][2]]
                dist = labyrinth[entersList[i][1] - 1][entersList[i][2]] + 2
                closestSch = entersList[i][0]
            if (type(labyrinth[entersList[i][1]][entersList[i][2] + 1]) == int) and (labyrinth[entersList[i][1]][entersList[i][2] + 1] < min):
                min = labyrinth[entersList[i][1]][entersList[i][2] + 1]
                dist = labyrinth[entersList[i][1]][entersList[i][2] + 1] + 2
                closestSch = entersList[i][0]
            if (type(labyrinth[entersList[i][1]][entersList[i][2] - 1]) == int) and (labyrinth[entersList[i][1]][entersList[i][2] - 1] < min):
                min = labyrinth[entersList[i][1]][entersList[i][2] - 1]
                dist = labyrinth[entersList[i][1]][entersList[i][2] - 1] + 2
                closestSch = entersList[i][0]
            i += 1
    return closestSch, dist


def cityMaking(n, kH, kV):
    city = []*(n+1)
    for i in range(0, (n+1)):
        row = ['X']*(n+1)
        city += [row]
    deltaH = n//kH
    deltaV = n//kV
    i = 0
    while i < n-deltaH:
        i += deltaH
        for j in range(0, n):
            city[i][j] = '.'
    j = 0
    while j < n-deltaV:
        j += deltaV
        for i in range(0, n):
            city[i][j] = '.'
    for i in range(0, n+1): city[i][0] = str(i)
    for j in range(0, n+1): city[0][j] = str(j)

    return city

def schoolMaking(nSchools, city, n):
    schools = []*nSchools
    enters = []
    for i in range(0, nSchools):
        row = [0] * 2
        row[0] = random.randint(1, n-2)
        row[1] = random.randint(1, n-2)
        while not (city[row[0]-1][row[1]] == '.' or city[row[0]][row[1]-1] == '.' or city[row[0]+1][row[1]] == '.' or city[row[0]][row[1]+1] == '.') or\
                (city[row[0]][row[1]] == '.') or (city[row[0]][row[1]] == 'E'):
            row[0] = random.randint(1, n-2)
            row[1] = random.randint(1, n-2)
        schools += [row]
        city[row[0]][row[1]] = 'S'

        rowEnt = [0] * 3
        if city[row[0]-1][row[1]] == '.':
            city[row[0]-1][row[1]] = 'E'
            rowEnt[0] = i
            rowEnt[1] = row[0] - 1
            rowEnt[2] = row[1]
            enters.append(rowEnt)
        rowEnt = [0] * 3
        if city[row[0]+1][row[1]] == '.':
            city[row[0]+1][row[1]] ='E'
            rowEnt[0] = i
            rowEnt[1] = row[0] + 1
            rowEnt[2] = row[1]
            enters.append(rowEnt)
        rowEnt = [0] * 3
        if city[row[0]][row[1]-1] == '.':
            city[row[0]][row[1]-1] ='E'
            rowEnt[0] = i
            rowEnt[1] = row[0]
            rowEnt[2] = row[1] - 1
            enters.append(rowEnt)
        rowEnt = [0] * 3
        if city[row[0]][row[1]+1] == '.':
            city[row[0]][row[1]+1] ='E'
            rowEnt[0] = i
            rowEnt[1] = row[0]
            rowEnt[2] = row[1] + 1
            enters.append(rowEnt)

    return city, schools, enters

def citizenMaking(nCitizens, city, n):
    citizens = []*nCitizens
    for i in range(0, nCitizens):
        row = [0] * 2
        row[0] = random.randint(1, n)
        row[1] = random.randint(1, n)
        while city[row[0]][row[1]] != '.':
            row[0] = random.randint(1, n)
            row[1] = random.randint(1, n)
        citizens += [row]
        city[row[0]][row[1]] = 'M'
    return city, citizens

