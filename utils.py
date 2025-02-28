"""
Utility functions
"""


def to_lower_case(input_str: str) -> str:
    """Converts a string to lowercase."""

    if input_str == "":
        raise IndexError("Input must not be an empty string")

    if isinstance(input_str, str):
        return input_str.lower()

    raise TypeError("Input must be a string")


# print(to_lower_case(None))
# print(to_lower_case(1234))
print(to_lower_case("\U0001F346"))
