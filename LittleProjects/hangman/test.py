def canParkCar(carLen, streetLen, carLocations, carLengths):
#Should check if a car can park in a street
    parkMap = ""
    i = 0
    park = 0
    j = 0
    while j < streetLen:#Generating a string like the example
        if park < len(carLocations) and j == carLocations[park]: #Checking if we are in a park position
            park +=1
            #if we are we add x to the string as many as carLength[i]
            for k in range(carLengths[i]):
                parkMap += "X"
                j +=1
            i +=1
        else:
            j+=1
            parkMap += "-"
    
    consecutive = 0
    for letter in parkMap:
        if letter == "-":
            consecutive +=1
            if consecutive >= carLen:
                return True
        elif letter == "X":
            consecutive =0
    return False
print(canParkCar(2, 10, [0,3,6], [2,2,2]))