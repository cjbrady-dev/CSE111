import random

numbers = [16.2, 75.1, 52.3]


def main():
#Calls the append_random_numbers function again with two arguments to add three numbers to numbers
    append_random_numbers(a) #one argument
    print(numbers)

    append_random_numbers(a, b) # two arguments
    print(numbers)
        

def append_random_numbers(numbers_list, quantity):
    quantity = #default of one
    x = random.uniform()

    for num in numbers:
        numbers.append(x)

        #random.choice(seq) Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.
        #random.uniform(a, b) Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
        #round(number, ndigits=None) Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.      