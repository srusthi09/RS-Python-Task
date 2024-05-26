#QUESTION3
def plusOne(n):
    for i in range(len(n) - 1, -1, -1):
        if n[i] < 9:
            n[i] += 1
            return n
        n[i] = 0
    return [1] + n

print(plusOne([1, 2, 4]))
print(plusOne([3, 6, 9])) 
print(plusOne([9, 9, 9]))  