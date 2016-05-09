
def isPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    Prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0 and num != i:
            return False
    return Prime

def split_two_primes(num):
    a = 0
    b = 0
    for i in range(num//2):
        a = i
        b = num - i
        if isPrime(a) == True and isPrime(b) == True:
            return a, b
    else:
        return False

print(split_two_primes(231223950))

