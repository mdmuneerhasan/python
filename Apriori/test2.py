min_support = 2
min_confidence = .5

dataset = [{'id': 'T1', 'items': ['i1', 'i2', 'i5']},
           {'id': 'T2', 'items': ['i2', 'i4']},
           {'id': 'T3', 'items': ['i2', 'i3']},
           {'id': 'T4', 'items': ['i1', 'i2', 'i4']},
           {'id': 'T5', 'items': ['i1', 'i3']},
           {'id': 'T6', 'items': ['i2', 'i3']},
           {'id': 'T7', 'items': ['i1', 'i3']},
           {'id': 'T8', 'items': ['i1', 'i2', 'i3', 'i5']},
           {'id': 'T9', 'items': ['i1', 'i2', 'i3']}, ]

frequencyTable = {}

customDataframe = {}

{1,2,4}


# convert list of items into hashed string
def hashed(processed):
    x = ""
    processed.sort()
    if len(processed) == 0:
        return x
    for i in range(0, len(processed)):
        if i != 0:
            x = x + ','
        x = x + processed[i]
    return x

# convert string into list of items
def deHash(params):
    params = str(params).split(',', -1)
    return params


# create all possible set by combining two tables
def deHashedTable(param: str, param1: str):
    sets = set()
    param1 = deHash(param1)
    param = deHash(param)
    for x in param1:
        temp = list(param)
        temp.append(x)
        y = hashed(temp)
        sets.add(y)
    return sets


def deHashedList(param: str, param1: str):
    param1 = deHash(param1)
    param = deHash(param)

    for x in param1:
        if x not in param:
            param.append(x)
    return param


# create a dataframe(type storage without using library) which store all possible frequencies
def addToDataframe(processed, unprocessed):
    if len(unprocessed) == 0:
        key = hashed(processed)
        if key in customDataframe.keys():
            customDataframe[key] += 1
        else:
            customDataframe[key] = 1
        return
    x = unprocessed[0]
    unprocessed.remove(x)
    addToDataframe(list(processed), list(unprocessed))
    processed.append(x)
    addToDataframe(list(processed), list(unprocessed))


# convert dataframe in to table
def findFrequencyTable(dataset):

    for i in range(len(dataset)):
        items = dataset[i]['items']
        addToDataframe(list(), list(items))

        for x in items:
            if x in frequencyTable.keys():
                frequencyTable[x] += 1
            else:
                frequencyTable[x] = 1


# convert frequency table by combining previous table and form a new table
def possibleResolving(min_support):
    temp = {}
    global frequencyTable
    for i in frequencyTable:
        for j in frequencyTable:
            if i != j:
                items = deHashedTable(i, j)
                for x in items:
                    if x in customDataframe.keys():
                        temp[x] = customDataframe[x]
    frequencyTable = temp
    pruning(min_support)
    if len(frequencyTable) == 0:
        return False
    else:
        return True


def pruning(min_support):
    delete = []
    for x in frequencyTable.keys():
        if frequencyTable[x] < min_support:
            delete.append(x)

    for x in delete:
        del frequencyTable[x]


def custom_print(frequencyTable):
    for x in frequencyTable.keys():
        print(x + " : " + str(frequencyTable[x]))
    print()


def findFrequentSet(dataset, min_support):
    findFrequencyTable(dataset);
    pruning(min_support)
    custom_print(frequencyTable)
    frequentSet = {}
    while possibleResolving(min_support):
        custom_print(frequencyTable)
        frequentSet = frequencyTable

    return frequentSet


def generateRules(key):
    key = deHash(key)
    generatedRules = {}
    for i in range(1, 2 ** len(key) - 1):
        p1 = []
        p2 = []
        for j in range(len(key)):
            if ((i >> j) & 1) == 1:
                p1.append(key[j])
            else:
                p2.append(key[j])
        generatedRules[hashed(p1)] = hashed(p2)
    return generatedRules


def findAssociationRules(frequentSet):
    rules = {}
    for key in frequentSet.keys():
        generatedRules = generateRules(key)
        for x in generatedRules.keys():
            y = hashed(deHashedList(x, generatedRules[x]));
            z = x + " -> " + generatedRules[x]
            confidence=customDataframe[y]/customDataframe[x];

            if confidence >= min_confidence:
                rules[z]=confidence
    return rules


frequentSet = findFrequentSet(dataset, min_support)

rules = findAssociationRules(frequentSet)
print("Association Rules")
custom_print(rules)



