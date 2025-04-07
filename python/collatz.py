def main():
    print("Enter a number:", end = " ")
    x = int(input())
    counter = 1

    while (x > 1):
        counter = counter + 1
        if (x % 2 == 0):
            x = x / 2
            print(int(x), end = " ") 
        else:
            x = ((3 * x) + 1)
            print(int(x), end = " ")

    print("    COUNT:", counter)

    print("New number (y/n):", end = " ")
    option = input()
    
    if (option == "y"):
        main()
    else:
        print("Goodbye")
main()
