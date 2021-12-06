#x="Text to print"
#Block under try is "tested"
try:
    print(x)
#executed if error
except:
    print("Error occured")
#executed if the try is successfull
else:
    print("Successfully printed")
#always executed
finally:
    print("Final statement")