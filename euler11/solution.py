file = open("input.txt", 'r')
lines = file.readlines()

allnum = []
for i in lines:
    allnum.append(i.rstrip())
rows = len(lines)


# Splitting and converting data to integer
for i in range(len(allnum)):
    allnum[i] = allnum[i].split(' ')
for i in range(len(allnum)):
    for j in range(len(allnum)):
        allnum[i][j] = int(allnum[i][j])

# Biggest value horizonatally
biggesthor = 0
biggestr = 0
biggestc = 0
for i in range(len(allnum)):
    for j in range(len(allnum[i])-3):
        num = 1
        for k in range(4):
            num *= allnum[i][k+j]
        if num > biggesthor:
            biggesthor = num

# Biggest value vertically
biggestver = 0
for i in range(len(allnum)):
    for j in range(len(allnum[i])-3):
        num = 1
        for k in range(4):
            num *= allnum[j+k][i]
        if num > biggestver:
            biggestver = num

# Biggest value diagonally 1

biggestdia = 0
for i in range(len(allnum) -3):
    for j in range(len(allnum[i])-3):
        num = 1
        for k in range(4):
            num *= allnum[i+k][j+k]
        if num > biggestdia:
            biggestdia = num

# Biggest value diagonally 2

biggestdia2 = 0
for i in range(len(allnum) -3):
    for j in range(3, len(allnum[i])):
        num = 1
        for k in range(0, 4):
            num *= allnum[i+k][j-k]
        if num > biggestdia2:
            biggestdia2 = num

def greatestproduct(a, b, c, d):
    if a > b and a > c and a > d:
        return a
    if b > a and b > c and b > d:
        return b
    if c > a and c > b and c > d:
        return c
    else:
        return d

print(greatestproduct(biggesthor,biggestver,biggestdia,biggestdia2))
