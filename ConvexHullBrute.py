# Ryland Atkins
# This is entirely my own work.

import random

# Helper function used to identify side of line.
def sign(num):
    if num > 0:
        return 1
    else:
        if num < 0:
            return -1
        else:
            return 0

multSum = 0
runTimes = 500
# Number of test runs.
for r in range(runTimes):

    # Generate a set of random points.
    ranje = 100
    x = 0
    y = 0
    pointSet = []
    for i in range(160):
        x = random.randint(-ranje,ranje)
        y = random.randint(-ranje,ranje)
        tup = (x, y)
        pointSet.append(tup)

    # Find convex hull.
    convexHull =[]
    mults = 0
    # For every point tuple...
    for i in range(len(pointSet)):     
        for j in range(i+1,len(pointSet)):
            Rside = []
            Lside = []
            done = False
            k = 0
            while k < len(pointSet) and not done:
                # Use determinant to find side of line.
                position = sign((pointSet[j][0]-pointSet[i][0])*(pointSet[k][1]-pointSet[i][1])-(pointSet[j][1]-pointSet[i][1])*(pointSet[k][0]-pointSet[i][0]))
                mults = mults + 1
                if position > 0:
                    Rside.append(pointSet[k])
                else:
                    if position < 0:
                        Lside.append(pointSet[k])
                if len(Lside) > 0 and len(Rside) > 0:
                    done = True
                k = k + 1

            # Append points to convex hull.
            if (len(Lside) == 0) and (len(Rside) > 0) or (len(Lside) > 0) and (len(Rside) == 0):
                if pointSet[i] not in convexHull:
                    convexHull.append(pointSet[i])
                if pointSet[j] not in convexHull:
                    convexHull.append(pointSet[j])
       
    multSum = multSum + mults
    
multAvg = multSum / runTimes
print('multAvg = ', multAvg)
               
