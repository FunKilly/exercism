class Garden(object):
    def __init__(self, diagram, students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet',
                                            'Ileana', 'Joseph', 'Kincaid', 'Larry']):
        self.plants_list = {'V':'Violets','R':'Radishes','C':'Clover','G':'Grass'}
        self.students = students
        self.students.sort()
        self.diagram = diagram.split('\n')

    def plants(self,student_name):
        n = (self.students.index(student_name)*2)+1
        result = []
        for row in self.diagram:
            result.append(self.plants_list[row[n-1]])
            result.append(self.plants_list[row[n]])
        return result

