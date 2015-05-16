"""
Test 2, problem 1.

Authors: David Mutchler, Chandan Rupakheti, their colleagues,
         and John Bender.  April 2014.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.

def main():
    """ Calls the   TEST   functions in this module. """
    test_problem1()
    

#------------------------------------------------------------------------
# Students: Use this   sum_of_digits   function in your solution to the
#    problem in this file, as appropriate.
#    It is ALREADY DONE - no need to modify or add to it.
#------------------------------------------------------------------------
def sum_of_digits(number):
    """
    Returns the sum of the digits in the given integer.
    For example, if the number is 83135, this function returns 20.
    
    Precondition: the given argument is an integer.
    """
    # Students: While you are welcome to try to understand this
    #           function definition, all you have to do is trust
    #           that the green doc-comment is correct (it is!).
    if number < 0:
        number = -number
        
    digit_sum = 0
    while True:
        if number == 0:
            break
        digit = number % 10  # Get the digit
        digit_sum = digit_sum + digit  # Accumulate it into the sum
        number = number // 10  # Get ready for the next digit
        
    return digit_sum


def test_problem1():
    """ Tests the   problem1   function. """
    # TODO: Implement this function, using it to test the NEXT
    #    function. Write the two functions in whichever order you prefer.
    #    Include at least 4 tests, i.e., 4 calls to the function to test.
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1   function:')
    print('NOTE: You should include at least FOUR tests.')
    print('--------------------------------------------------')
    seq1 = [58, 3304, 612, 5555, 13, 20010]
    seq2 = [111, 1111, 11111, 111111]
    seq3 = [12345, 98765, 444, 100, 9999999999]
    seq4 = [123, 423, 45, 2]
    print(problem1(seq1))
    print(problem1(seq2))
    print(problem1(seq3))
    print(problem1(seq4))

def problem1(sequence_of_integers):
    """
    Returns the sum of all the digits in all the items
    in the given sequence of integers.
    
    For example, if the sequence is:
       58, 3304, 612, 5555, 13, 20010
    then the sums of the digits for those integers are, respectively,
       13    10    9    20   4      3
    and the number to be returned would be
       13 + 10 + 9 + 20 + 4 + 3,
    which is 59.
    
    Other examples that you can use for testing include:
    -- If the sequence is:  [111, 1111, 11111, 111111]
                            then the correct answer is 18
                            
    -- If the sequence is:  (12345, 98765, 444, 100, 9999999999)
                            then the correct answer is 153
    
    Precondition: The argument is a sequence of nonnegative integers.
    """
    # TODO: Implement and test this function.
    # IMPLEMENTATION REQUIREMENT:
    #    Use (call) the   sum_of_digits   function
    #    defined above, as appropriate.
    
    length = len(sequence_of_integers)
    tot = 0
    for k in range(length):
        num = sum_of_digits(sequence_of_integers[k])
        tot = tot + num
    return tot
        
    
#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
