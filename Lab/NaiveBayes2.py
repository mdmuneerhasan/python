Yes = 0
No = 0
li = []
Yescount = [0, 0, 0, 0]
Nocount = [0, 0, 0, 0]
ProbY = [0, 0, 0, 0]
ProbN = [0, 0, 0, 0]
with open("data.csv", "r") as md:
    lines = md.readlines()
    xi = []
    for i in lines:
        xi = i.split(",")
        li.append(xi[:-1])
        # print(li)
    features = len(li[0])
    # print(features)
    for i in li:
        for j in i:
            if j == "Yes":
                Yes += 1
            if j == "No":
                No += 1
                # print(Yes)
    # print(No)
    PY = Yes / (Yes + No)
    PN = No / (Yes + No)
    # print(PY)
    # print(PN)
    PredInp = input("Your Outlook,Temp,Humidity,Windy data: ")
    Inpli = PredInp.split(",")
    for i in range(len(lines)):
        for j in range(features - 1):
            if li[i][j].lower() == Inpli[j].lower():
                if li[i][features - 1] == "Yes":
                    Yescount[j] += 1
                if li[i][features - 1] == "No":
                    Yescount[j] += 1
    print(Yescount)
    print(Nocount)
    for i in range(4):
        ProbY[i] = Yescount[i] / Yes
    for i in range(4):
        ProbN[i] = Nocount[i] / No
    PY1 = 1
    PN1 = 1
    for i in ProbY:
        PY1 *= i
    for i in ProbN:
        PN1 *= i
    PY1 *= PY
    PN1 *= PN
    print(PY1,PN1)
    if PY1 > PN1:
        print("Yes, Can Play!")
    else:
        print("No, Can't Play!")
