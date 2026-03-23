import random
#Function 1
def get_lucky_numbers(amount: int) -> tuple[int]:
    """
    :param amount:
    :return: tuple of random numbers
    """

    tuple_= tuple([random.randint(1, 100) for _ in range(amount)])
    print(tuple_)
    return tuple_

#Function 2
def input_until_lucky(lucky_numbers: tuple) -> int:
    """

    :param lucky_numbers:
    :return:
    """
    number_of_attempts=0
    while True:
        try:
            lucky_number = int(input('guss the lucky numbers: '))
            if lucky_number in lucky_numbers:
                number_of_attempts += 1
                print(f'NICE!! number of attempts is ')
                break

            else:
                print("worng")
                number_of_attempts += 1
        except:
            print("⚠️  That's not a valid number!")
    return number_of_attempts

print(input_until_lucky(get_lucky_numbers(7)))
