weight = int(input("Weight: "))
wtype = input("(K)g or (L)bs ")

if wtype.upper == "K":
    converted = weight / 0.45
    print("Weight in Kg: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Lbs: " + str(converted))