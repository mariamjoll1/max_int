
num_int = int(input("Input a number: "))    # Do not change this line
max_int = num_int

while num_int != 0:
    num_int = int(input("Input a number: "))
    max_int = num_int
    if num_int > 0:

        for max_int in num_int:
            if max_int > 0:
                max_int = max(num_int)
                print("The maximum is: ", max_int)
            else:
                print("error")

#print("The maximum is", max_int)    # Do not change this line
