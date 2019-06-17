class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.splited = self.matrix_string.split('\n')
        new_list = []
        for i in self.splited:
            i = i.split()
            i = list(map(int,i))
            new_list.append(i)
        self.new_list = new_list
        self.length = len(new_list[0]) - 1
    def row(self,index):
        index -= 1
        try:
            return self.new_list[index]
        except:
            print("There is not such index")
    def column(self, index):
        index -= 1
        list = []
        try:
            for element in self.new_list:
                list.append(element[index])
            return list
        except:
            return "There is not such index"