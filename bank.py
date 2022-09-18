greet = input().title().strip()

n = greet.split(",")
if (greet =="Hello"):
    money=0
elif (n[0]=="Hello"):
    money = 0
elif (greet == "H"):
    money = 20
else:
    money=100

print("$",money)
