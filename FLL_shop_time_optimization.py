import math
import itertools
import string

def getCustList():
    list_items_to_shop = []
    with open("listCustomerWantsToShop.txt") as r:
        for line in r:
            list_items_to_shop = line.split()
    return (list_items_to_shop)

#This method is used to manually input the list
#######################################################
def getCustList1():
    n_of_items_to_ship = int(input("Enter the items in the list"))
    list_items_to_shop = []
    for i in range(0, n_of_items_to_ship):
        item_to_shop = input("Enter the item:").lower().strip()
        list_items_to_shop.append(item_to_shop)
    return (list_items_to_shop)
########################################################
def getItemsAvailable(list1, list2):
    list1_set = set(list1)
    differ = list(list1_set.intersection(list2))
    #print("The list available", differ)
    return differ

def getItemsInAisleMapping():
    itemAisleMap = {}
    with open("itemsInAisleMapping.txt") as f:
        for line in f:
            (key, val) = line.split()
            itemAisleMap[key] = val
    #print(itemAisleMap)
    #print(type(itemAisleMap))
    return itemAisleMap

def getItemsInAisleMapping1():
    keymap_aisles = {
        "A1": "yogurt",
        "A2": "milk",
        "A3": "cheese",
        "B1": "carrots",
        "B2": "tomatoes",
        "B3": "artichokes",
        "C1": "bananas",
        "C2": "apples",
        "C3": "mango"
    }
    return keymap_aisles

def getAisleList(dictOfElements, listOfValues):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] in listOfValues:
            listOfKeys.append(item[0])
    return  listOfKeys


def aisle_mapp(aisle):
    aisle = str(aisle)
    first_val = aisle[0]
    second_val = int(aisle[1])
    alphabet = string.ascii_uppercase
    cord_list = []
    cord_list.append(alphabet.index(first_val))
    cord_list.append(second_val - 1)
    return cord_list

def dist_between_aisle(current_aisle,next_aisle):
    dis_bw_two_aisle=0
    if current_aisle[0]== next_aisle[0]:
        dis_bw_two_aisle=abs(current_aisle[1]-next_aisle[1])
        return dis_bw_two_aisle
    else:
        dis_bw_two_aisle= (abs(current_aisle[0]-next_aisle[0]))+(abs(current_aisle[1]-next_aisle[1]))
        return dis_bw_two_aisle

def get_distance_current_loop(usrlist):
    distance = 0
    for aisles in range(0, len(usrlist) - 1):
        current_aisle_cord = aisle_mapp(usrlist[aisles])
        next_aisle_cord = aisle_mapp(usrlist[aisles + 1])
        distance = distance + dist_between_aisle(current_aisle_cord, next_aisle_cord)
    return distance
def get_best_path(isle_list,distance):
    possible_perm = list(itertools.permutations(isle_list))
    distance_current = 0
    distance_minimum = distance
    list_optimum = []
    for permutation in range(0, len(possible_perm)):
        current_perm = list(possible_perm[permutation])
        distance_current = get_distance_current_loop(current_perm)
        if distance_current < distance_minimum:
            distance_minimum = distance_current
            list_optimum = current_perm.copy()
            #print("List optimum", list_optimum)
        list_optimum=current_perm.copy()
        #print("Distance:",distance_minimum,"List outside IF",current_perm )
    bestpath=[distance_minimum,list_optimum]
    print("Total routes inspected for best route: ",len(possible_perm))
    return bestpath
## Main Program where the Code starts ##
def main():
    print("Welcome to Navigator")
    list_items_in_shop = []
    list_aisle_in_shop = []
    keymap_aisles = getItemsInAisleMapping()
    #print(type(keymap_aisles))
    for items in keymap_aisles:
        list_items_in_shop.append(keymap_aisles[items])
        list_aisle_in_shop.append(items)

    list_items_to_shop = getCustList()
    print("The list Customer Wants to shop: ", list_items_to_shop)

    list_available = getItemsAvailable(list_items_to_shop, list_items_in_shop)
    print("The items in list available to shop: ", (list_available))
    isle_list = []
    isle_list.append(getAisleList(keymap_aisles, list_available))
    isle_list = isle_list[0]
    print("The aisle list to go around:", isle_list)
    distance = 0

    for items in range(0, len(isle_list)):
        isle_list_new = isle_list.copy()
        distance_current = get_distance_current_loop(isle_list_new)

    print("Total Aisle to cover: ", len(isle_list))

    distance = get_distance_current_loop(isle_list)
    print("Distance to cover", len(isle_list), " aisles :", distance)
    path=get_best_path(isle_list,distance)
    #print(path)


    print("Distance:","for Loop:",path)
    print("Shortest distance :",path[0], "Steps")
    print("Shortest route:", path[1])
    print(keymap_aisles)



if __name__=="__main__":
    main()



