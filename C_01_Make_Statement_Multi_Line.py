# Functions go here
def make_statement(statement, decoration, lines):
    """Creates headings (3 lines), subheadings (2 lines) and emphasised text
     and mini-headings (1 line). Only use emojis for single line statements"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    elif lines == 3:
        print(top_bottom)
        print(middle)
        print(top_bottom)
    else:
        print("Unsupported amount")
        print(middle)


# Main routine goes here

statement = input("Statement: ")
lines = int(input("How many lines: "))

if lines == 1:
    make_statement(f"{statement}", "😊", 1)
elif lines == 2:
    make_statement(f"{statement}", "-", 2)
elif lines == 3:
    make_statement(f"{statement}", "=", 3)
else:
    print("Something went wrong")