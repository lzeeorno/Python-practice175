### load data from file
input_file = open("input_lab8.txt", "r")

marks = []

while True:
    line = input_file.readline()

    if len(line) == 0:
        break # end of file
    line = line.strip()
    if len(line) == 0:
        continue # skip blank lines

    #print(line)

    line_break = line.split(" ")
    marks.append(int(line_break[1].strip()))
    
#print(marks)

### Calculate statistics
average = sum(marks)/len(marks)
minimum = min(marks)
maximum = max(marks)


### calculate display for bars
bars = []

for i in range(0,10):
    bars.append(0)

for mark in marks:
    bars[mark//10] += 1

### generate html
tags = "<html> <body> <h1> <b> Welcome to statistics page! </b> </h1> "

html = "<br/> Average is: " + str(average) + \
       "<br/>Minimum is: " + str(minimum) + \
       "<br/>Maximum is: " + str(maximum) +"<br/><br/><br/>"

chart = "<table> <tr> "
line2 = "<tr>"

i=0
for b in bars:
    height = 20 * b
    chart += "<td valign=\"bottom\"> <div style=\"width:30px;height:" + str(height) + "px;background:blue;border:1px solid red;\"> </div></td>"
    line2 += "<td style=\"width:50px;\"> [" + str(i) + "-" + str(i+9) + "] </td>"
    i += 10

chart += "</tr>"
endtags = " </tr> </table> </body></html>"

out = open("lab8q2_outputv1.html", 'w')
out.write(tags + html + chart + line2 + endtags)
out.close()
