import random
import time

guessesTaken = 0
greetings = "Esi sveicināts ciparu minēšanas spēlē!"

print(greetings)
time.sleep(2)
print('Kā Tevi sauc?')

name = input()

number = random.randint(1, 10)

print('Tā, ' + name + ', es iedomāšos ciparu no 1 - 10')

time.sleep(2)

while guessesTaken < 6:
    print("Mini!")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        # There are eight spaces in front of print.
        print('Tavs minējums ir pārāk mazs..')
    if guess > number:
        print('Tavs minējums ir par lielu!')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Apsveicu, ' + name + '! Tu uzminēji manu ciparu ar ' +
          guessesTaken + ' reizēm!')

if guess != number:
    number = str(number)
    print('Tu zaudēji, cipars, kuru es iedomājos bija ' + number)
