from banner import banner
banner("LOTTERY", "Amber")

print("Welcome to Lottery. Choose a number between 1 and 999. If you choose the same as the computer you will win 10 times your bet amount.")

computer_choice = random.randint(1, 999)

balance = 20