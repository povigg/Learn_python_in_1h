#Weight transformation excersise:
weight = int(input("Weight: "))
wtype = input("(K)g ir (L)bs: ")
if wtype.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))

