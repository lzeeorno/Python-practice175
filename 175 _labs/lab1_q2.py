f = open('lab1q2_input_earthquake.txt','r') # open the file
string = f.read() # read the file
list_of_string = string.splitlines() # split the lines between the string and create a list


def output():
    # create the dictionary of earthquake data
    # by spliting up the elements inside the list_of_stiring
    # return the dict
    
    line = []  
    earthquake = {}
    for elements in list_of_string: # check for each string inside the list
        C = elements.split() # split the strings
        line.append(C)
    
    for eachList in line: 
        region = eachList[len(eachList)-1] # set the region
        earthquake[region] = [] # create the dictionary

        for region in earthquake:
            for eachList in line:
                index = 0
                if region == eachList[len(eachList)-1]: # check for the region inside eachList
                    date = eachList[index + 1] # set the date
                    magnitude = float(eachList[index]) # set the magnitude
                    attribute = [date,magnitude] # set the attribute
                    earthquake[region].append(attribute) # append the attribute to the values of the dictionary               
        
        
        content = [region,*earthquake[region]]
        print(content)
    

output()