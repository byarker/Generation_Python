


#Global Variables
results = open("results.txt", "w")
max

#Functions
def is_prime(x: int):
    prime: bool = True
    if x in [0, 1]:
        return False
    for i in range(x - 1, 2, -1):
        if x % i == 0:
            isPrime = False
            break
    return isPrime



print("Prime numbers:")
for value in range(1, 250):
    if is_prime(value):
        print(value)
        results.write(str(value) + "\n")

results.close()

