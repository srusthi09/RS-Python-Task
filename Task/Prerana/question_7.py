#QUESTION7
def prime(n):
 if n > 1:
    for i in range(2, (n//2)+1):
        if (n % i) == 0:
            return False
    else:
        return True
 else:
    return False

def min_prime_factor(n):
    for i in range(2, n + 1):
        if n % i == 0 and prime(i):
            return i

def money_to_pay(mrp):
    min_prime = min_prime_factor(mrp)
    return mrp - min_prime

N = int(input("Enter the number of products: "))

for _ in range(N):
    mrp = int(input("Enter the MRP of the product: "))
    amount_to_pay = money_to_pay(mrp)
    print("Roy will pay:",amount_to_pay)