expenses = [21,32,10,23.3,10,12.3,4.1]

sumTotal = 0

for x in expenses:
    sumTotal = sumTotal + x

total = sum(expenses)

expensesPrintMessage = "You've spent $"

print(expensesPrintMessage, sumTotal)
print(expensesPrintMessage, sumTotal, sep='')
print(expensesPrintMessage, total, sep='')