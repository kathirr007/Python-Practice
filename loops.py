menus = {
    'Breakfast': ['Idli', 'Dosa', 'Vadai', 'Parotta'],
    'Lunch': ['South Indian Meals', 'North Indian Tali', 'Parotta'],
    'Dinner': ['Veg Fried Rice', 'Veg Noodles', 'Chicken Noodles', 'Chicken Fried Rice', 'Parotta']
}

# Print the menu items:

for name, menu in menus.items():
    print(f"{name}: ")
    print("---")
    for i, item in enumerate(menu):
        if i == len(menu) - 1:
            print(f"{item} \n")
        else:
            print(f"{item}")