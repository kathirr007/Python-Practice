acronym = input("What software acronym you would like to add? \n")
definition = input("What is the definition? \n")

with open("acronyms.txt", "a") as file:
    file.write(f"{acronym} - {definition}\n")
