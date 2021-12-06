#Global vs. local variables in functions

def someFunction():
#switch global to local by removing comment
    #global f
    f1 = "def"
    print(f1)

def main():
    # Declare a variable and initialize it
    #global f
    f = 0
    print(f)

    # re-declaring the variable works
    f = "abc"
    print(f)

    someFunction()
    print(f)

    #del f
    #print (f)

if __name__ == "__main__":
    main()