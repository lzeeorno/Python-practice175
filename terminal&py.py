#how to use python in terminal
def main():
    while True:
        s = input('do you come to learn how to open py doc in terminal?(yes/no):')
        if s.lower() == 'yes':
            print('cd use to enter doc, ls to look the all file, python filename.py to open the py document')
            s1 = input('do you understand?(yes/no):')
            if s1.lower() == 'yes':
                print('nice, bye')
                break
            else:
                print('ok, come to ask again')
                break

        elif s.lower()== 'no':
            print('ok, goodbye')
            break
        else:
            print('wrong input, please enter yes/no')
            continue
main()
