import random

def banner():
    logo = """ \n
 ####   ####           ##      #
 #   #     #            #
 ####    ###   # #      #     ##    ###
 #   #     #   ## #     #      #    #  #
 #   #     #   #        #      #    #  #
 ####   ####   #       ###    ###   #  #

Generate a project name like a 3 letter agency!
"""
    print(logo)

def generate_random_word(infile):
    with open(infile) as f:
        file_contents = f.read()
    lines = file_contents.splitlines()
    line_number = random.randrange(0, len(lines))
    return lines[line_number]

def B3rlin():
    codename = generate_random_word("adjectives.txt") + generate_random_word("nouns.txt")
    _codename = codename.upper() + "\n"
    print("Your new codename is: " + _codename)

def main():
    banner()
    B3rlin()

if __name__ == "__main__":
    main()
