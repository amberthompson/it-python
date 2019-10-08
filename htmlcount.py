from banner import banner
import os

def load(filename):
    data = []
    print(f"..... loading from {filename}")
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data

def count_tags(text):
    tag_count = 0
    previous_char = None
    for char in text:
        if char != "/" and previous_char == "<":
            tag_count +=1
        previous_char = char
    return tag_count

banner("HTML TAG COUNTER", "AMBER")
print("Welcome to the HTML tag counter.")
while True:
    filename = input("Please enter the name of the HTML file: ")
    data = load(filename)
    count = 0
    for line in data:
        count += count_tags(line)
    print(f"That html file has {count} tags.")
    print("")

    if input("Would you like to enter another file (Y/N)? ").upper == "Y":
        print("")
        continue
    else:
        break


