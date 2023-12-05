char = input("Enter your letter: ")
i = 1
if char == 'A' or char =='a' or char == 'A' or char =='a' or char == 'E' or char =='e' or char == 'I' or char =='i'  or char == 'O' or char =='o' or char == 'U' or char =='u':
    print("Vowels are not allowed in the input") 
elif len(char) >=2:
   print("The length of the character should be one ")
else:
    while i <= 10:
        print ( char * i)
        i=i+2