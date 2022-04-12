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


# --------------------
# Contents of dictionaries can be anything
SectionBreak("Dictionary contents")
my_dictionary = {
    "character": 'c',
    "string": "hello",
    "integer": 42,
    "float": 3.14,
    "list": [1,2,3,4,5,"David"],
    "dictionary": {
        "first_name": "Barry",
        "last_name": "Chuckle",
        "job": "Commedian"
    }
}

for key, value in my_dictionary.items():
    print(f"{key}: {value}")