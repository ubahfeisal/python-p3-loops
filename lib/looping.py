#!/usr/bin/env python3

# def happy_new_year():
#     # code goes here!
#     pass

# def square_integers(int_list):
#     # code goes here!
#     pass

# def fizzbuzz():
#     # code goes here!
#     pass


def fizzbuzz():
    i = 1
    while i <= 100:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1
fizzbuzz()
