#Variables
upper_limit = 100
automatic = False
substitutions = {
    3: "Fizz",
    5: "Buzz"
}

# Functions
def CheckValue(x: int) -> str:
    output = ""

    for item in list(substitutions.keys()):
        if x % item == 0:
            output += substitutions[item]
        
    #1If no multiples found, return the number
    if output == "": return str(x)

    return output

# def CheckValue(x: int) -> str:
#     output = ""

#     # Check for multiples
#     if x % 3 == 0: output += "Fizz"
#     if x % 5 == 0: output += "Buzz"
    
#     # If no multiples found, return the number
#     if output == "": return str(x)

#     return output

# Main
if __name__ == "__main__":
    if automatic:
        for i in range(upper_limit + 1):
            print(CheckValue(i))

    else:
        running = True
        step = 0

        print("FizzBuzz Guessing Game")
        print("Multiples to substitute")
        for item in list(substitutions.keys()):
            print(f"{item}: {substitutions[item]}")
        print("Start")

        while running:
            # Get the guess and expected input
            step += 1
            expected_input = CheckValue(step).lower()
            guess = input().lower()

            # Check for incorrect guesses
            if guess != expected_input:
                print(f"Incorrect. Expected entry was {expected_input}")
                print(f"You completed {step - 1} steps.")
                running = False 
        
    