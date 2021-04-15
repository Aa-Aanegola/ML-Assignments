agent = [(0, 0), (1, 3)]
prob = {(0, 0) : 0.4, (1, 3) : 0.6}
target = [(0, 1), (0, 2), (1, 1), (1, 2)]

probs = [0, 0, 0, 0, 0, 0]
for aR, aC in agent:
    for tR, tC in target:
        pr = prob[(aR, aC)] * 0.25
        if aR == tR and aC == tC:
            probs[0] += pr
        elif aR == tR and aC+1 == tC:
            probs[1] += pr
        elif aR+1 == tR and aC == tC:
            probs[2] += pr
        elif aR == tR and aC-1 == tC:
            probs[3] += pr
        elif aR == tR-1 and aC == tC:
            probs[4] += pr
        else:
            probs[5] += pr

print(probs)