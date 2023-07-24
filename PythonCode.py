# Code organized into Methods/Functions/Classes/Modules
from rich.console import Console

# welcome message
console = Console()
console.print("WELCOME TO SUPER SMASHTER SERIES!", style="bold")
console.print("\tPress 'Q' at any point to QUIT and repeat registration process", style="italic")
input("\t\t\tPress ENTER to continue. . .")

#Variables (List here all the variables)


# registration process
reg = []  # Create an empty list to store registration of the users

while True:  # Initiates an infinite loop for the registration process  until explicitly exited
    # get user input for name
    name = input("Enter your NAME: ").upper()  # Changes all inputs to CAPITALS

    if name.lower() == 'q':
        print("Returning to the beginning of the registration process...")
        continue  # Restart registration process from the beginning.Previous entries are preserved

    if not name.isalpha():
        print("Invalid input! Please enter LETTERS ONLY WITHOUT SPACES.")
        continue  # Skip the current iteration and prompt for a new name.Previous entries are preserved

    # get user input for gamer tag
    gamertag = input("Enter your GAMER TAG: ")

    if gamertag.lower() == 'q':
        print("Returning to the beginning of the registration process...")
        continue  # Restart the registration process from the beginning. Previous entries are preserved


    #Here I am trying to set the condition that whenever both variables "gamertag" and "name" are filled, print that message
    while gamertag==True:
        message = f"YOU ARE NOW REGISTERED! GOOD LUCK!"
        print(message)

    # store registration details in a dictionary
    registration = {'name': name, 'gamertag': gamertag}  # Create a dictionary to store the registration details
    reg.append(registration)  # Add the registration to the list of registration

    # Check if registration process is complete based on length condition
    if len(reg) >= 2:
        break  # Exit the registration process if the condition is met

    input("Press ENTER to continue...")

# displays registration results
print("Registration Process Completed!")
print("Registered Names and Gamer Tags:")

for registration in reg:
    console.print("Name:", registration['name'], style="bold")
    console.print("Gamer Tag:", registration['gamertag'], style="bold")
    print()

# edit registration
# Initializes the 'edit' variable with the none value until finding a match
edit = None  # When matching registration, the 'edit' variable is updated with the registration dictionary
# Find the desired registration
for entry in reg:  # variable "entry" auto created as part of the loop's iteration process
    if entry['name'] == 'WRONGN' or entry['gamertag'] == 'WRONGGT':
        edit = entry
        break

if edit is not None:
    # Perform the necessary edits on the registration dictionary
    if edit['name'] == 'WRONGN':
        edit['name'] = 'New Name'
    if edit['gamertag'] == 'WRONGGT':
        edit['gamertag'] = 'New Gamer Tag'
    print("Registration updated successfully!")
else:
    print("Registration not found.")


#Sort the registration list alphabetized without affecting the existing list
sorted_list = sorted(registration)
print(sorted_list)

# Code to validate whether the 'name' or 'gamertag' already exists to avoid duplicate registrations
