"""
Common tips and tricks dealing with iteration.
"""

# When looping over a list of numbers
# Use the built-in range function to preserve memory
# Each value is produced one at a time
for i in range(5):
    print(i)

# To loop over a collection
# Use Python's for-each loop
names = ["Ben", "Andrew", "Ashley"]

for name in names:
    print(name)

# To loop over a collection backwards
for name in reversed(names):
    print(name)

# To loop over a collection but with indicies
# Use the built-in enumerate function
for i, name in enumerate(names):
    print(f"names[{i}] = {name}")

# To loop over two collections
# Use the built-in zip function to preserve memory
# Each value is produced one at a time
colors = ["red", "blue", "yellow", "pink"]

for name, color in zip(names, colors):
    print(f"{name} likes {color}")

COUNTER = 0

# When calling a function until a sentinel value
def read_from_file_until_sentinel():
    """
    Mock function to simlulate reading from a file
    until a sentinel of an empty-string.
    """
    global COUNTER
    COUNTER += 1

    if COUNTER == 1:
        return "hello"
    if COUNTER == 2:
        return "world"

    return ""


for word in iter(read_from_file_until_sentinel, ""):
    print(word)

# Replace boolean variables with else statements
# for the corresponding if statement inside of a iteration.
for color in colors:
    if color == "green":
        break
else:
    print("Green not in colors!")
