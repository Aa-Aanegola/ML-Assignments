pos = {"W" : 0, 
       "N" : 1, 
       "E" : 2, 
       "S" : 3,
       "C" : 4}

mat = {"0" : 0, 
       "1" : 1}

arrows = {"0" : 0,
          "1" : 1,
          "2" : 2,
          "3" : 3}

MM = {"D" : 0, 
      "R" : 1}

health = {"0" : 0, 
          "25" : 1, 
          "50" : 2,
          "75" : 3, 
          "100" : 4}

action = {"UP" : 0,
          "LEFT" : 1,
          "DOWN" : 2, 
          "RIGHT" : 3, 
          "STAY" : 4, 
          "SHOOT" : 5,
          "HIT" : 6, 
          "CRAFT" : 7, 
          "GATHER" : 8, 
          "NONE" : 9}

value = []
for i in range(len(pos)):
    dim0 = []
    for j in range(len(mat)):
        dim1 = []
        for k in range(len(arrows)):
            dim2 = []
            for l in range(len(MM)):
                dim3 = []
                for m in range(len(health)):
                    dim4 = []
                    for n in range(len(action)):
                        dim4.append(0)
                    dim3.append(dim4)
                dim2.append(dim3)
            dim1.append(dim2)
        dim0.append(dim1)
    value.append(dim0)

# Returns a boolean that indicates whether the action is possible given the state
def actionPossible(pos, mat, arw, MM, hel, act):
    if health == 0 and act != "NONE":
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
        if pos == "N" and mat != "0" and arw != "3":
            return True 
        return False
    if act == "GATHER":
        if pos == "S" and mat != "2":
            return True
    if act == "NONE":
        if health == "0":
            return True
        return False 

# Returns a list of state dictionaries with the probability and the tuple of the state
def take_action(pos, mat, arw, MM, hel, act):
    ret = []
    if act == "UP":
        if pos == "C":
            ret.append({0.85 : ("N", mat, arw, MM, hel)})
            ret.append({0.15 : ("E", mat, arw, MM, hel)})
        if pos == "S":
            ret.append({0.85 : ("C", mat, arw, MM, hel)})
            ret.append({0.15 : ("E", mat, arw, MM, hel)})
    if act == "DOWN":
        if pos == "C":
            ret.append({0.85 : ("S", mat, arw, MM, hel)})
            ret.append({0.15 : ("E", mat, arw, MM, hel)})
        if pos == "N":
            ret.append({0.85 : ("C", mat, arw, MM, hel)})
            ret.append({0.15 : ("E", mat, arw, MM, hel)})
    if act == "LEFT":
        if pos == "C":
            ret.append({0.85 : ("W", mat, arw, MM, hel)})
            ret.append({0.15 : ("E", mat, arw, MM, hel)})
        if pos == "E":
            ret.append({1.00 : ("C", mat, arw, MM, hel)})
    if act == "RIGHT":
        if pos == "C":
            ret.append({1.00 : ("E", mat, arw, MM, hel)})
        if pos == "W":
            ret.append({1.00 : ("C", mat, arw, MM, hel)})
    if act == "STAY":
        if pos == "C":
            ret.append({0.85 : ("C", mat, arw, MM, hel)})
            ret.append({0.15 : ("E", mat, arw, MM, hel)})
        if pos == "N":
            ret.append({0.85 : ("N", mat, arw, MM, hel)})
            ret.append({0.15 : ("E", mat, arw, MM, hel)})
        if pos == "S":
            ret.append({0.85 : ("S", mat, arw, MM, hel)})
            ret.append({0.15 : ("E", mat, arw, MM, hel)})
        if pos == "W":
            ret.append({1.00 : ("W", mat, arw, MM, hel)})
        if pos == "E":
            ret.append({1.00 : ("E", mat, arw, MM, hel)})
    if act == "SHOOT":
        if pos == "C":
            ret.append({0.50 : (pos, mat, str(int(arw)-1)), MM, str(int(hel)-25)})
            ret.append({0.50 : (pos, mat, str(int(arw)-1), MM, hel)})
        if pos == "E":
            ret.append({0.90 : (pos, mat, str(int(arw)-1), MM, str(int(hel)-25))})
            ret.append({0.10 : (pos, mat, str(int(arw)-1), MM, hel)})
        if pos == "W":
            ret.append({0.25 : (pos, mat, str(int(arw)-1), MM, str(int(hel)-25))})
            ret.append({0.75 : (pos, mat, str(int(arw)-1), MM, hel)})
    if act == "HIT":
        if pos == "C":
            ret.append({0.10 : (pos, mat, arw, MM, str(max(0, int(hel-50))))})
            ret.append({0.90 : (pos, mat, arw, MM, hel)})
        if pos == "E":
            ret.append({0.20 : (pos, mat, arw, MM, str(max(0, int(hel-50))))})
            ret.append({0.80 : (pos, mat, arw, MM, hel)})
    if act == "CRAFT":
        ret.append({0.50 : (pos, str(int(mat)-1), str(min(3, int(arw)+1)), MM, hel)})
        ret.append({0.35 : (pos, str(int(mat)-1), str(min(3, int(arw)+2)), MM, hel)})
        ret.append({0.15 : (pos, str(int(mat)-1), str(min(3, int(arw)+3)), MM, hel)})
    if act == "GATHER":
        ret.append({0.75 : (pos, str(int(mat)+1), arw, MM, hel)})
        ret.append({0.25 : (pos, mat, arw, MM, hel)})
    return ret
