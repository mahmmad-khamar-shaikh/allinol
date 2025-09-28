acronym = input("What acronym do you want to Add? ").upper()
definition = input("What does it stand for? ")

with open("acronym.txt", "a") as file:
    file.write(f"{acronym}: {definition}\n")
    print("Acronym added.")
