"""
Test 2, problem 2.

Authors: David Mutchler, Chandan Rupakheti, their colleagues,
         and SOLUTION by David Mutchler.  April 2014.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem2a()
    test_problem2b()


def test_problem2a():
    """ Tests the   problem2a   function. """
    # DONE: Implement this function, using it to test the NEXT
    #    function. Write the two functions in whichever order you prefer.
    #    Include at least 2 tests, i.e., 2 calls to the function to test.)
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2a   function:')
    print('NOTE: You should include at least TWO tests.')
    print('--------------------------------------------------')

    seq1 = [4, 66, 9, -2, 55, 0]
    seq2 = [7, 22, 5, 10, -5, 9]
    correct_answer = [11, 88, 14, 8, 50, 9]
    print()
    print('Test 1, using {} and {}:'.format(seq1, seq2))
    print('Correct answer is:  {}'.format(correct_answer))
    print('Answer returned is: {}'.format(problem2a(seq1, seq2)))

    seq1 = [100, 200, 300, 5, 4, 3, 2, 1, 0, -100, 199]
    seq2 = [500, 100, 666, 0, 0, 1, 7, 7, 0, 1100, -98]
    correct_answer = [600, 300, 966, 5, 4, 4, 9, 8, 0, 1000, 101]
    print()
    print('Test 2, using {} and {}:'.format(seq1, seq2))
    print('Correct answer is:  {}'.format(correct_answer))
    print('Answer returned is: {}'.format(problem2a(seq1, seq2)))


def problem2a(list1, list2):
    """
    Returns a new list that is the item-by-item sum
    of the two given lists.

    For example, if the given lists are:
        [4,  66,  9, -2,  55,  0]
        [7,  22,  5, 10,  -5,  9]
    then the returned list should be:
        [11, 88, 14,  8,  50,  9]

    Another example:  if the given lists are:
       [100, 200, 300, 5, 4, 3, 2, 1, 0, -100, 199]
       [500, 100, 666, 0, 0, 1, 7, 7, 0, 1100, -98]
    then the returned list should be:
       [600, 300, 966, 5, 4, 4, 9, 8, 0, 1000, 101]

    Preconditions: the given lists are lists of numbers
                   and their lengths are the same.
    """
    # DONE: Implement and test this function.
    new_list = []
    for k in range(len(list1)):
        new_list.append(list1[k] + list2[k])

    return new_list


def test_problem2b():
    """ Tests the   problem2b   function. """
    # DONE: Implement this function, using it to test the NEXT
    #    function. Write the two functions in whichever order you prefer.
    #    Include at least 2 tests, i.e., 2 calls to the function to test.)
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2b   function:')
    print('NOTE: You should include at least TWO tests.')
    print('--------------------------------------------------')

    seq1 = [4, 66, 9, -2, 55, 0]
    seq2 = [7, 22, 5, 10, -5, 9]
    correct_answer = [11, 88, 14, 8, 50, 9]
    print()
    print('Test 1, using {} and {}:'.format(seq1, seq2))
    print('Correct answer is:        {}'.format(correct_answer))
    problem2b(seq1, seq2)
    print('Mutated list1 is:         {}'.format(seq1))
    print('Unmutated list2 remains:  {}'.format(seq2))

    seq1 = [100, 200, 300, 5, 4, 3, 2, 1, 0, -100, 199]
    seq2 = [500, 100, 666, 0, 0, 1, 7, 7, 0, 1100, -98]
    correct_answer = [600, 300, 966, 5, 4, 4, 9, 8, 0, 1000, 101]
    print()
    print('Test 2, using {} and {}:'.format(seq1, seq2))
    print('Correct answer is:        {}'.format(correct_answer))
    problem2b(seq1, seq2)
    print('Mutated list1 is:         {}'.format(seq1))
    print('Unmutated list2 remains:  {}'.format(seq2))


def problem2b(list1, list2):
    """
    MUTATES the first of the two given lists so that it becomes
    the item-by-item sum of the two given lists.

    For example, if the given lists are:
        [4, 66, 9, -2, 55, 0]
        [7, 22, 5, 10, -5, 9]
    then the first of those two lists should mutate into:
        [11, 88, 14, 8, 50, 9]

    Does NOT return anything explicitly (so None is returned implicitly).

    Preconditions: the given lists are lists of numbers
                   and their lengths are the same.
    """
    # DONE: Implement and test this function.
    for k in range(len(list1)):
        list1[k] = list1[k] + list2[k]

#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
