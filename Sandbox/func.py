# Learning materials
print("# Sandbox")

# Split up sections
def SectionBreak(title: str) -> None:
    print()
    print("-" * 20)
    print(f"# {title}")


# --------------------
# Methods can be chained together
SectionBreak("Method chaining")

greeting = "  Hello world! ".strip().title()
print(greeting)
farewell = "Goodbye!".upper().title().lower().strip()
print(farewell)


# --------------------
# Lists and the 'in' keyword
SectionBreak("The \"in\" keyword")

# Going through each item in a list
numbers = [1, 52, 33]
for item in numbers:
    print(item)

# Checking if an item is in a list
if 33 in numbers:
    print("33 is in numbers")

# in works on strings too
print("n" in "elephant")


# --------------------
# Assigning variables to one another
SectionBreak("Variable copying")

# Changing the original variable does not change the copy
alpha = "Chicken"
beta = alpha
alpha = "Beef"
print(beta)