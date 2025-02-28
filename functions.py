"""
All different types of Python functions
"""


# Function with no arguments
def greet():
    print("Hello!")


greet()


# Function with one argument
def greetWithOneArgument(name):
    print(f"Hello, {name}!")


greetWithOneArgument("Alice")


# Function with two arguments
def greetWithTwoArguments(name, time_of_day):
    print(f"Good {time_of_day}, {name}!")


greetWithTwoArguments("Alice", "morning")


# Function with default arguments
def greetWithDefault(name, time_of_day="evening"):
    print(f"Good {time_of_day}, {name}!")


greetWithDefault("Alice")


# Function with variable number of arguments
def greetWithVariableArguments(*names):
    for name in names:
        print(f"Hello, {name}!")


greetWithVariableArguments("Alice", "Bob", "Charlie")


# Function with keyword arguments
def greetWithKeywordArguments(name, time_of_day="evening"):
    print(f"Good {time_of_day}, {name}!")


greetWithKeywordArguments(name="Alice", time_of_day="morning")


# Function with keyword arguments and variable number of arguments
def greetWithKeywordArgumentsAndVariableArguments(*names, time_of_day="evening"):
    for name in names:
        print(f"Good {time_of_day}, {name}!")


greetWithKeywordArgumentsAndVariableArguments(
    "Alice", "Bob", "Charlie", time_of_day="morning"
)


# Function with keyword arguments and variable number of keyword arguments
def greetWithKeywordArgumentsAndVariableKeywordArguments(*names, **time_of_day):
    for name in names:
        print(f"Good {time_of_day['time_of_day']}, {name}!")


greetWithKeywordArgumentsAndVariableKeywordArguments(
    "Alice", "Bob", "Charlie", time_of_day="morning"
)


# Function with positional arguments
def add(x, y):
    """Adds two numbers and returns the result."""
    return x + y


# Calling the function
result = add(5, 3)
print(result)  # Output: 8

# Function with keyword arguments
def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

# Calling the function
describe_pet(animal_type="hamster", pet_name="Harry")
describe_pet(pet_name="Fido", animal_type="dog")  # Order doesn't matter

# Function with variable length positional arguments
def calculate_sum(*numbers):
    # *numbers collects all positional arguments into a tuple.
    """Calculates the sum of any number of arguments."""
    total = 0
    for number in numbers:
        total += number
    return total

# Calling the function
result1 = calculate_sum(1, 2, 3)
result2 = calculate_sum(10, 20, 30, 40, 50)
print(result1)  # Output: 6
print(result2)  # Output: 150

def build_profile(first_name, last_name, **user_info):
    """Builds a user profile dictionary."""
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

# Calling the function
profile = build_profile(
    last_name="Doe",
    location="New York",
    first_name="John",
    field="Software Engineer",
)
print(profile)
# Output: {'location': 'New York', 'field': 'Software Engineer', 'first_name': 'John', 'last_name': 'Doe'}

