#Sum
def sum(x):
    if x == 0: #базовый случай
        return x
    if x == 1: #базовый случай
        return x
    else:
        return x + sum(x-1) #рекурсивный случай,нахождение суммы

x = sum(5)
print(x)

#Factorial
def factorial(x):
    if x == 1: #базовый случай
        return x
    else:
        return x * factorial(x - 1) #рекурсивный случай,нахождение факториала
x = factorial(5)
print(x)

#Countdown
import time
def countdown(x):
    time.sleep(1)
    if x == 0: #базовый случай
        return x
    if x == 1: #базовый случай
        return x
    else:
        print(x)
        return countdown(x - 1) #рекурсивный случай
x = countdown(5)
print(x)