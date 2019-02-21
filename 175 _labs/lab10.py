#lab 10
#creat a function of mergesort
# leon zheng 
def mergeSort(alist):
    inversions_count = 0
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        #inversions

        inversions_count += mergeSort(lefthalf)
        inversions_count += mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                #####inversion
                inversions_count += 1
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        old_i = i

        while i < len(lefthalf):
            ####inversions
            if i > old_i:
                inversions_count += len(righthalf)
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)
    return inversions_count


#alist = [54,26,93,17,77,31,44,55,20]
alist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print('original alist is: ',alist)
n = mergeSort(alist)
print('the new sorted alist is: ', alist)
print('the inversion time is: ',n)
