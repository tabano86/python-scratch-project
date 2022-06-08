# Initial list of game characters

master_characters: list[str] = ["Megan Man", "Kirby", "Sonic", "Tails"]

# Displays descending list for user
print("There are currently {} characters on the list:".format(len(master_characters)))
print(*master_characters, sep=", ")

# # Newer block to streamline user prompt input
characters_to_add = input("Characters to add (separated by comma): ").split(",")

master_characters = master_characters + list(map(lambda x: x.strip(), characters_to_add))

print(f"Here is your updated list with [{len(characters_to_add)}] newly added characters:")
print(*(sorted(master_characters, reverse=True)), sep=", ")
