class Student:
    def __init__(self, student_id, name, mark):
        self.ID = student_id
        self.name = name
        self.mark = mark

    def __str__(self):
        return "\nID:{:10} name:{:20} mark:{}".format(str(self.ID), self.name, str(self.mark))

    def __repr__(self):
        return "\nID:{:10} name:{:20} mark:{}".format(str(self.ID), self.name, str(self.mark))

    def compareWith(self, other, compare_by='id'):
        if compare_by not in ['id', 'name', 'mark']:
            raise Exception('Compare method ['+compare_by+'] is invalid.')
        if not isinstance(other, Student):
            raise Exception('Cannot compare with object that\'s not Student class.')

        # prepare two datas to compare
        if compare_by == 'id':
            data1 = self.ID
            data2 = other.ID
        elif compare_by == 'name':
            data1 = self.name
            data2 = other.name
        else:
            data1 = self.mark
            data2 = other.mark

        # compare
        if data1 < data2:
            return -1
        elif data1 == data2:
            return 0
        else:
            return 1

def selectionSort(alist, compare_by):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location].compareWith(alist[positionOfMax], compare_by) == 1:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

if __name__ == '__main__':
    ### parse student info
    f = open('input_lab9_Students.txt','r')
    students = []
    while True:
        line = f.readline()
        if len(line) == 0:
            break # end of file
        line = line.strip()
        if len(line) == 0:
            continue # skip blank lines

        line_list = line.split(',')

        for i in range(len(line_list)):
            line_list[i] = line_list[i].strip()

        new_student = Student(int(line_list[0]), line_list[1], float(line_list[2]))
        # print(line_list)
        students.append(new_student)

    selectionSort(students, 'mark')
    print(students)
