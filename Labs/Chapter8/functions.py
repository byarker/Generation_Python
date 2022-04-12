def calculate(*values: int, operation="add"):
    result = 0
    if operation == "add":
        for item in values:
            result += item
        return result
    elif operation == "multiply":
        result = 1
        for item in values:
            result *= item
        return result

print(calculate(5, 3, 2, operation="multiply"))


