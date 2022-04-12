bosses = ["Abyss Watchers", "Aldrich", "Yhorm", "Prince Lothric"]
defeated_bosses = ["Abyss Watchers", "Yhorm"]

for enemy in bosses:
    if enemy in defeated_bosses:
        print(f"{enemy} has been defeated!")
    elif enemy == "Prince Lothric":
        if not ("Yhorm" in defeated_bosses and "Aldrich" in defeated_bosses):
            print(f"{enemy} is not currently reachable")
    else:
        print(f"{enemy} still lives!")