# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


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

        print("Please choose from: ", valid_answers)


def instructions():
    make_statement("Instructions", "ℹ️")

    print('''
    
For each ticket holder enter ...
- Their name
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate 
the ticket cost (and the profit).

Once you have either sold all of the tickets or entered the 
exit code ('xxx'), the program will display the ticket 
sales information and write the data to a text file.

It will also choose one lucky ticket holder who 
wins the draw (their ticket is free).  
    
    ''')


def not_blank(question):
    """Checks that a user response is not blank"""

    # Repeats until return
    while True:
        response = input(question).strip()

        if response != "":
            return response

        print("Sorry, this can't be blank. Please enter something.\n")


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


# Main routine goes here
# Initialise ticket numbers
max_tickets = 5
tickets_sold = 0

# Initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

make_statement("Mini-Movie Fundraiser Program", "🍿")

print()

want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

while tickets_sold < max_tickets:
    print()
    name = not_blank("Name: ")

    # If name is exit code
    if name == "xxx":
        break

    age = int_check("Age: ")

    if age < 12:
        print(f"Sorry, {name} is too young for this movie")
        continue
    elif age > 120:
        print(f"Sorry, {name} is dead")
        continue
    else:
        pass

    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"You chose {pay_method}")

    tickets_sold += 1


if tickets_sold == max_tickets:
    print(f"You have sold all the tickets (ie: {max_tickets} tickets")
else:
    print(f"You have sold {tickets_sold} / {max_tickets} tickets.")
