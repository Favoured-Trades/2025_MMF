# Functions go here
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
payment_ans = ('cash', 'credit')

want_instructions = string_check("Do you want to see the instructions? ")
print(f"You chose {want_instructions}")
pay_method = string_check("Payment method: ", payment_ans, 2)
print(f"You chose {pay_method}")



