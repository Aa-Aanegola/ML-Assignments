import copy
true = ["R", "G", "R", "G", "G", "R"]


observations = ["G", "R", "G"]

p = {"RR" : 0.9, "GR" : 0.1, "GG" : 0.85, "RG" : 0.15}

b = [1/3, 0, 1/3, 0, 0, 1/3]

ACT = ["RIGHT", "LEFT", "LEFT"]


for pos in range(len(ACT)):
    act = ACT[pos]
    newb = [0 for i in range(len(b))]
    obs = observations[pos]
    for i in range(len(b)):
        ps = obs + true[i]
        prob = p[ps]
        newbt = 0
        for j in range(len(b)):
            if j == i:
                if i == 0 and act == "LEFT":
                    newbt += 0.8 * b[j]
                elif i == 0 and act == "RIGHT":
                    newbt += 0.2 * b[j]
                if i == len(b)-1 and act == "RIGHT":
                    newbt += 0.8 * b[j]
                elif i == len(b)-1 and act == "LEFT":
                    newbt += 0.2 * b[j]
            elif j+1 == i:
                if act == "RIGHT":
                    newbt += 0.8 * b[j]
                elif act == "LEFT":
                    newbt += 0.2 * b[j]
            elif j-1 == i:
                if act == "LEFT":
                    newbt += 0.8 * b[j]
                elif act == "RIGHT":
                    newbt += 0.2 * b[j]
                    
        newb[i] = newbt * prob
    
    su = 0
    for pq in newb:
        su += pq
    for it in range(len(newb)):
        newb[it] /= su
    b = newb
    for bel in b:
        print(bel, end=' ')
    print()
    