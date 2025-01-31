total = 0
expenses = []

number_of_expenses = int(input('Enter the total # of expenses to Sum: '))

for i in range(number_of_expenses):
    expenses.append(float(input('Enter the expense #:' + str(i) + ': ')))

total = round(sum(expenses))

print(f"You've spent ${total}")