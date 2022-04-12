bosses = {
    "Abyss Watchers": True,
    "Aldrich": False,
    "Yhrom": True,
    "Prince Lothric": False
}

for enemy in bosses:
    if bosses[enemy]:
        print(f"{enemy} has been defeated!")
    elif enemy == "Prince Lothric":
        if not (bosses["Yhrom"] and bosses["Aldrich"]):
            print(f"{enemy} is not currently reachable.")
        else:
            print(f"{enemy} still lives!")
    else:
        print(f"{enemy} still lives!")