def main():
    name = "Martin"

#Basic formatting
    print ("Welcome to", name)
    print("Welcome to " + name)
    print ("Welcome to {}".format("Nathalie"))
    print ("Welcome to {}".format(name))
    print("Welcome to " + name + " and " + "Laurence")
    print ("Welcome to {} and {}".format(name,"Laurence"))

# Using variable or keyword arguments inside the Placeholder
    print("Welcome to {var1}".format(var1="Martin"))
    print("Welcome to {var1} {var2}".format(var1="Martin", var2="Dupont"))
    print("Welcome to {var2} {var1}".format(var1="Martin", var2="Dupont"))

#Using index or positional argument
    print("Welcome to {0} {1}".format("Martin", "Dupont"))
    print("Welcome to {1} {0}".format("Martin", "Dupont"))

# ----------------- More complex -----------------
#Formatting inside Placeholders
    print("The value is : {:.2f}".format(40))
    print("The scientific value is : {:e}".format(40))
    print("The value is : {:,}".format(1000000))
    print("The value is : {:%}".format(0.80))
    print("The binary to decimal value is : {:d}".format(0b0011))
    print("The binary value is : {:b}".format(500))

if __name__ == "__main__":
    main()