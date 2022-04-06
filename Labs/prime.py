#Global Variables
results = open("Labs/results.txt", "w")
upper_limit = 250

#Functions
def is_prime(x: int):
    prime: bool = True
    if x in [0, 1]:
        return False
    for i in range(x - 1, 2, -1):
        if x % i == 0:
            prime = False
            break
    return prime

if __name__ == "__main__":
    print("Prime numbers:")
    for value in range(1, upper_limit):
        if is_prime(value):
            print(value)
            results.write(str(value) + "\n")

    results.close()