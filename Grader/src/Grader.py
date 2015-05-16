"""
A Grader grades a WhatToGrade, using a:
  -- WhoToGrade
  -- RepoHelper (for checking out files)
  -- Tester
  -- Recorder.

A WhatToGrade specifies the:
  -- Course (including term)
       [and hence Course information like the students enrolled, etc]
  -- Project
  -- (optionally) Module(s) within the project
  -- (optionally) For each module, which units in the module
       (function, classes, methods, ...) to grade.

Authors:  David Mutchler, David Lam, Mark Hays and their colleagues.
Version 1.1:  May, 2015.
"""

import RepoHelper
import Recorder
import ReturnedValueTester
import utilities


class Grader(object):
    """
    A Grader grades a WhatToGrade,
    for students expressed by a WhoToGrade, using a:
      -- RepoHelper (for checking out files)
      -- Tester
      -- Recorder.
    """

    # The default (standard) Tester is a ReturnedValueTester.
    # The code that constructs a Grader can reassign this
    # to a different class (e.g. to a ChangesTester.)
    StandardTester = ReturnedValueTester.ReturnedValueTester

    def __init__(self,
                 what_to_grade,
                 who_to_grade=None,
                 my_tester=None,
                 my_recorder=None,
                 my_repo_helper=None):
        """
        A Grader grades a WhatToGrade,
        for students expressed by a WhoToGrade, using a:
          -- RepoHelper (for checking out files)
          -- Tester
          -- Recorder.

        If  who_to_grade  is None:  Grade all students in the Course.
        If  tester        is None:  Use a StandardTester.
        If  recorderr     is None:  Use a StandardRecorder.
        If  repo_helper   is None:  Use a StandardRepoHelper.

        :type what_to_grade: WhatToGrade
        :type who_to_grade: WhoToGrade
        :type tester: Tester
        :type recorder: Recorder
        :type repo_helper: RepoHelper
        """
        self.what_to_grade = what_to_grade

        course = what_to_grade.course
        self.who_to_grade = WhoToGrade(who_to_grade, course)

        self.repo_helper = my_repo_helper or \
            RepoHelper.StandardRepoHelper(what_to_grade)

        self.where_to_grade = self.repo_helper.get_grading_folder()

        self.tester = my_tester or \
            Grader.StandardTester(self.what_to_grade,
                                  self.who_to_grade,
                                  self.where_to_grade)

        self.recorder = my_recorder or Recorder.StandardRecorder()

    def __repr__(self):
        args = 'what_to_grade who_to_grade tester recorder repo_helper'
        return utilities.generic_repr(self, args)

    def grade(self, include_original=True, include_solution=True):
        """
        Grade this Grader's WhatToGrade,
        for the students/teams in this Grader's WhoToGrade,
        using this Grader's Tester,
        recording results using this Grader's Recorder.

        By default, also checkout the original and solution "students".
        """
        what = self.what_to_grade
        who = self.who_to_grade.students

        # Add the  original  and  solution  usernames:
        course = self.what_to_grade.course

        if include_original:
            who.append(course.username_for_original)

        if include_solution:
            who.append(course.username_for_solution)

        # Checkout the specified students (usernames):
        result = self.repo_helper.checkout_for_grading(what, who)
        self._display_result_of_checkout(result)

        # Do the tests on the specified students (usernames)
        # and record the results:
        self.recorder.results = self.tester.do_tests_on_students()
        self.recorder.record_all_results()

    @staticmethod
    def _display_result_of_checkout(result):
        """
        Display the given result, which is a 2-tuple containing:
          -- the list of failed checkouts
          -- the list of skipped (because they already exist) checkouts

        :type result: tuple(list(str))
        """
        failures, skipped, _ = result  # Ignore the 3rd item: successes

        if failures or skipped:
            print('***************************************************')

        if failures:
            print('Checkout FAILED for the following students:')
            print('  -- ', *failures, sep='  ')

        if skipped:
            print('Checkout SKIPPED the following students')
            print('because their projects were already checked out:')
            print('  -- ', *skipped, sep='  ')

        if failures or skipped:
            print('***************************************************')


class WhatToGrade(object):
    """
    A WhatToGrade specifies the:
      -- Course (including term)
          [and hence Course information like the students enrolled, etc]
      -- Project
      -- (optionally) Module(s) within the project
      -- (optionally) For each module, which units in the module
           (function, classes, methods, ...) to grade.
    """
    # CONSIDER: A WhatToGrade here is a Project within a Course.
    # Is that (augmented by the optional modules and module-units)
    # sufficiently general?

    def __init__(self, course, project, modules=None, units=None):
        """
        Stores the given Course, project and (optionally) modules
        within the project and units within those modules.

        The project can be specified as either:
          -- a positive integer that is the session number, or
          -- the project name itself.

        :type Course: Course
        :type project (int, str)
        :type modules list((int, str))
        """
        self.course = course
        self.project = project
        self.units = units

        try:
            # project can be a session number
            self.project_name = course.projects[project]
        except:
            # or the project name itself
            self.project_name = project

        self.modules = modules or course.get_modules(self.project_name)

    def __repr__(self):
        args = 'course project modules units'
        return utilities.generic_repr(self, args)


class WhoToGrade(object):
    """
    """
    # TODO: Augment the above comment

    def __init__(self, who_to_grade=None, course=None):
        """
        If  who_to_grade  is:
          -- None or empty list: Grade all students in the Course.
          -- An integer:         Grade all students in that section.
          -- Sequence:           Grade all students listed.
          -- Filename (string):  Grade all students listed in that file.

        :type who_to_grade: (list, tuple, int)
        :type Course: Course
        """
        # CONSIDER: Allow other types for  who_to_grade  ???
        # CONSIDER: Allow GROUP names in the sequence or file?
        self.who_to_grade = who_to_grade
        self.course = course

        try:
            # If who_to_grade is:
            #   -- None or empty list - grade all the students.
            #   -- Section number(s) - grade those section(s)
            self.students = course.get_usernames(self.who_to_grade)
        except:
            try:
                # filename - grade all students in that file
                with open(who_to_grade, 'r') as file:
                    self.students = file.read().split()
            except:
                # who_to_grade is a sequence of students to grade
                self.students = who_to_grade

    def __repr__(self):
        args = 'who_to_grade course'
        return utilities.generic_repr(self, args)
