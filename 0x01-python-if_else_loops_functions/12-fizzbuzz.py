#!/usr/bin/python3
FIZZ = "Fizz"
BUZZ = "Buzz"


def fizzbuzz():
    for number in range(1, 101):
        if (number % 3 and number % 5):
            print("%s%s" % (FIZZ, BUZZ), end=' ')
        elif (number % 3):
            print("%s" % (FIZZ), end=' ')
        elif (number % 5):
            print("%s" % (BUZZ), end=' ')
        else:
            print("%d" % (number), end=' ')
Footer
© 2022 GitHub, Inc.
Footer navigation

    Terms
    Privacy
    Security
    Status
    Docs
