data = [
    ['T100', ['I1', 'I2', 'I5']],
    ['T200', ['I2', 'I4']],
    ['T300', ['I2', 'I3']],
    ['T400', ['I1', 'I2', 'I4']],
    ['T500', ['I1', 'I3']],
    ['T600', ['I2', 'I3']],
    ['T700', ['I1', 'I3']],
    ['T800', ['I1', 'I2', 'I3', 'I5']],
    ['T900', ['I1', 'I2', 'I3']]
]

table = {}

fCount={}

ms=2
cf=0.5


def count(param, param1):
    if len(param) == 0:
        if frozenset(param1) in fCount.keys():
            fCount[frozenset(param1)]+=1
        else:
            fCount[frozenset(param1)]=1
        return

    ele = param[0]
    param.remove(ele)

    count(list(param),list(param1))

    param1.append(ele)
    count(list(param),list(param1))




for i in data:
    count(list(i[1]),list())

    for j in i[1]:
        k=frozenset({j})
        if k in table.keys():
            table[k] += 1
        else:
            table[k] = 1



def printMy(table):
    for i in table.keys():
        print(i,end=" : ")
        print(table[i])


def resolve(table):
    newTable={}
    for x in table:
        for y in table:
            k=frozenset(set(x).union(set(y)))

            if k in fCount.keys() and y != x and fCount[k]>=ms:
                newTable[k]=fCount[k]
    print()
    printMy(newTable)
    if len(newTable) >0:
        return resolve(newTable)
    else:
        return table


def allCombination(param):
    ans = []

    for x in range(1, 2 ** len(param) -1):
        left = set()
        right = set()
        for i in range(len(param)):
            if (x >> i) & 1:
                left.add(param[i])
            else:
                right.add(param[i])
        ans.append([left, right])
    return ans


def findRules(table):
    for x in table:
        combination = allCombination(list(x))
        for rules in combination:
            conf = fCount[frozenset(rules[0].union(rules[1]))] / fCount[frozenset(rules[0])]
            if (conf >= cf):
                print(list(rules[0]), end=" => ")
                print(list(rules[1]), end=" : ")
                print(conf*100 , end=" % \n")
        print()
    pass


printMy(table)
table=resolve(table)

print("Association rules")

findRules(table)



