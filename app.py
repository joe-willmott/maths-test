from scripts.helper_functions import generate_equation

question_total = 5
question_count = 0

while question_count < question_total:

    question, answer = generate_equation()

    print(question)
    user_response = input("What is x in the equstion above?")

    try:
        if int(user_response) == answer:
            print("Correct!")
        else:
            print(f"Wrong, the correct answer is {answer}.")
    except ValueError as err:
        print(f"Invalid input. Please enter an integer. The correct answer is {answer}.")
    
    question_count += 1