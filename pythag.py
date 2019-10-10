from banner import banner
banner("PYTHAGOREAN CALCULATOR", "Amber")

print("We will help you find the missing side of a right triangle. The lengths of the two legs are 'a' and 'b', and the length of the hypotenuse is 'c'.")
print("")

while True:
    print("Please enter the length of each side, or leave it blank if you don't know.")

    a = input("a = ")
    b = input("b = ")
    c = input("c = ")

    if a == "":
        b = float(b)
        c = float(c)
        a = ((c*c) - (b*b))**.5
        print(f"Your missing side length is {a}")
        print("")

    if b == "":
        a = float(a)
        c = float(c)
        b = ((c*c) - (a*a))**.5
        print(f"Your missing side length is {b}")
        print("")

    if c == "":
        a = float(a)
        b = float(b)
        c = ((a*a) + (b*b))**.5
        print(f"Your missing side length is {c}")
        print("")

    if input("Would you like to calculate another triangle (Y/N)? ") == "Y":
        continue
    else:
        break


