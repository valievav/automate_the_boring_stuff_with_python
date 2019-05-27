import random

messages = [
    "Not likely",
    "Yes, sure",
    "Decidedly so",
    "Future is foggy",
    "Try next time",
    "100% yes"
]

index = random.randint(0, len(messages) - 1)
print(messages[index])
