import numpy as np
import cvxpy as cp
import json

POS = {
    "W" : 0, 
    "N" : 1, 
    "E" : 2, 
    "S" : 3,
    "C" : 4
}

MAT = {
    "0" : 0, 
    "1" : 1, 
    "2" : 2
}

ARW = {
    "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3
}

MM = {
    "D" : 0, 
    "R" : 1
}

HEL = {
    "0" : 0, 
    "25" : 1, 
    "50" : 2,
    "75" : 3, 
    "100" : 4
}

ACT = {
    "UP" : 0,
    "LEFT" : 1,
    "DOWN" : 2, 
    "RIGHT" : 3, 
    "STAY" : 4, 
    "SHOOT" : 5,
    "HIT" : 6, 
    "CRAFT" : 7, 
    "GATHER" : 8, 
    "NONE" : 9
}

rPOS = {
    0 : "W", 
    1 : "N", 
    2 : "E",
    3 : "S", 
    4 : "C"
}

rMAT = {
    0  :"0",
    1 : "1", 
    2 : "2"
}

rARW = {
    0 : "0", 
    1 : "1",
    2 : "2",
    3 : "3"
}

rMM = {
    0 : "D",
    1 : "R"
}

rHEL = {
    0 : "0", 
    1 : "25", 
    2 : "50", 
    3 : "75", 
    4 : "100"
}

rACT = {
    0 : "UP",
    1 :"LEFT",
    2 : "DOWN", 
    3 : "RIGHT", 
    4 : "STAY", 
    5 : "SHOOT",
    6 : "HIT", 
    7 : "CRAFT", 
    8 : "GATHER", 
    9 : "NONE"
}

def getIndex(pos, mat, arw, mm, hel):
    return 120*POS[pos]+40*MAT[mat]+10*ARW[arw]+5*MM[mm]+HEL[hel]

def getState(ind):
    pos = ind//120
    ind %= 120
    mat = ind//40
    ind %= 40
    arw = ind//10
    ind %= 10
    mm = ind//5
    ind = ind % 5
    hel = ind
    return (rPOS[pos], rMAT[mat], rARW[arw], rMM[mm], rHEL[hel])

def actionPossible(pos, mat, arw, mm, hel, act):
    if hel == "0" and act != "NONE":
        return False
    if act == "UP":
        if pos == "C" or pos == "S":
            return True
        return False
    if act == "DOWN":
        if pos == "C" or pos == "N":
            return True
        return False
    if act == "LEFT":
        if pos == "C" or pos == "E":
            return True 
        return False
    if act == "RIGHT":
        if pos == "C" or pos == "W":
            return True
        return False
    if act == "STAY":
        return True
    if act == "SHOOT":
        if arw != "0" and pos != "N" and pos != "S":
            return True
        return False
    if act == "HIT":
        if pos == "C" or pos == "E":
            return True
        return False
    if act == "CRAFT":
        if pos == "N" and mat != "0":
            return True 
        return False
    if act == "GATHER":
        if pos == "S":
            return True
    if act == "NONE":
        if hel == "0":
            return True
        return False

def takeAction(pos, mat, arw, mm, hel, act):
    ret = []
    if act == "UP":
        if pos == "C":
            ret.append({0.85 : ("N", mat, arw, mm, hel)})
            ret.append({0.15 : ("E", mat, arw, mm, hel)})
        if pos == "S":
            ret.append({0.85 : ("C", mat, arw, mm, hel)})
            ret.append({0.15 : ("E", mat, arw, mm, hel)})
    if act == "DOWN":
        if pos == "C":
            ret.append({0.85 : ("S", mat, arw, mm, hel)})
            ret.append({0.15 : ("E", mat, arw, mm, hel)})
        if pos == "N":
            ret.append({0.85 : ("C", mat, arw, mm, hel)})
            ret.append({0.15 : ("E", mat, arw, mm, hel)})
    if act == "LEFT":
        if pos == "C":
            ret.append({0.85 : ("W", mat, arw, mm, hel)})
            ret.append({0.15 : ("E", mat, arw, mm, hel)})
        if pos == "E":
            ret.append({1.00 : ("C", mat, arw, mm, hel)})
    if act == "RIGHT":
        if pos == "C":
            ret.append({1.00 : ("E", mat, arw, mm, hel)})
        if pos == "W":
            ret.append({1.00 : ("C", mat, arw, mm, hel)})
    if act == "STAY":
        if pos == "C":
            ret.append({0.85 : ("C", mat, arw, mm, hel)})
            ret.append({0.15 : ("E", mat, arw, mm, hel)})
        if pos == "N":
            ret.append({0.85 : ("N", mat, arw, mm, hel)})
            ret.append({0.15 : ("E", mat, arw, mm, hel)})
        if pos == "S":
            ret.append({0.85 : ("S", mat, arw, mm, hel)})
            ret.append({0.15 : ("E", mat, arw, mm, hel)})
        if pos == "W":
            ret.append({1.00 : ("W", mat, arw, mm, hel)})
        if pos == "E":
            ret.append({1.00 : ("E", mat, arw, mm, hel)})
    if act == "SHOOT":
        if pos == "C":
            ret.append({0.50 : (pos, mat, str(int(arw)-1), mm, str(int(hel)-25))})
            ret.append({0.50 : (pos, mat, str(int(arw)-1), mm, hel)})
        if pos == "E":
            ret.append({0.90 : (pos, mat, str(int(arw)-1), mm, str(int(hel)-25))})
            ret.append({0.10 : (pos, mat, str(int(arw)-1), mm, hel)})
        if pos == "W":
            ret.append({0.25 : (pos, mat, str(int(arw)-1), mm, str(int(hel)-25))})
            ret.append({0.75 : (pos, mat, str(int(arw)-1), mm, hel)})
    if act == "HIT":
        if pos == "C":
            ret.append({0.10 : (pos, mat, arw, mm, str(max(0, int(hel)-50)))})
            ret.append({0.90 : (pos, mat, arw, mm, hel)})
        if pos == "E":
            ret.append({0.20 : (pos, mat, arw, mm, str(max(0, int(hel)-50)))})
            ret.append({0.80 : (pos, mat, arw, mm, hel)})
    if act == "CRAFT":
        ret.append({0.50 : (pos, str(int(mat)-1), str(min(3, int(arw)+1)), mm, hel)})
        ret.append({0.35 : (pos, str(int(mat)-1), str(min(3, int(arw)+2)), mm, hel)})
        ret.append({0.15 : (pos, str(int(mat)-1), str(min(3, int(arw)+3)), mm, hel)})
    if act == "GATHER":
        ret.append({0.75 : (pos, str(min(2, int(mat)+1)), arw, mm, hel)})
        ret.append({0.25 : (pos, mat, arw, mm, hel)})
    return ret


stateActions = {}
rstateActions = {}

ind = 0
for i in range(600):
    for act in ACT:
        pos, mat, arw, mm, hel = getState(i)
        if actionPossible(pos, mat, arw, mm, hel, act):
            stateActions[(pos, mat, arw, mm, hel, act)] = ind
            rstateActions[ind] = (pos, mat, arw, mm, hel, act)
            ind += 1

for i in stateActions:
    print(i)

x = cp.Variable(shape=(len(stateActions), 1), name="x")
A = [[0 for i in range(len(stateActions))] for j in range(600)]
alpha = [0 for i in range(600)]
R = [0 for i in range(len(stateActions))]

mmReach = ["C", "E"]

gamma = 0.999
stepCost = -20
atkRew = -40

np.set_printoptions(threshold=np.inf)

for i in range(600):
    pos, mat, arw, mm, hel = getState(i)
    alpha[i] = 1.0/600

for i in range(len(stateActions)):
    pos, mat, arw, mm, hel, act = rstateActions[i]
    ret = takeAction(pos, mat, arw, mm, hel, act)
    if hel == "0":
        if act == "NONE":
            A[getIndex(pos, mat, arw, mm, hel)][i] += 1
        continue
    
    if mm == "D":
        for it in ret:
            prob = list(it.keys())[0]
            dat = it[prob]
            if getIndex(dat[0], dat[1], dat[2], dat[3], dat[4]) == getIndex(pos, mat, arw, mm, hel):
                A[getIndex(dat[0], dat[1], dat[2], "R", dat[4])][i] -= prob*0.2
                A[getIndex(pos, mat, arw, mm, hel)][i] += prob*0.2
            else:
                A[getIndex(dat[0], dat[1], dat[2], dat[3], dat[4])][i] -= prob*0.8
                A[getIndex(dat[0], dat[1], dat[2], "R", dat[4])][i] -= prob*0.2
                A[getIndex(pos, mat, arw, mm, hel)][i] += prob
            R[i] += prob*stepCost
    else:
        if pos in mmReach:
            R[i] += 0.5*atkRew
        for it in ret:
            prob = list(it.keys())[0]
            dat = it[prob]
            if getIndex(dat[0], dat[1], dat[2], dat[3], dat[4]) == getIndex(pos, mat, arw, mm, hel):
                if pos in mmReach:
                    A[getIndex(pos, mat, "0", "D", str(min(100, int(hel)+25)))][i] -= prob*0.5
                    A[getIndex(pos, mat, arw, mm, hel)][i] += prob*0.5

                else:
                    A[getIndex(dat[0], dat[1], dat[2], "D", dat[4])][i] -= prob*0.5
                    A[getIndex(pos, mat, arw, mm, hel)][i] += prob*0.5
                R[i] += prob*stepCost

            else:
                A[getIndex(dat[0], dat[1], dat[2], dat[3], dat[4])][i] -= prob*0.5
                A[getIndex(pos, mat, arw, mm, hel)][i] += prob*0.5
                if pos in mmReach:
                    A[getIndex(pos, mat, "0", "D", str(min(100, int(hel)+25)))][i] -= prob*0.5
                    A[getIndex(pos, mat, arw, mm, hel)][i] += prob*0.5
                else:
                    A[getIndex(dat[0], dat[1], dat[2], "D", dat[4])][i] -= prob*0.5
                    A[getIndex(pos, mat, arw, mm, hel)][i] += prob*0.5
                R[i] += prob*stepCost
           
A = np.array(A)
R = np.array(R)

alpha = np.array(alpha)
alpha = alpha.reshape((600, 1))


constraints = [cp.matmul(A, x) == alpha, x >= 0.0]
objective = cp.Maximize(cp.matmul(R, x))
problem = cp.Problem(objective, constraints)

solution = problem.solve()

# print(solution)
# print(x.value)

policy = []

for i in range(600):
    mx = -100000
    optAct = "NONE"
    for j in range(10):
        act = rACT[j]
        pos, mat, arw, mm, hel = getState(i)
        if not actionPossible(pos, mat, arw, mm, hel, act):
            continue
        
        ind = stateActions[(pos, mat, arw, mm, hel, act)]
        
        # print(getState(i), act, x.value[ind], R[ind])
        
        if x.value[ind]*R[ind] > mx:
            optAct = act
            mx = x.value[ind]*R[ind]
    policy.append([getState(i), optAct])
    print("Optimum: ", getState(i), optAct, x.value[ind], R[ind])
    # print()
    
dump = {}

dump["a"] = A.tolist()
dump["r"] = R.tolist()
dump["x"] = x.value.tolist()
dump["alpha"] = alpha.tolist()
dump["policy"] = policy
dump["objective"] = solution

f = open("part_3_output.json", "w+");
json.dump(dump, f)