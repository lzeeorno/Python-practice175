from lab4_input_Stack import Stack
# assign 
forwardStack = Stack()
backwardStack = Stack()
current_page = "www.cs.ualberta.ca"
print(current_page)
while(True):
    user_command = input()
    if(user_command == '>'):
        # forward
        if (forwardStack.is_empty()):
            print("Error command")
            continue
        backwardStack.push(current_page)
        current_page = forwardStack.pop()
        
    elif(user_command=='<'):
        # backward
        if (backwardStack.is_empty()):
            print("Error command")
            continue
        forwardStack.push(current_page)
        current_page = backwardStack.pop()
        
    elif(user_command=='='):
        #enter anywebsaide
        if (backwardStack.is_empty()):
            print("the current page is ", current_page)
            continue
    else:
        # visit new website
        backwardStack.push(current_page)
        current_page = user_command
        forwardStack = Stack()
        
    print(forwardStack)
    print(backwardStack)
    print("The current page is: ", current_page)


