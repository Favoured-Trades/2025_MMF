import random

fruit_list = ['apple', 'banana', 'cherry', 'dragonfruit']
colour_list = ['green', 'yellow', 'red', 'pink']

first_fruit = random.choice(fruit_list)

fruit_index = fruit_list.index(first_fruit)

first_colour = colour_list[fruit_index]

print(f"first fruit: {first_fruit} | first colour: {first_colour}")