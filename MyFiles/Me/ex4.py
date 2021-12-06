#x="Text to print"
#Block under try is "tested"
try:
    print(x)
#executed if error
except:
    print("Error occured")
else:
    print("Success")
finally:
    print("End")