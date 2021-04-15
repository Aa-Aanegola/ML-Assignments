import sys

ACTIONS = ["STAY", "UP", "DOWN", "LEFT", "RIGHT"]


def main():
    print("discount : 0.5")
    print("values : reward")
    print("states : ", end='')
    for agentRow in range(2):
        for agentCol in range(4):
            for targetRow in range(2):
                for targetCol in range(4):
                    for call in range(2):
                        print(f"S{agentRow}{agentCol}{targetRow}{targetCol}{call} ", end='')
    print()
    print("actions : STAY UP DOWN LEFT RIGHT")
    print("observations : O1 O2 O3 O4 O5 O6")
    print()
    print("start : ")
    num = 0
    for agentRow in range(2):
        for agentCol in range(4):
            for targetRow in range(2):
                for targetCol in range(4):
                    for call in range(2):
                        if agentRow != 1 or agentCol != 1 or call == 1:
                            continue
                        if agentRow == targetRow and agentCol == targetCol:
                            num += 1
                            continue
                        if agentRow == targetRow+1 and agentCol == targetCol:
                            num += 1
                            continue
                        if agentRow == targetRow-1 and agentCol == targetCol:
                            num += 1
                            continue
                        if agentRow == targetRow and agentCol == targetCol+1:
                            num += 1
                            continue
                        if agentRow == targetRow and agentCol == targetCol-1:
                            num += 1
                            continue

    for agentRow in range(2):
        for agentCol in range(4):
            for targetRow in range(2):
                for targetCol in range(4):
                    for call in range(2):
                        if agentRow != 1 or agentCol != 1 or call == 1:
                            print("0.0", end=' ')
                            continue  
                        if agentRow == targetRow and agentCol == targetCol:
                            print(1.0/num, end=' ')
                            continue
                        if agentRow == targetRow+1 and agentCol == targetCol:
                            print(1.0/num, end=' ')
                            continue
                        if agentRow == targetRow-1 and agentCol == targetCol:
                            print(1.0/num, end=' ')
                            continue
                        if agentRow == targetRow and agentCol == targetCol+1:
                            print(1.0/num, end=' ')
                            continue
                        if agentRow == targetRow and agentCol == targetCol-1:
                            print(1.0/num, end=' ')
                            continue
                        print("0.0", end=' ')
    print()
    print()    
    
    
    # Transitions
    for agentRow in range(2):
        for agentCol in range(4):
            for targetRow in range(2):
                for targetCol in range(4):
                    for call in range(2):
                        for act in ACTIONS:
                            aR = agentRow
                            aC = agentCol
                            tR = targetRow
                            tC = targetCol
                            c = call
                            pr = 0
                            if call == 0:
                                if act != "STAY":
                                    # Successful transition
                                    if act == "UP":
                                        aR = max(0, agentRow-1)
                                    if act == "DOWN":
                                        aR = min(1, agentRow+1)
                                    if act == "LEFT":
                                        aC = max(0, agentCol-1)
                                    if act == "RIGHT":
                                        aC = min(3, agentCol+1)
                                    # No call
                                    fails = 0
                                    tR = max(0, targetRow-1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.04")
                                        pr += 0.04
                                    else:
                                        fails += 1
                                    tR = min(1, targetRow+1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.04")
                                        pr += 0.04
                                    else:
                                        fails += 1
                                    tC = max(0, targetCol-1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.04")
                                        pr += 0.04
                                    else:
                                        fails += 1
                                    tC = min(3, targetCol+1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.04")
                                        pr += 0.04
                                    else:
                                        fails += 1
                                    prob = round(0.24 + fails*0.04, 3)
                                    tR = targetRow
                                    tC = targetCol
                                    print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} {prob}")
                                    pr += prob
                                    # Call
                                    fails = 0
                                    tR = max(0, targetRow-1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}1 0.04")
                                        pr += 0.04
                                    else:
                                        fails += 1
                                    tR = min(1, targetRow+1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}1 0.04")
                                        pr += 0.04
                                    else:
                                        fails += 1
                                    tC = max(0, targetCol-1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}1 0.04")
                                        pr += 0.04
                                    else:
                                        fails += 1
                                    tC = min(3, targetCol+1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}1 0.04")
                                        pr += 0.04
                                    else:
                                        fails += 1
                                    prob = round(0.24 + fails*0.04, 3)
                                    tR = targetRow
                                    tC = targetCol
                                    pr += prob
                                    print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}1 {prob}")
                                    
                                    # Failed transition
                                    if act == "DOWN":
                                        aR = max(0, agentRow-1)
                                    if act == "UP":
                                        aR = min(1, agentRow+1)
                                    if act == "RIGHT":
                                        aC = max(0, agentCol-1)
                                    if act == "LEFT":
                                        aC = min(3, agentCol+1)
                                    # No call
                                    fails = 0
                                    tR = max(0, targetRow-1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.01")
                                        pr += 0.01
                                    else:
                                        fails += 1
                                    tR = min(1, targetRow+1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.01")
                                        pr += 0.01
                                    else:
                                        fails += 1
                                    tC = max(0, targetCol-1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.01")
                                        pr += 0.01
                                    else:
                                        fails += 1
                                    tC = min(3, targetCol+1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.01")
                                        pr += 0.01
                                    else:
                                        fails += 1
                                    prob = round(0.06 + fails*0.01, 3)
                                    tR = targetRow
                                    tC = targetCol
                                    print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} {prob}")
                                    pr += prob
                                    
                                    fails = 0
                                    tR = max(0, targetRow-1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}1 0.01")
                                        pr += 0.01
                                    else:
                                        fails += 1
                                    tR = min(1, targetRow+1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}1 0.01")
                                        pr += 0.01
                                    else:
                                        fails += 1
                                    tC = max(0, targetCol-1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}1 0.01")
                                        pr += 0.01
                                    else:
                                        fails += 1
                                    tC = min(3, targetCol+1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}1 0.01")
                                        pr += 0.01
                                    else:
                                        fails += 1
                                    prob = round(0.06 + fails*0.01, 3)
                                    tR = targetRow
                                    tC = targetCol
                                    pr += prob
                                    print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}1 {prob}")
        
                                else:
                                    aR = agentRow
                                    aC = agentCol
                                    tR = targetRow
                                    tC = targetCol
                                    c = call
                                    fails = 0
                                    tR = max(0, targetRow-1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.05")
                                        pr += 0.05
                                    else:
                                        fails += 1
                                    tR = min(1, targetRow+1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.05")
                                        pr += 0.05
                                    else:
                                        fails += 1
                                    tC = max(0, targetCol-1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.05")
                                        pr += 0.05
                                    else:
                                        fails += 1
                                    tC = min(3, targetCol+1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.05")
                                        pr += 0.05
                                    else:
                                        fails += 1
                                    prob = round(0.30 + fails*0.05, 3)
                                    tR = targetRow
                                    tC = targetCol
                                    print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} {prob}")
                                    pr += prob
                                    # Call
                                    fails = 0
                                    tR = max(0, targetRow-1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}1 0.05")
                                        pr += 0.05
                                    else:
                                        fails += 1
                                    tR = min(1, targetRow+1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}1 0.05")
                                        pr += 0.05
                                    else:
                                        fails += 1
                                    tC = max(0, targetCol-1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}1 0.05")
                                        pr += 0.05
                                    else:
                                        fails += 1
                                    tC = min(3, targetCol+1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}1 0.05")
                                        pr += 0.05
                                    else:
                                        fails += 1
                                    prob = round(0.30 + fails*0.05, 3)
                                    tR = targetRow
                                    tC = targetCol
                                    pr += prob
                                    print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}1 {prob}")
                                
                                
                            else:
                                if act != "STAY":
                                    # Successful transition
                                    if act == "UP":
                                        aR = max(0, agentRow-1)
                                    if act == "DOWN":
                                        aR = min(1, agentRow+1)
                                    if act == "LEFT":
                                        aC = max(0, agentCol-1)
                                    if act == "RIGHT":
                                        aC = min(3, agentCol+1)
                                    # No hangup
                                    fails = 0
                                    tR = max(0, targetRow-1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.072")
                                        pr += 0.072
                                    else:
                                        fails += 1
                                    tR = min(1, targetRow+1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.072")
                                        pr += 0.072
                                    else:
                                        fails += 1
                                    tC = max(0, targetCol-1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.072")
                                        pr += 0.072
                                    else:
                                        fails += 1
                                    tC = min(3, targetCol+1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.072")
                                        pr += 0.072
                                    else:
                                        fails += 1
                                    prob = round(0.432 + fails*0.072, 3)
                                    tR = targetRow
                                    tC = targetCol
                                    pr += prob
                                    print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} {prob}")
                                    
                                    # hangup
                                    fails = 0
                                    tR = max(0, targetRow-1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}0 0.008")
                                        pr += 0.008
                                    else:
                                        fails += 1
                                    tR = min(1, targetRow+1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}0 0.008")
                                        pr += 0.008
                                    else:
                                        fails += 1
                                    tC = max(0, targetCol-1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}0 0.008")
                                        pr += 0.008
                                    else:
                                        fails += 1
                                    tC = min(3, targetCol+1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}0 0.008")
                                        pr += 0.008
                                    else:
                                        fails += 1
                                    prob = round(0.048 + fails*0.008, 3)
                                    tR = targetRow
                                    tC = targetCol
                                    pr += prob
                                    print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}0 {prob}")
                                    
                                    # Failed transition
                                    if act == "DOWN":
                                        aR = max(0, agentRow-1)
                                    if act == "UP":
                                        aR = min(1, agentRow+1)
                                    if act == "RIGHT":
                                        aC = max(0, agentCol-1)
                                    if act == "LEFT":
                                        aC = min(3, agentCol+1)
                                    # No hangup
                                    fails = 0
                                    tR = max(0, targetRow-1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.018")
                                        pr += 0.018
                                    else:
                                        fails += 1
                                    tR = min(1, targetRow+1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.018")
                                        pr += 0.018
                                    else:
                                        fails += 1
                                    tC = max(0, targetCol-1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.018")
                                        pr += 0.018
                                    else:
                                        fails += 1
                                    tC = min(3, targetCol+1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.018")
                                        pr += 0.018
                                    else:
                                        fails += 1
                                    prob = round(0.108 + fails*0.018, 3)
                                    tR = targetRow
                                    tC = targetCol
                                    pr += prob
                                    print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} {prob}")
                                    
                                    # hangup
                                    fails = 0
                                    tR = max(0, targetRow-1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}0 0.002")
                                        pr += 0.002
                                    else:
                                        fails += 1
                                    tR = min(1, targetRow+1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}0 0.002")
                                        pr += 0.002
                                    else:
                                        fails += 1
                                    tC = max(0, targetCol-1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}0 0.002")
                                        pr += 0.002
                                    else:
                                        fails += 1
                                    tC = min(3, targetCol+1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}0 0.002")
                                        pr += 0.002
                                    else:
                                        fails += 1
                                    prob = round(0.012 + fails*0.002, 3)
                                    tR = targetRow
                                    tC = targetCol
                                    pr += prob
                                    print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}0 {prob}")
                                else:
                                    aR = agentRow
                                    aC = agentCol
                                    tR = targetRow
                                    tC = targetCol
                                    c = call
                                    # No hangup
                                    fails = 0
                                    tR = max(0, targetRow-1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.09")
                                        pr += 0.09
                                    else:
                                        fails += 1
                                    tR = min(1, targetRow+1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.09")
                                        pr += 0.09
                                    else:
                                        fails += 1
                                    tC = max(0, targetCol-1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.09")
                                        pr += 0.09
                                    else:
                                        fails += 1
                                    tC = min(3, targetCol+1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} 0.09")
                                        pr += 0.09
                                    else:
                                        fails += 1
                                    prob = round(0.54 + fails*0.09, 3)
                                    tR = targetRow
                                    tC = targetCol
                                    pr += prob
                                    print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}{c} {prob}")
                                    
                                    # hangup
                                    fails = 0
                                    tR = max(0, targetRow-1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}0 0.01")
                                        pr += 0.01
                                    else:
                                        fails += 1
                                    tR = min(1, targetRow+1)
                                    tC = targetCol
                                    if tR != targetRow:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}0 0.01")
                                        pr += 0.01
                                    else:
                                        fails += 1
                                    tC = max(0, targetCol-1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}0 0.01")
                                        pr += 0.01
                                    else:
                                        fails += 1
                                    tC = min(3, targetCol+1)
                                    tR = targetRow
                                    if tC != targetCol:
                                        print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}0 0.01")
                                        pr += 0.01
                                    else:
                                        fails += 1
                                    prob = round(0.06 + fails*0.01, 3)
                                    tR = targetRow
                                    tC = targetCol
                                    pr += prob
                                    print(f"T : {act} : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : S{aR}{aC}{tR}{tC}0 {prob}")
                            
                            assert 0.99 < pr < 1.01
    # Observations
    for agentRow in range(2):
        for agentCol in range(4):
            for targetRow in range(2):
                for targetCol in range(4):
                    for call in range(2):
                        if agentRow == targetRow and agentCol == targetCol:
                            print(f"O : * : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : O1 1.0")
                        elif agentRow == targetRow and agentCol == targetCol-1:
                            print(f"O : * : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : O2 1.0")
                        elif agentRow == targetRow-1 and agentCol == targetCol:
                            print(f"O : * : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : O3 1.0")
                        elif agentRow == targetRow and agentCol == targetCol+1:
                            print(f"O : * : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : O4 1.0")
                        elif agentRow == targetRow+1 and agentCol == targetCol:
                            print(f"O : * : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : O5 1.0")
                        else:
                            print(f"O : * : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : O6 1.0")
    
    # Rewards
    for agentRow in range(2):
        for agentCol in range(4):
            for targetRow in range(2):
                for targetCol in range(4):
                    for call in range(2):
                        if not call:
                            print(f"R : * : * : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : * -1")
                        else:
                            if agentRow == targetRow and agentCol == targetCol:
                                print(f"R : * : * : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : O1 69")
                            elif agentRow == targetRow and agentCol == targetCol-1:
                                print(f"R : * : * : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : O2 -1")
                            elif agentRow == targetRow-1 and agentCol == targetCol:
                                print(f"R : * : * : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : O3 -1")
                            elif agentRow == targetRow and agentCol == targetCol+1:
                                print(f"R : * : * : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : O4 -1")
                            elif agentRow == targetRow+1 and agentCol == targetCol:
                                print(f"R : * : * : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : O5 -1")
                            else:
                                print(f"R : * : * : S{agentRow}{agentCol}{targetRow}{targetCol}{call} : O6 -1")
                            
if __name__ == "__main__":
    main()