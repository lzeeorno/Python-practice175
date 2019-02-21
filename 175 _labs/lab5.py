#lab 05 


#step 1: get the infix input and extract 

from lab4_input_Stack import Stack
# assign the precodence 
#digit_operand="0123456789"
prec = {} #creat a dict  
prec["*"] = 3
prec["/"] = 3
prec["%"] = 3
prec["+"] = 2
prec["-"] = 2
prec["("] = 1

def main():
    file = open("input_lab5.txt" ,"r")
    infix_exprs = file.readlines() # infix experssion in the inout doc. 
    file.close()
    
    infix_exprs_list = []  #creat a list 
    for infix_expr in infix_exprs:
        infix_expr_list=[]
        for token in infix_expr.strip(): # to remove the white space  
            if token != " ":
                infix_expr_list.append(token)
        infix_exprs_list.append(infix_expr_list)
        
    for token_list in infix_exprs_list:
        op_stack = Stack()  #creat a stack for the operands 
        postfix_list = [] # the list for postfix 
        for token in token_list:
            if token in "0123456789": #to check  is the tokens belong to operands 
                postfix_list.append(token)
            elif token == "(":
                op_stack.push(token)   #either read a number or (  or a operand or )
            elif token == ")":
                op = op_stack.pop()
                while op != "(":
                    postfix_list.append(op)  # do not pop ( 
                    op = op_stack.pop()
            else:  # reading to the operands 
                while(not op_stack.is_empty()) and (prec[op_stack.peek()]>=prec[token]):
                    postfix_list.append(op_stack.pop())
                op_stack.push(token)
        while(not op_stack.is_empty()):
            postfix_list.append(op_stack.pop())
            
            
        #step 3: calculate the result 
           
        operand_stack = Stack()
        for token in postfix_list:
            if token in "0123456789":
                operand_stack.push(token)
            else:
                operand2 = operand_stack.pop() #pop twice time= take out the two items in the bottom
                operand1 = operand_stack.pop()
                result= 0
                if token=="+":
                    result = int(operand1)+int(operand2)
                elif token=="-":
                    result = int(operand1)-int(operand2)
                elif token== "*":
                    result = int(operand1)*int(operand2)
                elif token=="/":
                    result = int(operand1)/int(operand2)
                else:
                    result = int(operand1)%int(operand2)
                operand_stack.push(result)
        #step 4:  handle output
        print(operand_stack.pop()) # stack is notcallable, we only can call pop or we can use print(result) 
        #print(result)
main()