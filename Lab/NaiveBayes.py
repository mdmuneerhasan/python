datafile = open("data.csv", "r").read()

data = []
options = []
yesCount = {}
noCount = {}
yes = 0
no = 0
j = 0
for x in datafile.split('\n'):
    data.append(x.split(','))
    i = 0
    for y in x.split(','):
        if j == 0:
            options.append(set())
        options[i].add(y)
        if y.lower() == 'yes':
            yes = yes + 1
        if y.lower() == 'no':
            no = no + 1
        i = i + 1
    j = j + 1

row = len(data) - 1

if row == 0:
    print("no data available")
    exit()

col = len(data[0]) - 1

for i in range(row):
    for j in range(col - 1):
        if 'yes' in data[i] or 'Yes' in data[i]:
            if data[i][j].lower() in yesCount.keys():
                yesCount[data[i][j].lower()] = yesCount[data[i][j].lower()] + 1
            else:
                yesCount[data[i][j].lower()] = 1

        else:
            if data[i][j].lower() in noCount.keys():
                noCount[data[i][j].lower()] = noCount[data[i][j].lower()] + 1
            else:
                noCount[data[i][j].lower()] = 1

while True:
    condition = []
    j = 0
    i = 0
    yesProbability = 1
    noProbability = 1
    while i < col - 1:
        print("chose from : ", end="")
        print(options[i])
        j = j + 1
        c = input()
        c = c.strip().lower()

        if c in yesCount.keys() or c in noCount.keys():
            i += 1
            condition.append(c)
            if c in yesCount.keys():
                yesProbability = yesProbability * yesCount[c] / yes
            if c in noCount.keys():
                noProbability = noProbability * noCount[c] / no
        else:
            print("try again invalid key")

    yesProbability = yesProbability * yes / (yes + no)
    noProbability = noProbability * no / (yes + no)

    print(yesProbability,noProbability)
    print("p(yes|", end="")
    for x in condition:
        print(x, end=',')
    print(")", end='=')
    print(yesProbability / (noProbability + yesProbability))
    print("p(no|", end="")
    for x in condition:
        print(x, end=',')
    print(")", end='=')
    print(noProbability / (noProbability + yesProbability))
    if yesProbability > noProbability:
        print("yes can play")
    elif noProbability > yesProbability:
        print("probably not playing")
    else:
        print("equal chances")

    option = input("\nexit..?y/n")
    if option.lower() == 'y':
        exit()
