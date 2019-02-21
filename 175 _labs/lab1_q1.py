f1 = open('lab1q1_input_rainfall.txt','r')
newfile = open('rainfallfmt_lab1q1output.txt','w')

sixty = []
seventy = []
eighty = []
ninety = []

for line in f1:
    value = line.split()
    value[1] = float(value[1])
    if value[1]<=70:
        sixty.append(value)
    elif value[1]<=80:
        seventy.append(value)
    elif value[1]<=90:
        eighty.append(value)
    else:
        ninety.append(value)

#sort each bucket on the rainfall value
sixty.sort(key=lambda x:x[1])
seventy.sort(key=lambda x:x[1])
eighty.sort(key=lambda x:x[1])
ninety.sort(key=lambda x:x[1])

newfile.write("[60-70]\n")
for line in sixty:
    newfile.write('%+25s %5.1f\n' % (line[0],line[1]))
newfile.write("[70-80]\n")
for line in seventy:
    newfile.write('%+25s %5.1f\n' % (line[0],line[1]))
newfile.write("[80-90]\n")
for line in eighty:
    newfile.write('%+25s %5.1f\n' % (line[0],line[1]))
newfile.write("[90-100]\n")
for line in ninety:
    newfile.write('%+25s %5.1f\n' % (line[0],line[1]))

newfile.close()


