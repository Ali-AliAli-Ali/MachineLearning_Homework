import random

def reverseString(s): return s[::-1]

def Function(indI, indJ):
    if matrix[indI][0] == matrix[0][indJ]: g = 1
    else: g = -1
    matrix[indI][indJ] = max(matrix[indI-1][indJ-1]+g, matrix[indI-1][indJ]-1, matrix[indI][indJ-1]-1)



s1 = s2 = ''
l1, l2 = int(input()), int(input())
for i in range(l1):
    t = random.choice(['A', 'C', 'G', 'T'])
    s1 += t
for i in range(l2):
    t = random.choice(['A', 'C', 'G', 'T'])
    s2 += t
print(s1)
print(s2)
print('')
s1Res = s2Res = ''


matrix = []
for i in range(0, l2+2):
    row = [0] * (l1+2)
    matrix += [row]

for i in range(2, l2+2):
    matrix[i][0] = s2[i-2]
    matrix[i][1] = -(i-1)
for j in range(2, l1+2):
    matrix[0][j] = s1[j-2]
    matrix[1][j] = -(j-1)

for i in range (2, l2+2):
    for j in range(2, l1+2):
        Function(i, j)

while (i > 1) and (j > 1):
    m = max(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])
    if m == matrix[i-1][j-1]:
        s1Res += matrix[0][j]
        s2Res += matrix[i][0]
        i -= 1
        j -= 1
    elif m == matrix[i-1][j]:
        s1Res += '_'
        s2Res += matrix[i][0]
        i -= 1
    elif m == matrix[i][j-1]:
        s1Res += matrix[0][j]
        s2Res += '_'
        j -= 1
while i > 1:
    s1Res += '_'
    s2Res += matrix[i][0]
    i -= 1
while j > 1:
    s1Res += matrix[0][j]
    s2Res += '_'
    j -= 1


print(reverseString(s1Res))
print(reverseString(s2Res))
# for i in range(0, l2+2):
#     print("")
#     for j in range(0, l1+2):
#         print("{:4s}".format(str(matrix[i][j])), end = "")
