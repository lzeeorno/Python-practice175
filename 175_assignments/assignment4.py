#assignment 4 
#leon zheng (1465251)

class Minimax:
    def __init__(self, nimState, minMaxLevel):
        self.state = nimState
        self.level = minMaxLevel
        self.child = []

    def split_a_pile(self, numofCoins):
        poss = []
        mid = numofCoins//2 +1
        for pile_1 in range (1,mid):
            pile_2 = numofCoins - pile_1
            if pile_1 != pile_2:
                pair = [pile_1, pile_2]
                poss.append(pair)
                #print(pile_1, pile_2)
        return poss
    
    def split_child(self, state):
        out = []
        for pile in range( len(state)):
            k = state[pile]
            if k > 2:
                posibilities = self.split_a_pile(k)
                for i,j in posibilities:
                    newstate = list(state)
                    newstate[pile] = i
                    newstate.append(j)
                    newstate.sort()
                    if newstate not in out:
                        out.append(newstate)
        return out 
    
    def build(self):
        posibilities_of_next_step = self.split_child(self.state)
        for p in posibilities_of_next_step:
            self.add_child(p)
            self.child[-1].build()
            
        #for pile in range (len(self.state)):
            #k= self.state[pile]
            #if k >2:
                #posibilities = self. split_a_pile(k)
                #for i,j in posibilities:
                    ##newstate = list(self.state)
                    #newstate = self.state.copy()
                    #newstate[pile]=i
                    #newstate.append(j)
                    #newstate.sort()
                    #self.add_child(newstate)
                    
    
    
    def add_child(self, newstate):
        #print(newstate)
        if self.level == 'Min':
            newLevel = 'Max'
        else:
            newLevel = 'Min'
            
        child = Minimax(newstate, newLevel)
        
        self.child.append(child)
        
    def print_tree(self, indentation, last):
        print(indentation, end = '')
        
        if last:
            print('\-', end = '')
            indentation += '  '
        else:
            print('+ ', end='')
            indentation += '| ' 
            
            
        print(self.state, end ='')
        if last:
            print(' ', end='')
            print(self.level.upper())
        else:
            print(' ')
            
        child_i = 0 
        for child in self.child:
            is_last_child = False
            if child_i == len(self.child)-1:
                is_last_child = True
            child.print_tree(indentation, is_last_child)
            child_i +=1



def main():
    user_input = True
    while True:
        size = input('Choose your initial size of the pile. Should be more than 2:')
        try:
            size = int(size)
        except:
            continue        
        if size <= 2:
            continue
                    
        else:
            root = Minimax([size],'Max')
            root.build()
            root.print_tree('',True)
            break
main()


       
