menuList = []
priceList = []
def showBill():
    total = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        total += int(priceList[number])
    print("Total Cost :",total)

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
