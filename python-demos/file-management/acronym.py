def find_acronym():
    look_up = input("Enter acronym to look up: ").upper()
    found = False
    with open("acronyms.txt", "r") as file:
        for line in file:
            if line.startswith(look_up):
                print(line.strip())
                found = True
                break
    if not found:
        print("Acronym not found.")


def find_acronym():
    look_up = input("Enter acronym to look up: ").upper()
    found = False
    with open("acronym.txt", "r") as file:
        for line in file:
            if line.startswith(look_up):
                print(line.strip())
                found = True
                break
    if not found:
        print("Acronym not found.")


def main():
    while True:
        action = input("Would you like to (A)dd, (L)ookup, or (Q)uit? ").upper()
        if action == "A":
            acronym = input("What acronym do you want to Add? ").upper()
            definition = input("What does it stand for? ")
            with open("acronym.txt", "a") as file:
                file.write(f"{acronym}: {definition}\n")
                print("Acronym added.")
        elif action == "L":
            find_acronym()
        elif action == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose A, L, or Q.")


main()
