#Global Variables
results = open("Labs/Challenge/results.txt", "w")
lower_limit = 1
upper_limit = 250

#Functions
def is_prime(x: int) -> bool:
    prime: bool = True
    # 1 isn't prime, but this function will return that it is.
    if x == 1:
        return False

    for i in range(x - 1, 2, -1):
        if x % i == 0:
            prime = False
            break
    return prime

if __name__ == "__main__":
    print("Prime numbers:")
    for value in range(lower_limit, upper_limit):
        if is_prime(value):
            print(value)
            results.write(str(value) + "\n")

    results.close()