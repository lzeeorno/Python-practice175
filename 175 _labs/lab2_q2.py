# CMPUT 175 Winter 2013 Lab 2 Exercise 2
# This program is used to calculate the worth of an automobile.

class Automobile:
    
    # Constructor:
    def __init__(self, length, horsepower, color):
        self.__length = length
        self.__horsepower = horsepower
        self.__color = color
        
    # Returns the length:
    def get_length(self):
        #try:
            #length = input("please enter the length: ")
        length = int(length)
        #except ValueError:
            #print("not a number, ")
            
        return self.__length
    
    # Returns the horsepower:
    def get_horsepower(self):
        # TODO: You must implement this method!
        #try:
            #horsepower = input("please enter the horsepower: ")
        horsepower = int(horsepower)
        #except ValueError:
            #print("not a number, ")
             
        return self.__horsepower
    # Returns the color:
    def get_color(self):
        # TODO: You must implement this method!
        #try:
            #color = input("please enter the color of your automobile: ")
            #color = str(color)
            #if color == "red":
                #color_facor = 3
            #if color == "yellow" or "blue":
                #color_factor = 2
            #else:
                #color_fator = 1
        #except ValueError:
            #print("not a word about color")
            
        return self.__color
            
                
    #Returns the worth:
    def get_worth(self):
        # TODO: You must implement this method!
        
        worth = self.__horsepower*self.color_factor*self.__length*10
        return self.get_worth 
        
        
    
# Main function, which asks the user for the length, horsepower, and color of
# an automobile, and will then print out the worth of that automobile:
def main():
    # TODO: You must implement this function! 
    length = int(input("please enter the length: "))
    horsepower = int(input("please enter the horsepower: "))

    try:
        color_factor = 0
        color = input("please enter the color of your automobile: ")
        if color == "red":
            color_facor = color_factor + 3
        elif color == "yellow" or "blue":
            color_factor = color_factor + 2
        else:
            color_fator = color_factor + 1
    except:
        print("not a word about color")
    
    worth = horsepower*color_factor*length*10
    print (worth) 
    
    
                            
  

main()