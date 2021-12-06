#
# Example file for working with functions
#

# define a basic function

def func1():
    print("I am a function")

# function that takes arguments

def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value

def cube(x):
    #print(x*x*x)
    return x*x*x

# function with default value for an argument

def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# function with variable number of arguments

def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

def main():
    #Call func - function without arguments
    func1()
    #Call func2 with arguments
    func2(10, 20)
    #Call function cube and assign result to a variable
    v_cube = cube(4)
    print(v_cube)
    #call function cube inside a print statement
    print(cube(3))

    # ----------------- More complex -----------------

    #Example of fuctions that has an "optional" argument
    print(power(2))
    print(power(2, 3))
    print(power(x=3, num=2))
    #function with a variable number of arguments
    print(multi_add(4, 5, 10, 4))

if __name__ == "__main__":
    main()
