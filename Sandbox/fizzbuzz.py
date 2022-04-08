#Variables
upper_limit = 100

#Main
def CheckValue(x: int) -> str:
    output = ""

    if x % 3 == 0: output += "Fizz"
    if x % 5 == 0: output += "Buzz"
    
    if output == "": return x
    return output

if __name__ == "__main__":
    for i in range(upper_limit + 1):
        print(CheckValue(i))