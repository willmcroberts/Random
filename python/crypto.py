
def main():
    inp = input("Enter message: ")

    print()
    print("Choose cypher:")
    print("0) quit")
    print("1) Ceaser")
    print("2) Substitution")
    print("3) Modern")
    print()

    keepGoing = True

    while(keepGoing):
        choice = input("Enter option: ")
        print()
        if choice == "0":
            keepGoing = False
        elif choice == "1":
            ceaser(inp)
        elif choice == "2":
            sub(inp)
        elif choice == "3":
            modern(inp)
        else:
            print("invalid option")
    
def ceaser(string):
    string = string.lower()

    shift = input("Enter shift: ")

    alpha = "abcdefghijklmnopqrstuvwxyz.!, "

    cypherString = ""

    for i in string:
        letter = alpha.find(i)
        letterShift = (int(letter) - int(shift))
        newLetter = alpha[letterShift]
        cypherString += newLetter
    
    print()
    print("Encrpyted string: " + cypherString)
    print()

def sub(string):
    print("substituion")

def modern(string):
    print("modern")

main()
