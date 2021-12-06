def main():
    print("hello world!")
    name = input("What is your name? ")

#Basic formatting
    print("Nice to meet you,", name)
    print("Nice to meet you," + name)
    print("Nice to meet you, {}".format(name))

if __name__ == "__main__":
    main()