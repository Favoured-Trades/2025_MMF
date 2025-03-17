import pandas


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


# Currency formatting function
def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


# Main routine goes here

# Initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# Ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit charge surcharge
CREDIT_SURCHARGE = 0.05

# List to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharges = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharges
}

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
    elif age < 16:
        ticket_price = CHILD_PRICE

    # Adult ticket price is 10.50
    elif age < 65:
        ticket_price = ADULT_PRICE

    # Senior ticket price is 6.50
    elif age <= 120:
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

    print()

    # Add name, ticket cost and surcharge to 'all_lists'
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)

# Create data frame
print()
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total payable
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Work out total and profit
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# Currency formatting (uses currency function)
add_dollars =['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

print(mini_movie_frame.to_string(index=False))
print()
print(f"Total Paid: ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")