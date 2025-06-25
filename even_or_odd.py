# -*- coding: utf-8 -*-
def check_even_or_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

num = int(input("数字を入力してください: "))
check_even_or_odd(num)


def check_sign(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

if __name__ == "__main__":
  num = int(input("数字を入力してください: "))
  check_even_or_odd(num)
  check_sign(num)