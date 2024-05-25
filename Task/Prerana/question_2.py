#QUESTION2
def count_char(string):
    frequency = {}

    for char in string:
        if char.isalpha(): 
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    uppercase_char = sorted([char for char in frequency if char.isupper()])
    lowercase_char = sorted([char for char in frequency if char.islower()])

    print("Character frequencies in lexicographical order:")
    for char in uppercase_char:
        print(f"{char}: {frequency[char]}")
     
    for char in lowercase_char:
        print(f"{char}: {frequency[char]}")

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    count_char(input_string)