# Functions go here
def int_check(question, exit_code=None):
    """Checks users enter an integer"""

    error = "Oops - please enter an integer."

    while True:

        response = input(question)
        if response == exit_code:
            return response

        try:
            # Return the response if it's an integer
            response = int(response)

            return response

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    # Repeats until return
    while True:
        response = input(question).strip()

        if response != "":
            return response

        print("Sorry, this can't be blank. Please enter something.\n")


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or the 'n'
    letters of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # Check if the response is the entire word
            if response == item:
                return item

            # Check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print("Please choose from:", valid_answers)


# Main routine goes here

# Initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# Loop
while True:
    name = not_blank("Name: ")
    if name == "xxx":
        break

    age = int_check("Age: ")

    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is dead")
        continue
    else:
        pass

    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"You chose {pay_method}")
