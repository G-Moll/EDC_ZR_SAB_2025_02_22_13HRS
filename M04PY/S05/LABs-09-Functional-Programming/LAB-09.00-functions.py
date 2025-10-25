# 0900 Functions
# DRY: Don't Repeat Yourself

# 1) Declare functions
def a():
    print( "This is a basic function..." )

# Call, Invoke, Run, Evaluate, Execute functions
a()


# 2) Parameter & Arguments
# Function Paremeters
def sum( numOne, numTwo ):
    print( numOne + numTwo )

# Function Arguments
sum( 10, 20 )



# 3) Return values
def sayHello( name ):
    return "Hello " + name

message = sayHello( "Joshua" )
print( message )
