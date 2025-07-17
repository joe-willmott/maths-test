import random

def generate_equation():
    """
    Generates two random integers and calculates their product.
    Returns a tuple where the first item is an equation string with on integer replaced by 'x' and the second item is the value of x.
    """
    given_factor = random.randint(1, 12)
    missing_factor = random.randint(1, 12)
    product = given_factor * missing_factor

    equation = f"{given_factor}x = {product}"

    return equation, missing_factor