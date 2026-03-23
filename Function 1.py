import random

def get_lucky_numbers(amount: int) -> tuple[int]:

    tuple_= tuple([random.randint(1, 100) for _ in range(amount)])
    print(tuple_)
    return tuple_


try:
    amount = int(input('enter a number between 1 and 100: ? '))
    if amount not in range(1, 100 + 1):
        raise ValueError('Amount must be between 1 and 100')
    get_lucky_numbers(amount)
except ValueError as e:
    print("⚠️  That's not a valid number!")
