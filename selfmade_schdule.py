# enter the schedule you need
class Stack:

    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[len(self.__items)-1]

    def is_empty(self):
        return self.__items == []

    def size(self):
        return len(self.__items)

class schedule:
    def enterschdule():
        while True:
            s = input('do you want to study today?(y/n):')
            if s.lower() == 'y':
                schedule.setschdule()
                break
            elif s.lower() == 'n':
                print('ok, goodbye')
                break
            else:
                print('wrong input, please enter y/n!')


    def setschdule():
            while True:
                s2 = input('Do you want to change secdule right now?(y/n):')
                if s2.lower() == 'y':
                    f = open('schedule.txt','w')
                    work1 = input('please enter mission1:')
                    work2 = input('please enter mission2:')
                    work3 = input('please enter mission3:')
                    work4 = input('please enter mission4:')
                    work5 = input('please enter mission5:')


                    f.write("mission1 is: "+ work1 + "\n" )
                    f.write("mission2 is: "+ work2 + "\n")
                    f.write("mission3 is: "+ work3 + "\n")
                    f.write("mission4 is: "+ work4 + "\n")
                    f.write("mission5 is: "+ work5 + "\n")
                    f.close()
                    print('schedule has updated')

                elif s2.lower() == 'n':
                    f = open('schedule.txt','r')
                    print('Today missions are following below: ')
                    content = f.read()
                    print(content)
                    break

                else:
                    print('wrong order, please enter y or n!')
                    continue
def main():
    i = input('please press enter to start the program')
    schedule.enterschdule()

main()
