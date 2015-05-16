"""
"""
# TODO: Put a comment above.

import utilities
import Tester


class ProjectRecorder(object):
    """
    """
    # TODO: Put a comment above.

    # TODO: Implement this class.  It should record (not print).

    def __init__(self, results=None):
        """
        :type results: TesterResult
        """
        # TODO: Augment the above comment.

        # Note:  The  results  data instance is usually set
        # after the Tester finishes its work,
        # not when the ProjectRecorder is constructed.
        self.results = results

    def __repr__(self):
        args = 'results'
        return utilities.generic_repr(self, args)

    def record(self, result):
        pass

    def record_all_results(self):
        # TODO: Implement this.
        Tester.ProjectTester.print_results(self.results)


class StandardRecorder(ProjectRecorder):
    pass
