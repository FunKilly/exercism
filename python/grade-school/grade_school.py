from collections import defaultdict


class School(object):

    def __init__(self):
        self.students = defaultdict(list)

    def add_student(self, name='', grade=''):
        self.students[grade].append(name)

    def roster(self):
        roster_list = [(grade, tuple(sorted(students))) for grade, students in sorted(self.students.items())]
        roster_return = [stud for elem in roster_list for stud in elem[1]]
        return roster_return

    def grade(self, grade_number):
        return sorted(self.students[grade_number])
