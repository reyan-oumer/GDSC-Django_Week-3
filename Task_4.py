sum=0
NumFive = 0
NumThree = 0
Both = 0
for i in range(1,51):
    if i % 2 == 0:
        if i % 3 == 0 and i% 5==0:
            print("Three and Five")
            Both = Both + 1
        elif i % 3 == 0:
            print("Three")
            NumThree = NumThree +1
        elif i % 5 == 0:
            print("Five")
            NumFive = NumFive + 1
        else:
            print(i)
        sum = sum + i
print("The sum of all even numbers from 1 to 50 :",sum)
print("Count of numbers replaced with 'Three':", NumThree)
print("Count of numbers replaced with 'Five':", NumFive)
print("Count of numbers replaced with 'Three and Five':", Both)
    