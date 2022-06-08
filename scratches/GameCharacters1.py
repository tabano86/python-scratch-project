# Initial list of game characters

from sortedcontainers import SortedSet

character_set = SortedSet(map(lambda x: x.upper(), ["Mega Man", "Kirby", "Sonic", "Tails"]))

# Displays descending list for user
print("There are currently {} characters on the list:".format(len(character_set)))
print(*character_set, sep=", ")

# # Newer block to streamline user prompt input
characters_to_add = input("Characters to add (separated by comma): ").split(",")
for character in characters_to_add:
    character_set.add(character.strip().upper())

print(f"Here is your updated list with [{len(characters_to_add)}] newly added characters:")
print(*character_set, sep=", ")
