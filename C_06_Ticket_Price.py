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

# Ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit charge surcharge
CREDIT_SURCHARGE = 0.05

# Loop
while True:
    name = not_blank("Name: ")
    if name == "xxx":
        break

    age = int_check("Age: ")

    if age < 12:
        print(f"{name} is too young")
        continue

    # Child price is 7.50
    elif 12 <= age < 16:
        ticket_price = CHILD_PRICE

    # Adult ticket price is 10.50
    elif 16 <= age < 65:
        ticket_price = ADULT_PRICE

    # Senior ticket price is 6.50
    elif 65 <= age <= 120:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is dead")
        continue


# Ask user for payment method ( cash/ credit / ca / cr )
    pay_method = string_check("Payment method: ", payment_ans, 2)

    if pay_method == "cash":
        surcharge = 0

    # If payment by credit, calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    # Calculate total payable
    total_to_pay = ticket_price + surcharge

    print(f"{name}'s ticket cost ${ticket_price:.2f}, they paid by {pay_method} "
          f"so the surcharge is ${surcharge:.2f}\n"
          f"The total payable is ${total_to_pay:.2f}\n")
