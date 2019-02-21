#id:1465251 Zheng Fuchen
#reference: https://www.quora.com/What-is-the-use-ord-and-chr-in-python



#open the file
file=input("Enter the input filename:")
secret = open("as1q2_input_secret_code.txt",'r')

for line in secret:
    eachLine=line.split()
    try:
        originWord = eachLine[0]
    except:
        pass
    else:
        try:
            key=int(eachLine[1])
        except:
            print('MISSING KEY!' )
        else:  
            for word in originWord:
                newWord=chr(ord(word)+key)
                
                if ord(newWord)>ord('Z'):
                    newWord=chr(ord(newWord)-26)
                 
                print(newWord,end='')
            print('')