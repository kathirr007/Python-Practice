def calculate_percentage(part: int, whole: int) -> int:
    """
    Calculates the percentage of a part relative to a whole.

    Args:
        part: The part value (number).
        whole: The total value (number).

    Returns:
        The percentage or None if an error occurs.

    Raises:
        TypeError: If part or total are not number.
        ZeroDivisionError: If total is zero.
    """

    if not isinstance(part, int) or not isinstance(whole, int):
        raise TypeError("Part and Whole must be number.")

    if whole == 0:
        raise ZeroDivisionError("Whole cannot be zero.")

    try:
        percentage = (part / whole) * 100
        return int(percentage)
    except (
        TypeError,
        ZeroDivisionError,
    ) as e:  # Catch exceptions and re-raise or handle
        print(f"An error occurred: {e}")  # Or log it
        raise e  # or raise the exception: raise e


print(calculate_percentage(25, 100))  # 25.0
print(calculate_percentage(10, 50))  # 20.0
print(calculate_percentage(3, 10))  # 30.0
print(calculate_percentage(1, 2))  # 50.0
# calculate_percentage(1, "0")
