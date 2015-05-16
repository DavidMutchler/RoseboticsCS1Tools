"""
"""
# TODO: Put a comment above.

import Tester
import lines_of_code
import utilities


class ChangesTester(Tester.ProjectTester):
    """
    Tests by examining how much (if at all) each module has changed
    since the student received it.

    For each module, the result of running a ChangesTester
    on that module includes:
      -- the number of (lines, words, characters) the module has,
    along with that same triple, but compared to:
      -- the original state of the module (when students received it)
      -- the solution provided for the module
    """

    def __init__(self, what_to_grade, who_to_grade, where_to_grade,
                 verbosity=None):
        """
        Tests the given  what_to_grade  for the students specified
        by the given  who_to_grade, given that checked-out projects
        are in the given  where_to_grade  folder.

        Tests by examining how much (if at all) each module has changed
        since the student received it.

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
        self.stats_for_original = None
        self.stats_for_solution = None

    def initialize_tests_for_module(self, module):
        """
        For the given module, compute and save the ModuleStatistics
        for the original and solution versions of the module.
        """
        course = self.what_to_grade.course

        original = course.username_for_original
        self.stats_for_original = self.get_stats(original, module)

        solution = course.username_for_solution
        self.stats_for_solution = self.get_stats(solution, module)

    def get_stats(self, student, module):
        """
        Returns ...
        :rtype StatisticsForModule
        """
        # TODO: Augment the above comment.

        # FIXME: The folder structure in the following statement
        # should come from elsewhere.  Right now it is both here
        # and in RepoHelper, and it is specific to projects
        # as we set them up for Eclipse in 120.
        filename = self.where_to_grade + student + '/src/' + module

        # TODO: the  lines_of_code  module should use a class for this?
        return lines_of_code.evaluate_module(filename)

    def run_tests(self, student, module):
        """
        :rtype ChangesTesterResult
        """
        # TODO: Augment the above comment.

        stats_for_module = self.get_stats(student, module)
        vs_original = stats_for_module.minus(self.stats_for_original)
        vs_solution = stats_for_module.minus(self.stats_for_solution)

        result = ChangesTesterResult(self.what_to_grade,
                                     student,
                                     module,
                                     stats_for_module,
                                     vs_original,
                                     vs_solution)
        return result

    def score_result(self, result, student, module):
        """
        Adds a "score" -- a brief summary item -- to the given
        TesterResult (result) for the given student and module.

        For a ChangesTester, the score is ...

        This is a miserable way to evaluate a student's work.
        Other Testers can do much better.

        :rtype int
        """
        # TODO: Augment the above comment

        course = self.what_to_grade.course
        solution = course.username_for_solution

        solution_result = self.results[solution][module]
        student_result = result

        solution_stats = solution_result.statistics_for_vs_original
        solution_score = solution_stats.wo_comments.lines

        student_stats = student_result.statistics_for_vs_original
        student_score = student_stats.wo_comments.lines

        score = (student_score / solution_score) * 100
        score = round(score)

        return score


class ChangesTesterResult(Tester.TesterResult):
    """
    The result obtained by running a ChangesTester on a module
    for a student.  That result includes:
      -- the StatisticsForModule for the module,
      -- that StatisticsForModule compared to the StatisticForModule
           objects for:
           -- the original state of the module
           -- the solution provided for the module

    Each StatisticsForModule is a set of (lines, words, characters) for:
      -- the module itself
      -- the module with blank lines removed
      -- the module with blank lines and docstrings removed
      -- the module with blank lines, docstrings and comments removed
    """
    def __init__(self,
                 what_to_grade,
                 student,
                 module_name,
                 statistics_for_module=None,
                 statistics_for_vs_original=None,
                 statistics_for_vs_solution=None,
                 score=0):
        """
        :type what_to_grade: WhatToGrade
        :type student str
        :type module_name str
        :type statistics_for_module: StatisticsForModule
        :type statistics_for_vs_original: StatisticsForModule
        :type statistics_for_vs_solution: StatisticsForModule
        :type score int
        """
        # TODO: Augment the above comment.
        super().__init__(what_to_grade, student, module_name)

        self.statistics_for_module = statistics_for_module
        self.statistics_for_vs_original = statistics_for_vs_original
        self.statistics_for_vs_solution = statistics_for_vs_solution
        self.score = score

    # CONSIDER: repr and str below are provided to display results.
    # But what we really need is to STORE and/or LOG results.
    # The following will eventually need to change, I suspect.

    def __repr__(self):
        args = 'what_to_grade student module_name'
        args += ' statistics_for_module'
        args += ' statistics_for_vs_original'
        args += ' statistics_for_vs_solution'
        args += ' score'

        return utilities.generic_repr(self, args)

    def __str__(self):
        result = 'For {:8} on {}:\n'.format(self.student,
                                            self.module_name)

        format_string = '{:15} {:>16} {:>16} {:>16}\n'
        header = ('When I removed:',
                  'vs. Original', 'vs. Solution', 'Module itself')
        result += format_string.format(*header)

        transformations = ('nothing_removed',
                           'wo_blank_lines',
                           'wo_docstrings',
                           'wo_comments')
        labels = ('  Nothing',
                  '  Blank lines',
                  '   + docstrings',
                  '   + comments')

        for k in range(len(transformations)):
            transformation = transformations[k]
            label = labels[k]
            vs_original = getattr(self.statistics_for_vs_original,
                                  transformation)
            vs_solution = getattr(self.statistics_for_vs_solution,
                                  transformation)
            for_module = getattr(self.statistics_for_module,
                                 transformation)

            trio = (vs_original, vs_solution, for_module)
            stat = []
            for k in range(len(trio)):
                stat.append(' {:3} {:4} {:5}'.format(trio[k].lines,
                                                     trio[k].words,
                                                     trio[k].characters))

            result += format_string.format(label, *stat)

        result += 'Score: {:3d}\n'.format(self.score)

        return result
