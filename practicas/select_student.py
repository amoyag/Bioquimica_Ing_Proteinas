import random

# Initial list of names
names = ["Jorge", "Juandiego", "Enzo", "Ashley"]

# Function to pick and remove a random name
def pick_random_name(remaining_names):
    # Pick a random name from the list
    selected_name = random.choice(remaining_names)
    # Remove the selected name from the list
    remaining_names.remove(selected_name)
    return selected_name, remaining_names

# Run the script 3 times
remaining_names = names[:]
for i in range(3):
    selected_name, remaining_names = pick_random_name(remaining_names)
    print(f"Round {i+1}: Selected name - {selected_name}")
    print(f"Remaining names - {remaining_names}")

