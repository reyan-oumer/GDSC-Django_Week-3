"""for i in range(101):
    print(f"{i:02d}", end=" ")""
for num in range(101):
    print(str(num).zfill(2) , end=", ")"""
for i in range(101):
    if i == 100:
        print(i, end='\n')
    else:
        print(str(i).zfill(2), end=', ')