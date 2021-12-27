import math
def aisle(X,Y):
    print(X,Y)
    #if (A[x] == B[x]):
    #    print("Same aisle")

def aisle_mapp(aisle_cordinates):
    A1 = [0,0]
    A2 = [0,1]
    A3 = [0,2]
    B1 = [1,0]
    B2 = [1,1]
    B3 = [1,2]
    C1 = [2,0]
    C2 = [2,1]
    C3 = [2,2]
    A0 = [0,0]

    if aisle_cordinates == "A1":
        return A1
    elif aisle_cordinates =="A2":
        return A2
    elif aisle_cordinates =="A3":
        return A3
    elif aisle_cordinates =="B1":
        return B1
    elif aisle_cordinates =="B2":
        return B2
    elif aisle_cordinates =="B3":
        return B3
    elif aisle_cordinates =="C1":
        return C1
    elif aisle_cordinates =="C2":
        return C2
    elif aisle_cordinates =="C3":
        return C3
    else:
        return A0
def dist_between_aisle(current,next):
    #print(current)
    #print(next)
    dis_bw_two_aisle=0
    if current[0]== next[0]:
     #   print("Same isle")
        dis_bw_two_aisle=abs(current[1]-next[1])
        return dis_bw_two_aisle
    else:
      #  print("Next aisle")
      #  print(current[0],":",current[1])
      #  print(next[0],":",next[1])
        dis_bw_two_aisle= (abs(current[0]-next[0]))+(abs(current[1]-next[1]))
        return dis_bw_two_aisle

def get_distance_current_loop(usrlist):
    distance = 0
    for aisles in range(0, len(usrlist) - 1):
        # print(usrlist[1])

        # print(usrlist[aisles],":",aisle_mapp(usrlist[aisles]))
        current_aisle_cord = aisle_mapp(usrlist[aisles])
        next_aisle_cord = aisle_mapp(usrlist[aisles + 1])
        #print("Current Aisle: ", usrlist[aisles], ":", current_aisle_cord)
        #print("Next Aisle ", usrlist[aisles + 1], ":", next_aisle_cord)

        distance = distance + dist_between_aisle(current_aisle_cord, next_aisle_cord)
        #print("Distance Travelled total :", distance)
    return distance


usrlist = ['A1', 'A2', 'B1','B2','C1']
print("Total Aisle to cover: ",len(usrlist))
#print(len(usrlist))
distance=0
distance=get_distance_current_loop(usrlist)
print("Distance to cover",len(usrlist)," aisles :",distance)
