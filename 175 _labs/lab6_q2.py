# lab6 exerxise 2
from lab6_q1 import CircularQueue

#create two queue for VIP and normal customer
queue_capicity = 3
VIP_queue = CircularQueue(queue_capicity)
Normal_queue = CircularQueue(queue_capicity)

while True:
    user_cmd = input("Add, Serve, or Exit: ")
    if user_cmd.lower() in ["add",'serve','exit']:
        
        if user_cmd.lower() == "exit":
            print('Quitting')
            break
        elif user_cmd.lower() == "serve":
            if not VIP_queue.isEmpty():
                servedv = VIP_queue.dequeue()
                print(servedv, 'has been served')
            elif not Normal_queue.isEmpty():
                serven = Normal_queue.dequeue()
                print( serven,'has been served')
            else:
                #raise exception
                print("Error: both queues are empty")
                #raise Exception("Error: both queues are empty")
        
        else:
            name = input("enter the name of the person to add: ")
            isVIP = input("is the customer VIP? (yes/no): ")
            #assert isVIP.lower() in ['yes','no']
            if isVIP.lower() in ['yes','no']:
                
                if isVIP.lower() == 'yes':
                    if not VIP_queue.isFull():
                        VIP_queue.enqueue(name)
                        print('add'+ name +"to the VIP line")
                        
                    else:
                        #raise exception
                        print("error: VIP customer queue is full")
                        #raise Exception("error: VIP customer queue is full")                
                else:
                    if not Normal_queue.isFull():
                        Normal_queue.enqueue(name)
                        print('add',name,"to the line")
                    else:
                        #raise exception
                        print("error: normal customer queue is full")
                        #raise Exception("error: normal customer queue is full")
            else:
                continue
                
        #display result    
        print("people in the normal line: ", str(Normal_queue))
        print("people in the VIP line: ", str(VIP_queue))
    
        
            
        
