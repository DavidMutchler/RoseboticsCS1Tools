"""
"""
# TODO: Put a comment above.

import Tester
import importlib.util
import unittest
import re
import utilities
import copy


class ReturnedValueTester(Tester.ProjectTester):
    """
    Tests functions in modules by, for each function to be tested,
    determining whether the function returns the correct value
    and has (only) the correct side effects.

    More precisely, a ReturnedValueTester does the following for
    each module_name that it tests:
      1. Reads (from a file) a collection of Tests, where a Test is:
           -- The name of the function to call.
           -- The arguments to send to the function in that Test.
           -- The correct returned value,
                and the correct side effects (if any),
                from calling the function with those arguments.

      2. For each student to be tested:
           -- Loads the student's module_name.
           -- Applies each Test to that student's module_name.
           -- Records whether or not the student's code returned
                the correct value and had the correct side effects.
           -- Also records the nature of the failure for failed tests.
    """
    def __init__(self, what_to_grade, who_to_grade, where_to_grade,
                 verbosity=None):
        """
        Tests the given  what_to_grade  for the students specified
        by the given  who_to_grade, given that checked-out projects
        are in the given  where_to_grade  folder.

        See the superclass (ProjectTester) for a description of the
        possible values for verbosity and the effects of each.

        type: what_to_grade: WhatToGrade
        type: who_to_grade: WhoToGrade
        type: where_to_grade: str
        type: verbosity: int
        """
        super().__init__(what_to_grade, who_to_grade,
                         where_to_grade, verbosity)

        # The following are set by  initialize_tests_for_module
        #   (which is called by  do_tests).
        self.tests = {}

    def initialize_tests_for_module(self, module_name):
        """
        :type module_name: str
        """
        # TODO: Augment the above comment.

        filename = self.get_filename_with_tests(module_name)
        with open(filename, 'r') as f:
            test_text = f.read()
        self.tests[module_name] = self.parse_test_text(test_text)

    def get_filename_with_tests(self, module_name):
        """
        :type module_name: str
        """
        # TODO: Augment the above comment

        # CONSIDER: The files are text files.
        # Should they be .txt instead of .py?
        suffix = self.what_to_grade.course.suffix_for_test_files
        tail = module_name.split('.')[0] + suffix + '.py'

        head = self.where_to_grade
        head += self.what_to_grade.course.username_for_solution
        head += '/src/'

        return head + tail

    def parse_test_text(self, test_text):
        """
        For each module_name to be tested, reads the tests to be applied
        to that module_name from a text file like this example:
           @ m2 problem2a
           [[4, 66, 9, -2, 55, 0], [7, 22, 5, 10, -5, 9]]
           [11, 88, 14, 8, 50, 9]

           [[], []]
           []

           [[-1, 0, 1], [1, 0, -1]]
           [0, 0, 0]

           @ m2 problem2b
           [[4, 66, 9, -2, 55, 0], [7, 22, 5, 10, -5, 9]]
           None
           [[11, 88, 14, 8, 50, 9], [7, 22, 5, 10, -5, 9]]

           @ m2 test_problem2a # This tests a TEST function
           [] # No parameters
           None # Nothing returned

        In particular:
          -- Lines that begin with an  @  indicate a function to test,
               with the first word after the @ being the module_name name
               and the second word being the function name.
               The module_name name can be abbreviated as indicated above.
          -- A Test has 2 or 3 lines:
               -- Line 1: a list of the arguments
                    (So a function with one argument has [BLAH].)
               -- Line 2: the correct returned value
               -- Line 3 (if present): the correct value for the
                    arguments AFTER the function call.
                    (If absent, the function should not mutate
                    the argument.)
          -- Tests for a module_name must be separated by one or more
               empty lines (i.e., lines with only whitespace).
          -- A  #  character and all characters on the rest of its line
               are ignored.

        Returns a list of ReturnedValueTest objects.

        :rtype list(ReturnedValueTest)
        """
        returned_value_tests = []

        # Remove comments from the text:
        text = re.sub(r'#[^\n]*', '', test_text)

        # Functions to test begin with  @.
        functions_to_test = text.split('@')[1:]

        # Go through the functions to test.
        for function_tests in functions_to_test:

            # Line 1 of each function-to-test
            # contains the module and function names.
            line1 = function_tests.split('\n')[0]

            # TODO: In the following, implement allowing module_name
            # abbreviations like m2 for m2_... and omitting .py.
            module_and_function = line1.strip().split(' ')
            module_name = module_and_function[0]
            function_name = module_and_function[1]

            # Subsequent lines contain test cases for the function.
            # Each such test case is separated from the next one
            # by one or more empty lines.
            test_cases = ('\n').join(function_tests.split('\n')[1:])
            tests = test_cases.split('\n\n')

            # For each test:
            for test in tests:
                lines = test.split('\n')
                empty_tests = lines.count('')
                for _ in range(empty_tests):
                    lines.remove('')
                if len(lines) < 2:
                    continue

                # Line 1 contains the arguments.
                # Line 2 contains the correct returned value.
                arguments = eval(lines[0])  # FIXME: ugh!  Better way?
                returned_value = eval(lines[1])

                # Line 3 (if present) contains the correct value
                # of the arguments AFTER the function call.
                if len(lines) > 2:
                    arguments_after_test = eval(lines[2])
                else:
                    arguments_after_test = copy.deepcopy(arguments)

                rv_test = ReturnedValueTest(module_name,
                                            function_name,
                                            arguments,
                                            returned_value,
                                            arguments_after_test)
                returned_value_tests.append(rv_test)

        return returned_value_tests

    def run_tests(self, student, module_name):
        """
        :type student: str
        :rtype ReturnedValueTesterResult
        """
        # TODO: Augment the above comment.

        folder = self.where_to_grade + student + '/src/'

        tests = self.tests[module_name]
        pathname = folder + module_name

        return self.run_returned_value_tests(tests,
                                             module_name,
                                             pathname,
                                             student)

    def run_returned_value_tests(self, tests, module_name, pathname,
                                 student):
        """
        :type tests: list(ReturnedValueTest)
        :type module_name: str
        :type pathname: str [Pathname of the file to be tested]
        :type student: str
        :rtype ReturnedValueTesterResult
        """
        # TODO: Augment the above comment.

        # CRITICAL NOTE: The following is ugly.
        # The challenge is for this function to load a module_name
        # WITHOUT RETAINING the definitions loaded when this function
        # exits.  We need that because if student 1 has a correct
        # function and student 2 does not define that function at all,
        # the definition from student 1 is used.
        # There is probably a better way to solve this problem that
        # what is done below, which is to load the student's module_name
        # into a UNIQUELY-NAMED module_name and use that uniquely-named
        # module_name when running the tests. The uniquely-named module_name
        # is obtained by appending the student's username to the
        # module_name name.  That may fail if [something unforeseen].
        # A better approach would be to "wipe" the namespace when
        # this function exits, but I don't know how to do that.
        new_module_name = module_name + '_' + student

        spec = importlib.util.spec_from_file_location(new_module_name,
                                                      pathname)

        # TODO: The  load_module  method is deprecated,
        # but I do not know how to do it without that method.

        # TODO: Need to deal with inability to load or cannot read
        # tests, etc.  For now, just print the exception and move on.
        try:
            module = spec.loader.load_module(new_module_name)

        except Exception as exception:
            print('***** Student\'s code failed to load: *****')
            print(exception)

            # FIXME: There must be a better way than what follows
            # to make a test result to indicate failure to load.
            fake_test_result = unittest.TestResult()
            fake_test_result.student = student
            message = 'Syntax Error (failed to load module)'
            fake_test_result.errors = [message]
            fake_test_result.failures = []
            result = ReturnedValueTesterResult(self.what_to_grade,
                                               student,
                                               module_name,
                                               [],
                                               fake_test_result)
            return result

        test = ReturnedValueTestCase(tests, module)
        test_result = test.run()

        result = ReturnedValueTesterResult(self.what_to_grade,
                                           student,
                                           module_name,
                                           test.subtest_results,
                                           test_result)

        return result

    def score_result(self, result, student, module):
        """
        Returns a "score" -- a brief summary item -- to the given
        TesterResult (result) for the given student and module.

        For a ReturnedValueTester, the score is ...

        :rtype int
        """
        # TODO: Augment the above comment
        # TODO: Implement this method in some reasonable way
        # that yields a number in the range [0, 100].


class ReturnedValueTest():
    def __init__(self, module_name, function_name,
                 arguments, returned_value, arguments_after_test):
        self.module_name = module_name
        self.function_name = function_name
        self.arguments = arguments
        self.returned_value = returned_value
        self.arguments_after_test = arguments_after_test

    def __repr__(self):
        format_string = 'ReturnedValueTest({}, {}, {!r}, {!r}, {!r}'
        return format_string.format(self.module_name,
                                    self.function_name,
                                    self.arguments,
                                    self.returned_value,
                                    self.arguments_after_test)

# ----------------------------------------------------------------------
# TODO: Test the following more carefully:
#   1. Catches inadvertant mutations?
#   2. Are the catches for not-implemented and throws-exception correct?
#
# TODO: Find other wrong side-effects like printing.
# ----------------------------------------------------------------------


class ReturnedValueTestCase(unittest.TestCase):
    """
    A TestCase that tests a function in a module_name by running
    this TestCase's list of  ReturnedValueTest  instances on this
    TestCase's module_name.  As such, it  determines whether the function
    returns the correct value and has (only) the correct side effects.
    """
    def __init__(self, tests, module):
        """
        :type tests: list(ReturnedValueTest)
        :type module_name: module_name    [A real module_name, NOT a filename]

        """
        # Augment the above comment.
        self.subtests = tests
        self.module_name = module
        super().__init__('runSubTestsOnModule')

        self.subtest_results = []

    def runSubTestsOnModule(self):
        """
        """
        # TODO: Augment the above comment.

        # TODO: The triples below should become a class.
        # TODO: The following needs inline comments.
        # FIXME: I am uncertain re correctness of the following code.
        print('***** OUTPUT from student\'s run: *****')
        for test in self.subtests:
            f_name = test.function_name
            args = copy.deepcopy(test.arguments)
            rv = copy.deepcopy(test.returned_value)
            args_after_call = copy.deepcopy(test.arguments_after_test)

            with self.subTest():
                error = ''  # so far
                try:
                    function = getattr(self.module_name, f_name)
                except Exception as exception:
                    # FIXME: These should be ENUMSs.
                    error = 'FUNCTION_NOT_IMPLEMENTED'
                    message = 'Function {} is not implemented'
                    triple = (error, message.format(f_name), test)
                    self.subtest_results.append(triple)
                    raise exception

                try:
                    result = function(*args)
                except Exception as exception:
                    error = 'THROWS_EXCEPTION'
                    message = 'Function {} throws an exception: {}'
                    triple = (error,
                              message.format(f_name, exception), test)
                    self.subtest_results.append(triple)
                    raise exception

                try:
                    self.assertEqual(result, rv,
                                     'Wrong returned value')
                except Exception as exception:
                    error = error + 'WRONG_RETURNED_VALUE'
                    message = 'Expected: {}. Got: {}.'
                    message = message.format(rv, result)

                try:
                    self.assertEqual(args, args_after_call,
                                     'Wrong mutation')
                except Exception as exception:
                    if error:
                        error = error + ' and BAD_MUTATION'
                        message = message + ' '
                    else:
                        error = error + 'BAD_MUTATION'
                        message = ''
                    message2 = 'Expected arguments to be: {}\nGot: {}'
                    message2 = message2.format(args_after_call, args)
                    message = message + message2
                if not error:
                    error = 'PASSED_TEST'
                    message = 'OK'

                triple = (error, message, test)
                self.subtest_results.append(triple)

                if error != 'PASSED_TEST':
                    raise Exception(triple)

        print()
        print('***** RESULTS of tests: *****')
        for result in self.subtest_results:
            print(result)

        return self.subtest_results


class ReturnedValueTesterResult(Tester.TesterResult):
    """
    The result obtained by running a ChangesTester on a module_name
    for a student.  That result includes:
      -- A list of subTest results, where each subTest result
           is a triple:
             -- type of result
             -- message for the result
             -- test that was run
      -- The returned value from running the tests, which is a
           unittest.result.TestResult object.
    """
    # TODO: Augment the above comment as needed.

    def __init__(self, what_to_grade, student, module_name,
                 subtest_results, test_result):
        """
        :type what_to_grade: WhatToGrade
        :type student str
        :type module_name str
        :type subtest_results: list(tuple())
        :type test_result: unittest.TestResult
        """
        # TODO: Augment the above comment.

        super().__init__(what_to_grade, student, module_name)

        self.subtest_results = subtest_results
        self.test_result = test_result

    def __repr__(self):
        args = 'what_to_grade  student  module_name'
        args += ' subtest_results  test_result'
        return utilities.generic_repr(self, args)

    def __str__(self):
        # TODO: I probably should not return representations
        # of BOTH self.test_result AND self.subtest_results.
        # Further, this really is NOT the best representation.
        if self.test_result.wasSuccessful():
            result = '  {:8}: OK'.format(self.student)
        else:
            result = '  {:8} ERRORS: {}'.format(self.student,
                                                self.test_result.errors)
            result += '  {:8} FAILURES: {}'.format(self.student,
                                                   self.test_result.failures)

        result += '\n'

        for subtest in self.subtest_results:
            if subtest[0] == 'PASSED_TEST':
                continue
            format_string = '{:8} failed a test of {:9}: {}\n'
            result += format_string.format(self.student,
                                           subtest[2].function_name,
                                           subtest)
        return result

# ----------------------------------------------------------------------
# The following class tests a function that begins   test_blah.
# It is correct (probably) but needs to be converted to the form
# of the above class.
# ----------------------------------------------------------------------


# class TesterTest(unittest.TestCase):
#     """
#     A subclass of unittest.TestCase for testing whether a TESTING
#     function calls the function to be tested enough times.
#     For example, it might test whether  test_blah() calls blah(...)
#     at least 4 times (for 4 tests).
#     A TesterTest:
#       -- Has a module_name (NOT name of moudule -- the module_name itself)
#       -- Has the name X of a function in that module_name
#       -- Has a positive integer N
#     and
#       -- Runs test_X() [where X is the name of the function]
#            (and catches and ignores any exception)
#       -- Counts how many times X is called
#     The test passes if that count >= N.  Else the test fails.
#     """
#
#     def __init__(self, module_name, name_of_test_function,
#                  name_of_function_it_tests, min_number_of_tests):
#         self.module_name = module_name
#         self.name_of_test_function = name_of_test_function
#         self.name_of_function_it_tests = name_of_function_it_tests
#         self.min_number_of_tests = min_number_of_tests
#         super().__init__('runTestsOnModule')

#         self.number_of_calls = 0
#         test_function_name = 'test_' + self.function_name
#         try:
#             test_function = getattr(self.module_name, test_function_name)
#
#         except:
#             message = 'Function {} is not implemented'
#             self.fail(message.format(test_function_name))
#             return


#     def runTestsOnModule(self):
#         number_of_calls = 0
#
#         # If the test_function or the function it tests does not exist,
#         # fail immediately.
#         try:
#             test_function = getattr(self.module_name,
#                                     self.name_of_test_function)
#         except:
#             message = 'Function {} is not implemented'
#             self.fail(message.format(test[0]))
#
#             function_it_tests = getattr(self.module_name,
#                                     self.name_of_function_it_tests)
#         # Redefine the function the test_function tests
#         # to include a counter.
#
#         # Call the test_function, catching and ignoring any exceptions.
#
#         # Test passes if number_of_calls >= min_number_of_tests
#
#         def count_calls(function_name, ):
#             self.number_of_calls = self.number_of_calls + 1
#             try:
#
#
#                 message = 'Function {} is not implemented'
#             self.fail(message.format(test_function_name))
#             return
#
#
#
#             with self.subTest(i=test):
#                 try:
#                     function = getattr(self.module_name, test[0])
#                 except:
#                     message = 'Function {} is not implemented'
#                     self.fail(message.format(test[0]))
#                     continue
#                 try:
#                     result = function(*test[1])
#                 except Exception as e:
#                     message = 'Function {} throws an exception: {}'
#                     self.fail(message.format(test[0], e))
#                     continue
#                 self.assertEqual(result, test[2], 'Wrong returned value')
#                 self.assertEqual(test[1], test[3], 'Wrong mutation')


# ----------------------------------------------------------------------
# Code below here was once useful but is no longer correct.
#
# CONSIDER: Maybe rejuventate the following when UnitTester
# becomes operative again.
# ----------------------------------------------------------------------
