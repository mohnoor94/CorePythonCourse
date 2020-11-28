def multiply(num1, num2, *numbers):
    """
    Multiply all values and return the result.
    """
    result = num1 * num2
    
    if len(numbers):
        for num in numbers:
            result *= num

    return result


def avg(*numbers):
    """
    Return the average of all numbers.
    """
    return sum(numbers) / len(numbers) if len(numbers) else 0