from turtle import *
from random import randint
from _tkinter import *

# Defining The Functions
# 1) About Me

def about_me():
    print("You have chosen option 1 - About Me")
    print("Ok let's start with the basics")
    print()

    am1 = int(input("What is your age? "))
    if am1 < 100:
        print(f"Nice!")
    else:
        print("Oh, come on don't lie!")
    print()

    am2 = float(input("How tall are you in terms of feet? "))
    if am2 == 5:
        print("Wow nice, I'm 5 feet too!")
    else:
        print("Cool!")
    print()

    am3 = input("What is your favorite flavor of ice cream? ").lower()
    if am3 == "mango":
        print("Wow! I love Mango ice cream too!")
    else:
        print(f"{am3} is okay.")
    print()

    am4 = input("What is you dream? ").lower()
    print("I hope you will be sucessfull! ")

    print()
    exit1 = input("Do you want to return to home [Y/N] ").lower()
    if exit1 == "y":
      options()

    else:
        exit()


# 2) Jokes

def jokes():
    print("You have chosen option 2 - Jokes")
    print("I bet you'll laugh!")
    print()

    j1 = input("What did the shark say when he ate the clownfish? ")
    print(input("This tastes a little funny"))
    print()

    j2 = input("What did the pirate say when he turned 80? ")
    print(input("Aye matey"))
    print()

    j3 = input("What did the buffalo say when his son left for college? ")
    print(input("Bison"))
    print()

    j4 = input("What is an astronaut's favorite part of the keyboard? ")
    print(input("The space bar"))
    print()

    print()
    exit2 = input("Do you want to return to home [Y/N] ").upper()
    if exit2 == "Y":
      options()

    else:
      exit()

# 3) Flag Quiz

def flag():
    print("You have chosen option 3 - Flag Quiz")
    print("Let's go!")
    print()

    def recs(hexacode):
      penup()
      fillcolor(hexacode)
      begin_fill()

      for x in range(2):
        forward(200)
        left(90)
        forward(50)
        left(90)

      end_fill()
    recs("#FF671F")
    right(90)

    recs("#FFFFFF")

    forward(100)
    left(90)

    recs("#138808")
    goto(100, -45)
    pendown()
    pencolor("#06038D")
    pensize(3)

    circle(20)
    penup()
    goto(100, -25)
    pendown()
    a = 360 / 24

    for i in range(24):
        pensize(1)
        pencolor("#06038D")
        forward(15)
        backward(15)
        left(a)

    hideturtle()

    fq1 = input("#1 What is this flag : ").lower()
    if fq1 == "india" :
        print("CORRECT! That was an easy one.")

    else:
        print("INCORRECT, It was India.")

    print()
    reset()

    def rectangle(hexacode):
      penup()
      fillcolor(hexacode)
      begin_fill()
      for x in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
      end_fill()
      forward(50)

    rectangle("#002555")
    rectangle("#FFFFFF")
    rectangle("#CE1126")

    hideturtle()

    fq2 = input("#2 What is this flag : ").lower()
    if fq2 == "france" :
        print("CORRECT, Going great!")

    else:
        print("INCORRECT, It was France.")

    print()
    reset()

    def rectangle(hexacode):
      penup()
      fillcolor(hexacode)
      begin_fill()
      for x in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
      end_fill()
      forward(50)

    rectangle("#008C45")
    rectangle("#F4F9FF")
    rectangle("#CD212A")

    hideturtle()

    fq3 = input("#3 What is this flag : ").lower()
    if fq3 == "italy" :
        print("CORRECT, Third time's the lucky charm!")

    else:
        print("INCORRECT, It was Italy.")

    print()
    reset()
    goto(0, 0)

    def recs(hexacode):
      fillcolor(hexacode)
      begin_fill()

      for x in range(2):
        forward(250)
        left(90)
        forward(50)
        left(90)
      end_fill()

    recs("#FFFFFF")
    right(90)
    forward(50)
    left(90)

    recs("#1C3578")
    right(90)
    forward(50)
    left(90)

    recs("#E4181C")

    fq4 = input("#4 What is this flag : ").lower()
    if fq4 == "russia" :
      print("CORRECT, That was a guess!")

    else:
      print("INCORRECT, It was Russia!")

    print()
    reset()

    exit3 = input("Do you want to return to home [Y/N] ").upper()
    if exit3 == "Y":
        options()

    else:
        exit()


# Calculator

def calc():
    print("You have chosen option 4 - Calculator")
    print("Welcome to the Alexa Calculator!")
    print()
    question = input("Please enter A for Addition, S for Subtraction, M for Multiplication, and D for Division: ").upper()
    print()
    num1 = float(input("Please enter the first number: "))
    print()
    num2 = float(input("Please enter the second number: "))
    print()

    def sum(a, b):
        return a + b

    def difference(a, b):
        return a - b

    def product(a, b):
        return a * b

    def quotient(a, b):
        return a / b

    if question == "A":
        ans = sum(num1, num2)
        print(f"The sum of {num1} and {num2} is {ans}.")
    elif question == "S":
        ans = difference(num1, num2)
        print(f"The difference between {num1} and {num2} is {ans}.")
    elif question == "M":
        ans = product(num1, num2)
        print(f"The product of {num1} and {num2} is {ans}.")
    elif question == "D":
        ans = quotient(num1, num2)
        print(f"The quotient of {num1} and {num2} is {ans}.")
    else:
        print("That was an invalid entry. Please try again!")

    print()
    exit4 = input("Do you want to return to home [Y/N] ").upper()
    if exit4 == "Y":
        options()

    else:
        exit()

#5) Heads or Tails

def toss():
    t1 = randint(0, 1)
    if t1 == 1:
      print("Heads")

    else:
        print("Tails")

    print()
    exit5 = input("Do you want to go home or reroll [H/R]").upper()
    if exit5 == "H":
        options()

    else:
        toss()

#6) Fahrenheit to Celsius

def ftoc():
    fahrenheit = int(input("Enter temperature in Fahrenheit: "))

    celsius = (fahrenheit - 32) * 5 / 9

    print(f"The temperature in Celsius is {celsius}")

    print()
    exit6 = input("Do you want to return to home [Y/N] ").upper()
    if exit6 == "Y":
        print()
        options()

    else:
        exit()

# Menu function

def name():
  name = input("Hi, my name is Alexa. What would you like me to call you? ")
  print()
  print(f"Hello, {name}!")
  print("I can perform many things. What would you like to do today?")
  print()

def options():
    print()
    print("1) About Me")
    print("2) Joke")
    print("3) Flag Quiz")
    print("4) Calculator")
    print("5) Heads or Tails")
    print("6) Fahrenheit to Celsius")
    print("7) Exit")

    choice = int(input("Please enter your choice [1 - 7]: "))
    print()

    if choice == 1:
      about_me()
    elif choice == 2:
      jokes()
    elif choice == 3:
      flag()
    elif choice == 4:
      calc()
    elif choice == 5:
      toss()
    elif choice == 6:
      ftoc()
    elif choice == 7:
      exit()

    else:
      print("That was an invalid entry. Please try again!")

name()
options()