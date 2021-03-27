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
    
print(value[pos['N']][mat['1']][arrows['1']][MM['R']][health['25']][action['GATHER']])