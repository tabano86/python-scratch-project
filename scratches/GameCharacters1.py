# Initial list of game characters
list = ["Megan Man", "Kirby", "Sonic", "Tails"]
org_list_len = len(list)  # holding original list length

# Displays descending list for user
print(f"There are currently {org_list_len} characters on the list:")
for list_view in list:
    print(list_view)

# Newer block to streamline user prompt input
prompt = input("Add some more characters to the list!\n")
prompt_list = prompt.split()
list = list + prompt_list

# Displays updated descending list for user
list_sum = len(list)
print(f"Here is your updated list with {list_sum - org_list_len} new added characters:")
for list_view in list:
    print(list_view)
