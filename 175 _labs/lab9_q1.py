#lab 9 
def recursiveSelectionSort(alist):
    # base case
    if len(alist) <= 1:
        return alist

    maximum = max(alist)
    max_index = alist.index(maximum)

    alist[max_index], alist[-1] = alist[-1], alist[max_index]
    alist[:len(alist)-1] = recursiveSelectionSort(alist[:len(alist)-1])
    return alist


def selectionSort(data):
# Sort the given Array with selection sort method
#(Ascending order)
    for index in range(len(data)):
        smallIndex = index
        for i in range(index,len(data)): # finding smallest
            if(data[i]<data[smallIndex]):
                smallIndex=i
        temp=data[index] # swapping
        data[index]=data[smallIndex]
        data[smallIndex]=temp

#def selectionSort(alist):
    #for fillslot in range(len(alist)-1,0,-1):
        #positionOfMax=0
        #for location in range(1,fillslot+1):
            #if alist[location]>alist[positionOfMax]:
                #positionOfMax = location

        #temp = alist[fillslot]
        #alist[fillslot] = alist[positionOfMax]
        #alist[positionOfMax] = temp

import random, time
input_list = [300, 293, 286, 279, 272, 265, \
              258, 251, 244, 237, 230, 223, \
              216, 209, 202, 195, 188, 181, \
              174, 167, 160, 153, 146, 139, \
              132, 125, 118, 111, 104, 97, \
              90, 83, 76, 69, 62, 55, 48, \
              41, 34, 27, 20, 13, 6, 0]
#comparing time

print(input_list)
start_time = time.time()
recursiveSelectionSort(input_list)
end_time = time.time()

print("Text book:", end_time - start_time)

start_time = time.time()
selectionSort(input_list)
end_time = time.time()
print("Recursion:", end_time - start_time)
print(input_list)
