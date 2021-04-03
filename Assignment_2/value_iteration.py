import copy
from math import inf
import random

POS = {"W" : 0, 
       "N" : 1, 
       "E" : 2, 
       "S" : 3,
       "C" : 4}

MAT = {"0" : 0, 
       "1" : 1, 
       "2" : 2}

ARW = {"0" : 0,
          "1" : 1,
          "2" : 2,
          "3" : 3}

MM = {"D" : 0, 
      "R" : 1}

HEL = {"0" : 0, 
          "25" : 1, 
          "50" : 2,
          "75" : 3, 
          "100" : 4}

ACT = {"UP" : 0,
          "LEFT" : 1,
          "DOWN" : 2, 
          "RIGHT" : 3, 
          "STAY" : 4, 
          "SHOOT" : 5,
          "HIT" : 6, 
          "CRAFT" : 7, 
          "GATHER" : 8, 
          "NONE" : 9}

val = []
for i in range(len(POS)):
    dim0 = []
    for j in range(len(MAT)):
        dim1 = []
        for k in range(len(ARW)):
            dim2 = []
            for l in range(len(MM)):
                dim3 = []
                for m in range(len(HEL)):
                    dim3.append(0)
                dim2.append(dim3)
            dim1.append(dim2)
        dim0.append(dim1)
    val.append(dim0)

# Returns a boolean that indicates whether the action is possible given the state
def actionPossible(pos, mat, arw, mm, hel, act):
    if hel == 0 and act != "NONE":
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

# Returns a list of state dictionaries with the probability and the tuple of the state
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

def sim(actList):
    if len(actList) == 1:
        return actList[0][list(actList[0].keys())[0]]
    elif len(actList) == 2:
        if random.uniform(0, 1) < list(actList[0].keys())[0]:
            return actList[0][list(actList[0].keys())[0]]
        else:
            return actList[1][list(actList[1].keys())[0]]
    else:
        prob = random.uniform(0, 1)
        if  prob < list(actList[0].keys())[0]:
            return actList[0][list(actList[0].keys())[0]]
        elif prob < list(actList[0].keys())[0] + list(actList[1].keys())[0]:
            return actList[1][list(actList[1].keys())[0]]
        else:
            return actList[2][list(actList[2].keys())[0]]

mmReach = ["C", "E"]

bellmanError = 0.001
stepCost = -1
atkRew = -40
gamma = 0.999
finalRew = 50
delta = inf
j = 0

f = open('temp.txt', 'w+')


while delta > bellmanError:
    newVal = copy.deepcopy(val)
    
    print(f"iteration={j}", file=f)
    j += 1
    
    delta = 0
    optAct = "NONE"
    for pos in POS.keys():
        for mat in MAT.keys():
            for arw in ARW.keys():
                for mm in MM.keys():
                    for hel in HEL.keys():
                        if hel == "0":
                            newVal[POS[pos]][MAT[mat]][ARW[arw]][MM[mm]][HEL[hel]] = 0
                            print(f"({pos},{mat},{arw},{mm},{hel}):NONE=[0.000]", file=f)
                            continue
                        mx = -inf
                        for act in ACT.keys():
                            if not actionPossible(pos, mat, arw, mm, hel, act):
                                continue
                            actVal = 0
                            if mm == "D":
                                ret = takeAction(pos, mat, arw, mm, hel, act)
                                for i in ret:
                                    prob = list(i.keys())[0]
                                    dat = i[prob]
                                    if dat[4] == "0":
                                        actVal += 0.8*prob*(finalRew + stepCost + gamma*val[POS[dat[0]]][MAT[dat[1]]][ARW[dat[2]]][MM[dat[3]]][HEL[dat[4]]])
                                        actVal += 0.2*prob*(finalRew + stepCost + gamma*val[POS[dat[0]]][MAT[dat[1]]][ARW[dat[2]]][MM["R"]][HEL[dat[4]]])
                                    else:
                                        actVal += 0.8*prob*(stepCost + gamma*val[POS[dat[0]]][MAT[dat[1]]][ARW[dat[2]]][MM[dat[3]]][HEL[dat[4]]])
                                        actVal += 0.2*prob*(stepCost + gamma*val[POS[dat[0]]][MAT[dat[1]]][ARW[dat[2]]][MM["R"]][HEL[dat[4]]])
                            else:
                                ret = takeAction(pos, mat, arw, mm, hel, act)
                                for i in ret:
                                    prob = list(i.keys())[0]
                                    dat = i[prob]
                                    if pos in mmReach:
                                        actVal += 0.5*prob*(stepCost + atkRew + gamma*val[POS[pos]][MAT[mat]][ARW["0"]][MM["D"]][HEL[str(min(100, int(hel)+25))]])
                                        if dat[4] == "0":
                                            actVal += 0.5*prob*(finalRew + stepCost + gamma*val[POS[dat[0]]][MAT[dat[1]]][ARW[dat[2]]][MM[dat[3]]][HEL[dat[4]]])
                                        else:
                                            actVal += 0.5*prob*(stepCost + gamma*val[POS[dat[0]]][MAT[dat[1]]][ARW[dat[2]]][MM[dat[3]]][HEL[dat[4]]])
                                    else:
                                        if dat[4] == "0":
                                            actVal += 0.5*prob*(finalRew + stepCost + gamma*val[POS[dat[0]]][MAT[dat[1]]][ARW[dat[2]]][MM["D"]][HEL[dat[4]]])
                                            actVal += 0.5*prob*(finalRew + stepCost + gamma*val[POS[dat[0]]][MAT[dat[1]]][ARW[dat[2]]][MM[dat[3]]][HEL[dat[4]]])
                                        else:
                                            actVal += 0.5*prob*(stepCost + gamma*val[POS[dat[0]]][MAT[dat[1]]][ARW[dat[2]]][MM["D"]][HEL[dat[4]]])
                                            actVal += 0.5*prob*(stepCost + gamma*val[POS[dat[0]]][MAT[dat[1]]][ARW[dat[2]]][MM[dat[3]]][HEL[dat[4]]])
                            if actVal > mx:
                                mx = actVal
                                optAct = act
                        newVal[POS[pos]][MAT[mat]][ARW[arw]][MM[mm]][HEL[hel]] = mx
                        print(f"({pos},{mat},{arw},{mm},{hel}):{optAct}=[{mx:.3f}]", file=f)
                        
                        delta = max(delta, abs(mx - val[POS[pos]][MAT[mat]][ARW[arw]][MM[mm]][HEL[hel]]))
    val = copy.deepcopy(newVal)
    

# pos = "C"
# mat = "0"
# arw = "2"
# mm = "R"
# hel = "75"
# score = 0

# while hel != "0":
#     optAct = "NONE"
#     mx = -inf
#     if mm == "D" and random.uniform(0, 1) < 0.2:
#         mm = "R"
#     elif mm == "R" and random.uniform(0, 1) < 0.5:
#         mm = "D"
#         if pos in mmReach:
#             arw = "0"
#             hel = str(min(int(hel)+25, 100))
#             score += atkRew + stepCost
#             print(f"<MM Attacked> STATE=({pos}, {mat}, {arw}, {mm}, {hel}) : ACTION INCAPACITATED : SCORE={score}", file=f)
#         else:
#             print(f"<MM Missed> STATE=({pos}, {mat}, {arw}, {mm}, {hel}) : ACTION VIABLE : SCORE={score}", file=f)
        
#     for act in ACT.keys():
#         if not actionPossible(pos, mat, arw, mm, hel, act):
#             continue
        
#         ret = takeAction(pos, mat, arw, mm, hel, act)
#         expUtl = 0
#         for it in ret:
#             prob = list(it.keys())[0]
#             dat = it[prob]
#             expUtl += prob * val[POS[dat[0]]][MAT[dat[1]]][ARW[dat[2]]][MM[dat[3]]][HEL[dat[4]]]
#         if expUtl > mx:
#             optAct = act
#             mx = expUtl
    
#     ret = takeAction(pos, mat, arw, mm, hel, optAct)
#     nxtState = sim(ret)
#     score += stepCost
#     print(f"STATE=({pos}, {mat}, {arw}, {mm}, {hel}) : ACTION {optAct} : NEW STATE=({nxtState}) : SCORE={score}", file=f)
#     pos, mat, arw, mm, hel = nxtState


# score += finalRew
# print(f"<MM Defeated> STATE=({pos}, {mat}, {arw}, {mm}, {hel}) : ACTION NONE : SCORE={score}", file=f)