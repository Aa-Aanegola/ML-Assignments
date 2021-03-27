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