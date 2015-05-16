"""
Test 2, problem 3.

Authors: David Mutchler, Chandan Rupakheti, their colleagues,
         and John Bender.  April 2014.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem3()


#------------------------------------------------------------------------
# Students: Use this   is_prime   function in your solution to the
#    problems in this file, as appropriate.
#    It is ALREADY DONE - no need to modify or add to it.
#------------------------------------------------------------------------
def is_prime(n):
    """
    Returns True if the given integer is prime, else returns False.
    
    Note: The algorithm used here is simple and clear but slow.
    
    Precondition:  The given argument is an integer that is at least 2.
    """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True


#------------------------------------------------------------------------
# Students: Use this   sum_of_digits   function in your solution to the
#    problems in this file, as appropriate.
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
    #           that the green doc-string is correct (it is!).
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


def test_problem3():
    """ Tests the   problem3  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3   function:')
    print('--------------------------------------------------')
    
    # Test 1 is ALREADY DONE (here).
    m = 35
    n = 4
    print()
    print('Test 1, using {} and {}:'.format(m, n))
    correct_answer = [38, 41, 43, 47]
    returned_answer = problem3(m, n)
    print('Correct answer is:  {}'.format(correct_answer))
    print('Answer returned is: {}'.format(returned_answer))
    if correct_answer != returned_answer:
        print('YOUR CODE FAILED TEST 1.')
    
    # Test 2 is ALREADY DONE (here).
    m = 119
    n = 3
    print()
    print('Test 2, using {} and {}:'.format(m, n))
    correct_answer = [119, 120, 122]
    returned_answer = problem3(m, n)
    print('Correct answer is:  {}'.format(correct_answer))
    print('Answer returned is: {}'.format(returned_answer))
    if correct_answer != returned_answer:
        print('YOUR CODE FAILED TEST 2.')
        
    # Test 3 is ALREADY DONE (here).
    m = 617
    n = 7
    print()
    print('Test 3, using {} and {}:'.format(m, n))
    correct_answer = [623, 625, 629, 632, 634, 638, 641]
    returned_answer = problem3(m, n)
    print('Correct answer is:  {}'.format(correct_answer))
    print('Answer returned is: {}'.format(returned_answer))
    if correct_answer != returned_answer:
        print('YOUR CODE FAILED TEST 3.')
        
    # Test 4 is ALREADY DONE (here).
    m = 9806
    n = 10
    print()
    print('Test 4, using {} and {}:'.format(m, n))
    correct_answer = [9806, 9811, 9815, 9820, 9824, 9833, 9839, 9842, 9848, 9851]
    returned_answer = problem3(m, n)
    print('Correct answer is:  {}'.format(correct_answer))
    print('Answer returned is: {}'.format(returned_answer))
    if correct_answer != returned_answer:
        print('YOUR CODE FAILED TEST 4.')
    
    # Test 5 is ALREADY DONE (here).
    m = 999
    n = 5
    print()
    print('Test 5, using {} and {}:'.format(m, n))
    correct_answer = [1000, 1001, 1002, 1004, 1006]
    returned_answer = problem3(m, n)
    print('Correct answer is:  {}'.format(correct_answer))
    print('Answer returned is: {}'.format(returned_answer))
    if correct_answer != returned_answer:
        print('YOUR CODE FAILED TEST 5.')


def problem3(m, n):
    """
    Returns a list of the first n integers, starting at m, for which
    the sum of their digits is prime.
    
    For example, suppose that m is 35 and n is 4. Then this function
    examines the following integers, in the order listed:
      35:  Sum of its digits is  8,   which is NOT prime.
      36:  Sum of its digits is  9,   which is NOT prime.
      37:  Sum of its digits is 10,   which is NOT prime.
      38:  Sum of its digits is 11,   which IS prime.     Got one.
      39:  Sum of its digits is 12,   which is NOT prime.
      40:  Sum of its digits is  4,   which is NOT prime.
      41:  Sum of its digits is  5,   which IS prime.     Got second.
      42:  Sum of its digits is  6,   which is NOT prime.
      43:  Sum of its digits is  7,   which IS prime.     Got third.
      44:  Sum of its digits is  8,   which is NOT prime.
      45:  Sum of its digits is  9,   which is NOT prime.
      46:  Sum of its digits is 10,   which is NOT prime.
      47:  Sum of its digits is 11,   which IS prime.     Got fourth.
    
    At that point, the function should return [38, 41, 43, 47].
    
    Another example: suppose that m is 111 and n is 3. Then this
    function examines the following integers, in the order listed:
      119:  Sum of its digits is 11,   which IS prime.
      120:  Sum of its digits is  3,   which IS prime.
      121:  Sum of its digits is  4,   which is NOT prime.
      122:  Sum of its digits is  5,   which IS prime.
    At that point, the function should return [119, 120, 122].

    See the test cases in    test_problem3   above for more examples.

    Preconditions: the arguments are positive integers.
    """
    # TODO: Implement and test this function.
    #       We supplied some tests in   test_problem3   above.
    count = 0
    retlist = []
    while count != n:
        if is_prime(sum_of_digits(m)) == True:
            retlist.append(m)
            count = count + 1 
        m = m + 1
    return retlist
    
        

#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
