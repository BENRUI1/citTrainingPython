import configparser

#read ini file
parser = configparser.ConfigParser()
print(type(parser))
parser.read('configparser.ini')

v_parameter1_1=parser['block1']['parameter1']
v_parameter1_2=parser['block1']['parameter2']
v_parameter2_1=parser['block2']['parameter1']
v_parameter2_2=parser['block2']['parameter2']
v_parameter2_3=parser['block2']['parameter3']

print()

def main():
    print("Block 1 - ¨Parameter 1 : {}".format(v_parameter1_1))
    print("Block 1 - ¨Parameter 2 : {}".format(v_parameter1_2))
    print("Block 2 - ¨Parameter 1 : {}".format(v_parameter2_1))
    print("Block 2 - ¨Parameter 2 : {}".format(v_parameter2_2))
    print("Block 2 - ¨Parameter 3 : {}".format(v_parameter2_3))

if __name__ == "__main__":
    main()