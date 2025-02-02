def find_acronym():
    look_up = input("What software acronym you would like to lookup? \n")

    found = False
    try:
        with open("acronyms.txt") as file:
            for line in file:
                if str.lower(look_up) in str.lower(line):
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found")
        return

    if not found:
        print("The acronym doesn't exist.")


def add_acronym():
    acronym = input("What software acronym you would like to add? \n")
    definition = input("What is the definition? \n")

    try:
        with open("acronyms.txt", "a") as file:
            file.write(f"{acronym} - {definition}\n")
    except FileNotFoundError as e:
        print("File not found.")


def main():
    choice = input("Do you want to find(F) or add(A) acronym? \n")

    if str.lower(choice) == "f":
        find_acronym()
    elif str.lower(choice) == "a":
        add_acronym()


main()
