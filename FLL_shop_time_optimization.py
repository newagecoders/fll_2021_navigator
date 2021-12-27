
def getCustList():
    n_of_items_to_ship = int(input("Enter the items in the list"))
    list_items_to_shop = []
    for i in range(0, n_of_items_to_ship):
        item_to_shop = input("Enter the item:").lower().strip()
        list_items_to_shop.append(item_to_shop)
    return (list_items_to_shop)


def getItemsAvailable(list1, list2):
    list1_set = set(list1)
    differ = list(list1_set.intersection(list2))
    #print("The list available", differ)
    return differ

def getItemsInAisleMapping():
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

def getCartDetails():
    pass



list_items_in_shop = []
list_aisle_in_shop = []
keymap_aisles = getItemsInAisleMapping()
for items in keymap_aisles:
    #print(items)
    #print(keymap_aisles[items])
    list_items_in_shop.append(keymap_aisles[items])
    list_aisle_in_shop.append(items)
#print(list_aisle_in_shop)

list_items_to_shop = getCustList()
print("The list Customer Wants to shop: ", list_items_to_shop)

list_available = getItemsAvailable(list_items_to_shop, list_items_in_shop)
print("The items in list available to shop: ",(list_available))
isle_list=[]
isle_list.append(getAisleList(keymap_aisles,list_available))

print("The aisle list:",isle_list)
#print(type(isle_list))



