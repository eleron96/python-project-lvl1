#!/usr/bin/python -tt
import sys
from random import randint
import prompt


def brain_even():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    i = 1
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while i <= 3:
        for _ in range(10):
            value = randint(0, 10)

        print("Question: " + str(value))
        useranswer = input('Your answer: ')

        if (value % 2) == 0:
            if useranswer == "yes":
                print("Correct!")
                i += 1
            else:
                sys.exit("'yes' is wrong answer ;(. Correct answer was 'no'.\n"+f"Let's try again,{name}!")


        else:
            if useranswer == "no":
                print("Correct!")
                i += 1
            else:
                sys.exit("'yes' is wrong answer ;(. Correct answer was 'no'.\n"+f"Let's try again,{name}!")
    print(f"Congratulations, {name}!")


def main():
    brain_even()


if __name__ == '__main__':
    main()
