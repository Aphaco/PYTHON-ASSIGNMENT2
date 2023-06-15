total = 0

while True:
    num = int(input("Enter a number: "))
    if num <0:
        break
    elif num >0:
        total = num+total 
print("Total:", total)