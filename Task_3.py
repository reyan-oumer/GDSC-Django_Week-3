s=input("Enter the word to be checked: ")
pal =  s[::-1]
#pal.lower()
if s.lower() == pal.lower():
    print("Your word is palindrome ")
else:
    print("The word", s.lower(),"is not palindrome,")
    print( "Because the word", pal.lower() , "is not equal to" , s.lower())