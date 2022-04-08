import random

#magicians = ["Dark Magician", "Dark Magician Girl", "Dark Magician of Chaos"]
#attacks = ["Dark Magic Attack", "Dark Burning Attack", "Spell of Destruction - Death Ultima"]

magicians = {"Dark Magician": "Dark Magic Attack",
    "Dark Magician Girl":  "Dark Burning Attack",
    "Dark Magician of Chaos": "Spell of Destruction - Death Ultima"}

selection = random.choice(list(magicians))

print("Go " + selection + "! " + magicians[selection] + "!")
print(f"Go {selection}! {magicians[selection]}!")