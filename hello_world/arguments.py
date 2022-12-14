# arguments

def argument_function(one, two):
    print(one + " plus " + two)
argument_function("one","two")

def argument_function_two(*numbers):
    print("1 is "+numbers[1])
argument_function_two("zero","one","two")

def argument_function_three(colour1,colour2,colour3):
    print("I like "+colour3)
argument_function_three(colour1="red", colour2="green", colour3="blue")

def argument_split(**name):
    print("my first name is "+ name["firstname"])
argument_split(firstname="praneeth", lastname="kumar")


