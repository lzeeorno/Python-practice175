#id:1465251 Zheng Fuchen
#reference: https://www.quora.com/What-is-the-use-ord-and-chr-in-python
#https://www.youtube.com/watch?v=sHsnH1u03e4
#https://www.youtube.com/watch?v=mEFko9nf5UU


#open the file 
filename = input("Enter the input filename: ")

the_file = open("as1q2_input_secret_code.txt", "r")
while True:
    #estimate key in file
    line = the_file.readline()
    if (line==""): #read the file until the end 
        break
    
    
    line_breakdown_list = line.strip().split(" ")
    #print(line_breakdown_list)  # to track the content of the line_breakdown_list
    if (len(line_breakdown_list)<2 ):  # line_breakdown_list<2 means it lost a key or the chr
        if (line_breakdown_list[0] != ''): # this line means file have chr but lost a key 
            print("Missing key!")
        continue
    #analysis the data
    newWord = ""
    for i in line_breakdown_list[0]:
        originalWord = ord(i) + int(line_breakdown_list[1])
        #print(int(line_breakdown_list[1]))  #checking the key of the old chr
        
        #if (originalWord >=65+26 and originalWord< 65):
            #pass
            ##print(chr(originalWord))
        #elif (originalWord <= 65):
            #originalWord += 26
        #elif (originalWord >= 65+26):
            #originalWord -= 26
                
        originalWord = ((originalWord +26 -65)%26) + 65   #ASCII code for ‘A’ is 65
        
        newWord += chr(originalWord)  
        #chr() gives the corresponding character for given ASCII code.
        
    print(newWord)
        
            

    