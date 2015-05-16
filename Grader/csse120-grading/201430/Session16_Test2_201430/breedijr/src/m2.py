"""
Test 2, problem 2.

Authors: David Mutchler, Chandan Rupakheti, their colleagues,
         and John Breeding.  April 2014.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.

def main():
    """ Calls the   TEST   functions in this module. """
    test_problem2a()
    test_problem2b()


def test_problem2a():
    """ Tests the   problem2a   function. """
    # TODO: Implement this function, using it to test the NEXT
    #    function. Write the two functions in whichever order you prefer.
    #    Include at least 2 tests, i.e., 2 calls to the function to test.)
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2a   function:')
    print('NOTE: You should include at least TWO tests.')
    print('--------------------------------------------------')
    list1 = [4, 66, 9, -2, 55, 0]
    list2 = [7, 22, 5, 10, -5, 9]
    print(problem2a(list1, list2))
    list3 = [100, 200, 300, 5, 4, 3, 2, 1, 0, -100, 199]
    list4 = [500, 100, 666, 0, 0, 1, 7, 7, 0, 1100, -98]
    print(problem2a(list3, list4))
    

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
    # TODO: Implement and test this function.
    return_list = []
    length = len(list1)
    for k in range(length):
        list1_k = list1[k]
        list2_k = list2[k]
        return_k = list1_k + list2_k
        return_list.append(return_k)
    return return_list


def test_problem2b():
    """ Tests the   problem2b   function. """
    # TODO: Implement this function, using it to test the NEXT
    #    function. Write the two functions in whichever order you prefer.
    #    Include at least 2 tests, i.e., 2 calls to the function to test.)
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2b   function:')
    print('NOTE: You should include at least TWO tests.')
    print('--------------------------------------------------')
    list1 = [4, 66, 9, -2, 55, 0]
    list2 = [7, 22, 5, 10, -5, 9]
    problem2b(list1, list2)
    print(list1)
    list3 = [100, 200, 300, 5, 4, 3, 2, 1, 0, -100, 199]
    list4 = [500, 100, 666, 0, 0, 1, 7, 7, 0, 1100, -98]
    problem2b(list3, list4)
    print(list3)
    

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
    # TODO: Implement and test this function.
    for k in range(len(list1)):
        list1[k] = list1[k] + list2[k]
        
    
#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
