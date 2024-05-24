a=input("Enter string 1:")
b=input("Enter string 2:")
if len(a)!=len(b):
    print("Not Anagram")
else:
    if sorted(a)==sorted(b):
        print("given strings are Anagrams")
    else:
        print("given strings are not Anagram")