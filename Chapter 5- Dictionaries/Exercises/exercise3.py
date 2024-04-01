'''Chapter 5 Exercise 3: Glossary 2'''


glossary = {
    "variable": "A name that refers to a value.",
    "function": "A named sequence of statements that performs a computation.",
    "loop": "A control flow statement for executing a block of code repeatedly.",
    "list": "A collection of items that are ordered and mutable.",
    "tuple": "A collection of ordered and immutable items.",
    "method": "A function associated with an object.",
    "dictionary": "A collection of key-value pairs that are unordered and mutable.",
    "class": "A blueprint for creating objects, providing initial values for state, and implementations of behavior.",
    "module": "A file containing Python code.",
    "tuple": "A collection of ordered and immutable items.",
    "method": "A function associated with an object.",
    "argument": "A value passed to a function or method when calling it.",}

    # Iterate over the dictionary and print each term along with its definition
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n") 