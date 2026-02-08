import random
while True:
    l = [1, 2, 3, 4, 5, 6]
    a = input("Enter (Roll as R & Exit as E) : ")
    if a == "R":
        print(random.choice(l))
    elif a == "E":
        break
    else:
        print("Try Again!")