def reverseString(s): return s[::-1]

s1 = input()
s2 = input()
sRes = ''

matrix = []
for i in range(0, len(s2)+1):
    row = [0] * (len(s1)+1)
    matrix += [row]
matrixSigns = []
for i in range(0, len(s2)+1):
    row = [False] * (len(s1)+1)
    matrixSigns += [row]

for i in range(0, len(s2)+1): matrix[i][0] = 0
for j in range(0, len(s1)+1): matrix[0][j] = 0

for i in range(1, len(s2)+1):
    for j in range(1, len(s1)+1):
        if s2[i-1] == s1[j-1]:
            matrix[i][j] = matrix[i-1][j-1]+1
            matrixSigns[i][j] = True
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

while (i >= 0) and (j >= 0):
    if matrixSigns[i][j]:
        sRes += s1[j-1]
        i -= 1
        j -= 1
    elif matrix[i-1][j] > matrix[i][j-1]:
        i -= 1
    else: j -= 1

print(reverseString(sRes))
for i in range(1, len(s2)+1): matrix[i][0] = s2[i-1]
for j in range(1, len(s1)+1): matrix[0][j] = s1[j-1]
for i in range(0, len(s2)+1):
    print("")
    for j in range(0, len(s1)+1):
        print("{:4s}".format(str(matrix[i][j])), end = "")
print('')
for i in range(0, len(s2)+1):
    print("")
    for j in range(0, len(s1)+1):
        print("{:4s}".format(str(int(matrixSigns[i][j]))), end = "")