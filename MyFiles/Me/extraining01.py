def func1(arg1, arg2=0):
    if arg2 == 0:
        return (arg1 * 4)
    else:
        return (arg1*2 + arg2*2)

def func2():
    x = 5
    y = 20
    x, y = y, x
    print(x, y)

def func3():
    for num in range(1, 10):
        #% is modulo operator
        if (num % 2) == 0:
            print(num)

def func4():
    x=2
    while (x < 7):
        x = x + 1
        if x == 5: continue
        print(x)

def func5():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        if d == "Thu": break
        print(d)

def main():
    print("start")

    # Calls to func 1
    v_prec = func1(4,5)
    v_psq = func1(6)
    print("prec : ", v_prec, "psq : ", v_psq)

    #call to func 2
    func2()

    #call to func 3
    func3()

    #call to func 4
    func4()

    #call to func 5
    func5()

if __name__ == "__main__":
    main()