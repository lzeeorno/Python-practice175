from datetime import date


# Open files
members_file = open("as1q1_input_members.txt", "r")  #open method plus file name and r means  allow to read the file
books_file = open("as1q1_input_books.txt", "r")

# Load information
lib_info = {} # creat a dict
# loading the first file
while True:
    line = members_file.readline()  # readline method means start to read the file
    if (line == ""): # read until end of file
        break

    line = line.strip()  #remove certain characters (such as whitespace)
    line_breakdown_list_members = line.split(",") # use , to split in members file

    value = {}    #create a dict called value
    value['name'] = line_breakdown_list_members[1]  #assign file's info as the name, address and push them into dict value
    value['address'] = line_breakdown_list_members[2]
    value['rents'] = []

    lib_info[line_breakdown_list_members[0]] = value  #push phone number into big dict as ID

#print (value)  # to check the value dict's content
# loading the second file
while True:
    line = books_file.readline()
    if (line == ""): # end of file
        break

    line = line.strip()  #remove certain characters (such as whitespace)
    line_breakdown_list_books = line.split(";")  # use ; to split in books file

    member_phone = line_breakdown_list_books[3] #assign phone number in a new variables call member_phone
    value = lib_info[member_phone]
    book = {}  #create a new dict to save info about books
    book["book_id"] = line_breakdown_list_books[0]   #push elements into book dict
    book["price"] = float(line_breakdown_list_books[1])

    # return date extraction
    dueDate_str = line_breakdown_list_books[2]   # get all the date into books file
    dueDate_bd = dueDate_str.split("/")   # split the date by / , so we get year, month, and day
    y = int(dueDate_bd[0])    #sign  year, month, and day into y,m,d.
    m = int(dueDate_bd[1])
    d = int(dueDate_bd[2])
    dueDate = date(y, m, d)
    book["dueDate"] = dueDate

    value['rents'].append(book)
    #print(book)  #checking the content of book dict


# Close files， in case the file did not save
members_file.close()
books_file.close()

# Analysis the data

today = date(2018,1,19)
for key, value in lib_info.items():
    due = 0
    for book in value['rents']:
        nbDays = (today - book['dueDate']).days
        due += nbDays * 0.25    # the days over the duedays times 0.25 each day = the fine money
        # due = due + nbDays * 0.25   #same code with the line above
        if(nbDays>90):  # when students didn't return book after 90days of dueday, the fine need to plus the price of the book
            due += book['price']


        # save analysis datas
        book['nbDays'] = nbDays
    value['due'] = due
    #print(book)   # to track the dict's changes
    #print(value)

# Display and save to file


print("+--------------+------------------------------+--------+") #print in the python shell
print("| Phone Number | Name                         | Due    |")
print("+--------------+------------------------------+--------+")
myKeyList = list(lib_info.keys())
myKeyList.sort()

total_due = 0

for key in myKeyList:
    member_info = lib_info[key]
    total_due += member_info['due']

    output_line = "|"
    output_line += "("+key[:3]+") "+key[3:6]+" "+key[6:]+"|"   #push phone number into table
    # key[:3] means only takes first three number, key[6:] means start taking number from position 6.
    # key [3:6] means takes 3 number to the sixth number
    output_line += member_info['name']+" "*(30 - len(member_info['name']))+"|"  #push name into table

    output_line += "$"+"{0:7.2f}".format(member_info['due'])+"|"  #push due money into table
    # 7.2f means 7 position and two number after decimal point
    rent_list = member_info['rents']


    for book in rent_list:
        output_line += "["+book['book_id']+"]("+str(book['nbDays'])+" days); "  #add the book_id and nbdays after the due money

    print(output_line)

print("+--------------+------------------------------+--------+")
print("| Total Dues   |"+"{:>39}".format("$"+"{0:10.2f}".format(total_due))+"|")
print("+--------------+------------------------------+--------+")
