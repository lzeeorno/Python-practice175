### step 1: load data from file

input_file = open("input_lab8.txt", "r")

marks = []

while True:
    line = input_file.readline()
    
    if len(line) == 0:
        break # end of file
    line = line.strip()
    if len(line) == 0:
        continue # skip blank lines   
    line_break = line.split(" ")
    marks.append(int(line_break[1].strip()))
    print(line_break)
print(marks)    
### Step 2: analysis data
average = sum(marks)/len(marks)
minimum = int(min(marks))
maximum = int(max(marks))

bars = [0 for i in range(10)]
for mark in marks:
    bar_i = int(mark//10)
    bars[bar_i] += 1
print(bars)

### Step 3: generate html
output_file = open("lab8q2_outputv2.html", "w")

output_file.write("<html><body>")
output_file.write("<h1> <b> Welcome to statistic page!</b> </h1>")
output_file.write("<br/> \
                  Average is: "+str(average) +\
                  "<br/> \
                  Minimum is: "+str(minimum) +\
                  "<br/> \
                  Maximum is: "+str(maximum))
                  
output_file.write("<table>")
## row 1
output_file.write("<tr>")
# bars
for i in bars:
    output_file.write("<td valign=\"bottom\">")
    output_file.write("<div style=\"width:40px;\
                                    height:"+ str(i*24)+"px;\
                                    background:blue;\
                                    border:1px solid red;\"></div>")
    output_file.write("</td>")
output_file.write("</tr>")


## row 2
output_file.write("<tr>")
# label
start = 0
end = 9
for i in bars:
    output_file.write("<td>" +"[{}-{}]".format(start, end) + "</td>")
    start = start + 10
    end = end + 10

output_file.write("</tr>")

output_file.write("</table>")

output_file.write("</body></html>")

output_file.close()
