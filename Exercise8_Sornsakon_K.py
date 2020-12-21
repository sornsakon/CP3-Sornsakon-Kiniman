username = input("Username : ")
password = input("Password : ")
if username == "kaz" and password == "2212":
    print("Welcome To LK Shop")
    print("------------------")
    print("1 : Sangsom 430 Bath")
    print("2 : Blend285 450 Bath")
    print("3 : Black Label 1000 Bath")
    print("------------------")
    product = int(input("Select a product number : "))
    if product == 1:
        product_number = int(input("how many products do you want? : "))
        print("Total Cost :",product_number*430)
    elif product == 2:
        product_number = int(input("how many products do you want? : "))
        print("Total Cost :",product_number*450)
    elif product == 3:
        product_number = int(input("how many products do you want? : "))
        print("Total Cost :",product_number*1000)
    else :
        print ("Please enter number : 1 or 2 or 3")
elif username != "kaz" and password == "2212":
    print ("Incorrect username")
elif username == "kaz" and password != "2212":
    print ("Incorrect password")
else:
    print ("Incorrect username and password")