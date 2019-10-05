
'''
    === Learned so far ===

    1. Literals/Constants
    2. Variables
    3. Data types
        1. String 
        2. List 
        3. Tuple 
        4. Set
        5. Frozenset 
        6. Boolean
        7. Dictionary
    4. Range
    5. if elif else, For & While
    6. Operators
        1. Arithmetic
        2. Assignment
        3. Bitwise
        4. Comparison
        5. Identity
        6. Logical 
        7. Membership 
    7. Empty Objects
    8. Functions
        1. Positional Arguments 
        2. Default Arguments
        3. Arbitrary Arguments 
            1. Non-keyword
            2. Keyword
        4. Lambda
        5. Recursion

    9. Exception Handling
        try, except, else, finally
    10. File IO - file operations (Read, Write, Append, Delete)
    11. Debugging (Thonny, VS Code)
    12. JSON
        1. loads() 
        2. dumps()
    13. Requests
        1. get()
    14. In-built Functions
        dir()
        help()
        sum()
        type()
'''
cats = 5
dogs = 6

# string = "I have {1} cats and {0} dogs to walk with.".format(cats, dogs)
string = f"I have {cats} cats and {dogs} dogs to walk with."  # f string
print(string)

# doc string


def diff(v1, v2):
    '''Used to find difference between two integer values'''
    return v1 - v2


# print(diff(4, 5))

print(diff.__doc__)
