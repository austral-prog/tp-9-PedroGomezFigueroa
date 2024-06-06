def create_inventory(items):
    mydict=dict()
    for i,value in enumerate(items):
        if value in mydict:
            mydict[value]+=1
        else:
            mydict[value]=1
    return mydict
print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))
    

def add_items(inventory, items):

    for i,value in enumerate(items):
        if value in inventory:
            inventory[value]+=1
        else:
            inventory[value]=1
    return inventory


print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))


def decrement_items(inventory, items):
    mydict = inventory
    for i,value in enumerate(items):
        if value in mydict and mydict[value]!=0:
            mydict[value]-=1
    return mydict

print(decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"]))


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]

    return inventory
print(remove_item({"coal":2, "wood":1, "diamond":2}, "coal"))


def list_inventory(inventory):
    listaparaborrar=[]
    milista=[]
    for key, value in inventory.items():
        if value == 0:
            listaparaborrar.append(key)
    for i in listaparaborrar:
        del inventory[i]
    for key,value in inventory.items():
        milista.append((key,value))

            
    return milista

print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))

