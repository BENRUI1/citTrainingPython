import os

def main():
    filename = input("Enter filename : ")

    try:
        f= open(filename,'r')
        v_del_file = input("File exists, do you want to replace it? (Y/N)")
        if v_del_file == "Y":
            os.remove(filename)
            v_operation = "write"
        else:
            v_operation="read"
    except:
        v_operation="write"

    if v_operation == "write":
        f=open(filename,'w')

    if v_operation == "read":
        fl = f.readlines()
        print(fl)
    else:
        name = True
        while name:
            name = input("Enter name : ")
            f.write(name + "\n")

    f.close()


if __name__ == "__main__":
    main()