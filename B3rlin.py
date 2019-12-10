import random, argparse

parser = argparse.ArgumentParser()

parser.add_argument('-n', help='Number of times to run', dest='num', required=False)

args = parser.parse_args()

def banner():
    logo = """ \n
 ####   ####           ##      #
 #   #     #            #
 ####    ###   # #      #     ##    ###
 #   #     #   ## #     #      #    #  #
 #   #     #   #        #      #    #  #
 ####   ####   #       ###    ###   #  #
-------------------------------------------------
Generate a project name like a 3 letter agency!
-------------------------------------------------
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
    if args.num != "":
        try:
            _num = int(args.num)
            for i in range(_num):
                B3rlin()

        except Exception, e:
            print("Error encountered... \nReview the following... " + str(e))

    else:
        print("That's not how this works... ;)")

if __name__ == "__main__":
    main()
