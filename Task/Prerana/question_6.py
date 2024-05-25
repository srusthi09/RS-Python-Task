#QUESTION6
# Function check whether a number
# is prime or not
def is_prime(n):
    if n > 1:
        for i in range(2, (n//2)+1):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False

def main(arr):
    maxx = -1
    minn = -1
    mp = {}
    for num in arr:
        mp[num] = mp.get(num, 0) + 1
    for num in sorted(mp):
        if is_prime(num):
            minn = num
            break
        
    for num in sorted(mp, reverse=True):
        if is_prime(num):
            maxx = num
            break

    print("Minimum:", minn)
    print("Maximum:", maxx)
    print("The absolute difference is:", maxx-minn)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    main(arr)
