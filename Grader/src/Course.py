"""
"""
# TODO: Put a comment above.

# CONSIDER: May need the following to automate getting rosters, etc.
# FOLDER_FOR_ROSTERS = 'Rosters'
# URL_FOR_ROSTERS = URL_FOR_CSSE_HOME + COURSE + '/' + TERM + '/' \
#     + FOLDER_FOR_ROSTERS + '/' + TERM + '/'


# TODO: information other than prefix, number and term
# should come from a lookup on the schedule lookup page.
# Even the term should default to the current term,
# so only 'csse120' is needed.

import utilities


class Course(object):
    """
    """
    # TODO: Augment the above comment.

    URL_FOR_COURSES = 'http:www.rose-hulman.edu/class/csse/'

    def __init__(self, prefix, number, term,
                 sections,
                 projects=None,
                 course_repo=None,
                 students_repo=None,
                 course_url=None,
                 username_for_solution='solution',
                 username_for_original='original',
                 suffix_for_test_files='_tests'):
        self.prefix = prefix
        self.number = number
        self.term = str(term)
        self.sections = sections
        self.course_name = self.prefix + str(self.number)

        self.projects = projects  # FIXME to look up projects

        self.course_repo = course_repo or (self.course_name + '/trunk/')
        self.students_repo = students_repo or \
            (self.course_name + '-' + self.term)

        self.course_url = course_url or \
            (Course.URL_FOR_COURSES + self.course_name)

        # CONSIDER: I created SVN accounts whose usernames are
        # are 'solution' and 'original'.  These could conflict
        # with a future student, but are highly unlikely to do so.
        self.username_for_solution = username_for_solution
        self.username_for_original = username_for_original

        self.suffix_for_test_files = suffix_for_test_files

    def __repr__(self):
        args = 'prefix  number  term  sections  projects'
        args += ' course_repo  students_repo  course_url'
        args += ' username_for_solution  username_for_original'
        args += ' suffix_for_test_files'

        return utilities.generic_repr(self, args)

    def get_usernames(self, section=None):
        # TODO: Implement this.  No section means all students.
        #       Lookup data up from the web.

        # For now (for testing):
        with open('usernames.txt', 'r') as file:
            return file.read().split()

    def get_modules(self, project_name, include_examples=False):
        """
        Returns a list of all the modules in a project,
        excluding the example modules (unless include_examples is True).
        """
        # TODO: Implement this.  For now (for testing):
        return ['m2.py']


# Don't forget to change the TERM each term, and the SECTIONS.
# TODO: Automate that.  Also automate finding the project names.
CSSE120 = Course('csse', '120', '201430', ['01', '02'],
                 [None,
                  'Session01_IntroductionToPython',
                  'Session02_InputComputeOutput',
                  'Session03_LoopsAndUsingObjects',
                  'Session04_FunctionsAndAccumulators',
                  '', '', '', '', '', '', '', '', '', '', '',
                  'Session16_Test2_201430'
                  ],
                 'csse120-python/branches/robonew/'
                 )
