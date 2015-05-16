"""
Tests (informally) the Grader and other classes in this project.

Authors:  David Mutchler, David Lam, Mark Hays and their colleagues.
Version 1.1:  May, 2015.
"""
# TODO:  Augment the above comment to include simple instructions
# for how to use this project.
# A short example (ala  test_Grader  below) might be enough.

import Course
import Grader
import ChangesTester
import ReturnedValueTester


# ----------------------------------------------------------------------
# NOTES to David Lam:
#   1. This project is incomplete but runs.
#
#   2. Run this module  (main_for_testing)  to see what gets printed.
#
#   3. In a nutshell, this project currently:
#        a. Constructs a WhatToGrade (Course and project)
#             and a Grader.  See  test_Grader  below for an example.
#
#        b. Determines the students in the Course
#             and the non-example modules in the project.
#
#           TODO: Currently student usernames are read from a file
#             and the  Course.get_modules  method is faked
#             (hard-coded to a particular module).  Fix both.
#
#        c. Constructs a ProjectTester that, for each student in the
#             course, and each non-example module in the project,
#             tests the module and returns a TesterResult.
#
#           So far 2 Testers are implemented:
#
#             -- ChangesTester: "Tests" by computing how many lines,
#                  words, and characters the student file has,
#                  compared to the same data for the original
#                  version of the file (that students received)
#                  and a solution file.
#
#             -- ReturnedValueTester: The solution file specifies tests,
#                  each of which specifies a function, arguments to send
#                  the function, the correct returned value, and the
#                  mutation to the arguments that should occur (if any).
#                TODO: "Score" the data returned.
#
#        d. Records the results.  Currently just prints the results.
#
# Major TODO's include:
#   1.  Test everything far more carefully than I did.
#
#   2. Complete   Course.get_usernames()  and  Course.get_modules().
#
#   3. Add a   score   method to the ReturnedValueTester.
#
#   4. Uncomment the   ReturnedValueTester.TesterTest  class
#      and fix it.  (Its idea is right, but the form is from
#      a previous version of the code.)
#
#   5. Add a  FunctionsImplementedTester  that examines each
#      TODO function in a class and sees whether or not
#      the student added code to implement that function.
#      Also checks whether the student put her name per that TODO.
#
#   6. lines_of_code is a mess (but correct, perhaps).
#
#   7. Also see the  TODO, FIXME and CONSIDER comments for more to do.
#
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# NOTE: Throughout I have used not-yet-implemented extensions
# of PyDev's hint-notation, e.g. the following to indicate that the type
# of  foo  is a list of items that are EITHER an integer or a string.
#   :type foo: list<int, str>
# which means a list whose items are either an int or a str.
# ----------------------------------------------------------------------


def main():
    """
    Tests (informally) the Grader and other classes in this project.
    """
    test_Grader(ChangesTester.ChangesTester)
    test_Grader(ReturnedValueTester.ReturnedValueTester)


def test_Grader(project_tester):
    """
    Sets the StandardTester to the given ProjectTester.
    Then runs an informal test of a Grader using that StandardTester.

    :type project_tester: ProjectTester
    """
    # CONSIDER: This testing is inadequate.  Should we take the time
    # to make unit-tests for the classes/methods in this project?

    # TODO: At the least, test (informally) better than the following.

    Grader.Grader.StandardTester = project_tester

    csse120 = Course.CSSE120
    what_to_grade = Grader.WhatToGrade(csse120, 16)  # Session 16

    grader = Grader.Grader(what_to_grade)
    grader.grade()


if __name__ == '__main__':
    main()
