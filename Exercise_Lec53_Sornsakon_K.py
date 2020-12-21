def VaxCalculate(Price) :
    result = Price + Price*(7/100)
    print("Total Cost :",result)
print("--- Vax Calculator ---")
VaxCalculate(int(input("Price : ")))