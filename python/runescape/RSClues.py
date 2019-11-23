# Collin Bauer


# prints available options provided by the options menu
def printOptions(options):
    for option in options:
        print(option)

# inputs a string
# prints all possible offset cyphers for said string
def cypher():
    cypher = input("Please input cypher: ").upper()

    for i in range(26):
        temp = list(cypher)
        for j in range(len(temp)):
            if temp[j] != " ":
                val = (ord(temp[j]) - 65 + i) % 26 + 65
            else:
                val = ord(" ")
            temp[j] = chr(val)

        new = ""
        new = new.join(temp)
        print("{:2}: {}".format(i,new))


def anagram():
    print("This has not been implemented yet!")
        

def main():
    print("This program handles a number of different clue scroll related questions.")

    # build options menu
    options = []
    options.append("  0: List available options")
    options.append("  1: Decode a cypher")
    options.append("  2: Unwrap an anagram")
    options.append("  x: Quit program")
    printOptions(options)

    # while loop
    cont:bool = True
    while cont:
        arg = str(input("Select an option: ")[0])
        # argument "lookup" table
        if arg == '0':
            printOptions(options)
        elif arg == '1':
            cypher()
        elif arg == '2':
            anagram()
        elif arg == 'x':
            cont = False
        else:
            print("Not a valid option.")
            
    # end while
    
    print("Done.")


main()
    
