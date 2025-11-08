# 0900 Functions
# DRY: Don't Repeat Yourself

# 1) Declare functions
def a():
    print( "This is a basic function..." )

# Call, Invoke, Run, Evaluate, Execute functions
# a()
# a() # 1000
# a() # otro.py


# 2) Parameter & Arguments
# Function Parameters
def sum( numOne, numTwo ):
    print( numOne + numTwo )

# Function Arguments
x = 10
# sum( x, 20 )
# sum( 100, 200 )
# sum( -100, 300 )



# 3) Return values
def sayHello( name ):
    # "Hello " + name
    return "Hello " + name

message = sayHello( "Joshua" )
print( message )
message = sayHello( "Paul" )
print( message )
message = sayHello( "Peter" )
print( message )
