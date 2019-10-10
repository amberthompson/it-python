import random
from banner import banner
banner("LOTTERY", "Amber")

print("Welcome to Lottery. Choose a number between 1 and 10. If you choose the same as the computer you will win 10 times your bet amount.")
print("")
balance = 20
print(f"BALANCE: ${balance}")
print("")

while True:
    computer_choice = random.randint(1, 10)

    bet = int(input("How much would you like to bet? $"))
    print("")

    if bet > balance:
        print(f"You don't have that much money!")
        print("")
        continue

    balance = balance - bet

    number = int(input("What number do you pick? "))
    print("")

    if number > 20:
        print("Only pick a number between 1 and 10!")
        print("")
        continue

    if number > computer_choice:
        print(f"Sorry, the computer chose {computer_choice} and you chose {number}")
        print("")
        print(f"BALANCE: ${balance}")
        print("")

    elif number < computer_choice:
        print(f"Sorry, the computer chose {computer_choice} and you chose {number}")
        print("")
        print(f"BALANCE: ${balance}")
        print("")

    else:
        balance = balance + bet * 10
        print(f"You chose the same number as the computer!")
        print("")
        print(f"BALANCE: ${balance}")
        print("")

    if balance > 1000000:
        print("You won the lottery! Congrats!")

    if balance == 0:
        print("You're broke!")
        break