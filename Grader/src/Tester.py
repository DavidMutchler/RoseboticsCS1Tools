"""
"""
# TODO: Put a comment above.

import abc
import utilities


class Tester(object):
    """ Abstract base class for testing student code. """
    # This class exists for future expansion beyond a ProjectTester.
    pass


class ProjectTester(Tester):
    """
    Abstract base class for testing student code that is in the form
    of modules within a project.
    """
    # TODO: Maybe clarify/augment the above comment.

    DEFAULT_VERBOSITY = 40

    def __init__(self, what_to_grade, who_to_grade, where_to_grade,
                 verbosity=None):
        """
        -- Tests the given  what_to_grade,
        -- for the students specified by the given  who_to_grade,
        -- given that checked-out projects are in the given
               where_to_grade  folder.
        -- The  verbosity  controls the amount of data that is PRINTED.
             (The RETURNED value is always the complete results).
             Verbosity of:
               -- 0  -> Print nothing.
               -- 10 -> Additionally, as each student is tested,
                          print a message indicating that that student
                          is being tested.
               -- 20 -> Additionally, as each student is tested,
                          print the student's output.
               -- 30 -> Additionally, as each student is tested,
                          print a brief form of the test results
                          for that student.
               -- 40 -> Print a brief form of the test results after
                          completing the tests for all the students.
               -- 50 -> Ditto, but print a more complete form
                          of the test results.


        type: what_to_grade: WhatToGrade
        type: who_to_grade: WhoToGrade
        type: where_to_grade: str
        type: verbosity: int
        """
        self.what_to_grade = what_to_grade
        self.who_to_grade = who_to_grade
        self.where_to_grade = where_to_grade
        self.verbosity = verbosity or ProjectTester.DEFAULT_VERBOSITY

        # Note:  The value for the  results  data instance is set after
        # the Tester finishes its work (from do_tests_on_students),
        # not when the Tester is constructed.
        self.results = None

        # TODO: Use an ENUM (with sensible names)
        # for the verbosity magic numbers.

    def __repr__(self):
        args = 'what_to_grade who_to_grade where_to_grade'
        args += ' verbosity results'
        return utilities.generic_repr(self, args)

    def do_tests_on_students(self):
        """
        Does this Tester's tests on this Tester's  what_to_grade
        for ALL of the students specified by its  who_to_grade.
        Prints appropriate messages in doing so.

        Returns a dictionary of dictionaries that maps each student,
        then each module_name, to the TesterResult (actually, a subclass
        of TesterResult) for that student and module_name.

        For example, this code snippet:
           results = do_tests_on_students()
           result = results['mutchler']['m2.py']
           print(type(result))
        prints  ChangesTesterResult  if this Tester is a ChangesTester.

        :rtype dict(dict(TesterResult))
          [actually, a subclass of TesterResult, not TesterResult]
        """
        # For each module_name, initialize its tests.
        for module in self.what_to_grade.modules:
            self.initialize_tests_for_module(module)

        # For each student, do this Tester's tests on that student.
        self.results = {}
        for student in self.who_to_grade.students:
            self.results[student] = self.do_tests_on_student(student)

        # Add a "score" for each student/module that summarizes
        # each result (typically, as a single number in [0, 100]).
        self.score_results()

        # Print results if verbosity is high enough.
        if self.verbosity >= 40:
            self.print_results(self.results)

        # TODO: Implement verbosity >= 50 (which prints a more complete
        # version of the results.

        return self.results

    def do_tests_on_student(self, student):
        """
        For the given student, does this Tester's tests on each of the
        modules in this Tester's  what_to_grade.  Returns a dictionary
        that maps each module_name to the TesterResult (actually, a subclass
        of TesterResult) for that student and module_name.

        For example, this code snippet:
           results = do_tests_on_student('mutchler')
           result = results['m2.py']
           print(type(result))
        prints  ChangesTesterResult  if this Tester is a ChangesTester.

        :rtype dict(TesterResult)
          [actually, a subclass of TesterResult, not TesterResult]
        """
        if self.verbosity >= 10:  # TODO: Fix this magic number
            print()
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('TESTING:', student)
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        # TODO: Implement verbosities in the range [20, 30).
        # These would send the student's output to /dev/null
        # (or, better, to a log file).
        # Maybe the student's error-output too.

        self.initialize_tests_for_student(student)

        result = {}
        for module in self.what_to_grade.modules:
            result[module] = self.run_tests(student, module)

            if self.verbosity >= 30:
                print(result[module])

        return result

    def score_results(self):
        """
        For each student and module, adds  a "score" -- a brief
        summary item -- to the  result[student][module]  data attribute
        that this Tester computed.

        The score is added as the data attribute:
            result[student][module].score

        The score can be any type, but an integer between 0 and 100
        would be typical.
        """
        for student in self.who_to_grade.students:
            for module in self.what_to_grade.modules:
                result = self.results[student][module]
                score = self.score_result(result, student, module)

                self.results[student][module].score = score

    def initialize_tests_for_module(self, module):
        """
        Called (once) for the given module_name by  do_tests.
        The call occurs prior to doing the tests on all the students.
        """
        # Override in subclass if needed.
        pass

    def initialize_tests_for_student(self, student):
        """
        Called (once) for the given student by  do_tests
        prior to doing tests on that student.
        """
        # Override in subclass if needed.
        pass

    @abc.abstractmethod
    def run_tests(self, student, module):
        """
        Runs this Tester's tests for the given student and module_name.
        Returns the results of the tests, as a TesterResult
        (actually, a subclass of TesterResult).
        """
        # Must implement in subclass.

    @abc.abstractmethod
    def score_result(self, result, student, module):
        """
        Returns a "score" -- a brief summary item -- to the given
        TesterResult (result) for the given student and module.

        The score can be any type, but an integer between 0 and 100
        would be typical.
        """
        # Must implement in subclass.

    @staticmethod
    def print_results(results):
        """
        Prints the results in a pretty form.
        Call this only AFTER running  do_tests_for_students!
        """
        print()
        print('---------------------------------------------------')
        print('***************************************************')
        print(' ***** RESULTS FROM TESTER: *****')
        print('***************************************************')
        print('---------------------------------------------------')
        students = sorted(results.keys())

        for student in students:
                modules = sorted(results[student].keys())
                for module in modules:
                    print(results[student][module])


class TesterResult(object):
    def __init__(self, what_to_grade, student, module_name):
        """
        The result from running a Tester's tests on the given module_name
        in the given  what_to_grade, for the given student.

        :type what_to_grade: WhatToGrade
        :type student str
        :type module_name str
        """
        self.what_to_grade = what_to_grade
        self.student = student
        self.module_name = module_name

        # The subclass will add additional data attributes that store
        # the actual results of the Tester for the given student
        # on the given module_name.

    def __repr__(self):
        args = 'what_to_grade  student  module_name'
        return utilities.generic_repr(self, args)

    def __str__(self):
        format_string = 'Student: {}\n'
        format_string += 'What was tested: {}\n'

        s = format_string.format(self.student, self.what_was_tested)

        modules = sorted(self.results.keys())
        for module in modules:
            s += 'Results for {}:\n'.format(module)
            s += str(self.results[module])

        return s
