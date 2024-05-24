a=input("Enter string 1:")
b=input("Enter string 2:")
if len(a)!=len(b):
    print("given strings are Not Anagrams")
else:
    if sorted(a)==sorted(b):
        print("given strings are Anagrams")
    else:
        print("given strings are not Anagrams")