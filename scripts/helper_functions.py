import random

def generate_equation():
    given_factor = random.randint(1, 12)
    missing_factor = random.randint(1, 2)
    product = given_factor * missing_factor

    equation = f"{given_factor}x = {product}"

    return equation, missing_factor