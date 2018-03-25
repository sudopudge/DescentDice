

attackDice = {'blue':   ('X',
                         {'hearts': 2, 'range': 2, 'surge': 1},
                         {'hearts': 2, 'range': 3, 'surge': 0},
                         {'hearts': 2, 'range': 4, 'surge': 0},
                         {'hearts': 1, 'range': 5, 'surge': 0},
                         {'hearts': 1, 'range': 6, 'surge': 1}),
                
              'red':    ({'hearts': 1, 'range': 0, 'surge': 0},
                         {'hearts': 2, 'range': 0, 'surge': 0},
                         {'hearts': 2, 'range': 0, 'surge': 0},
                         {'hearts': 2, 'range': 0, 'surge': 0},
                         {'hearts': 3, 'range': 0, 'surge': 0},
                         {'hearts': 3, 'range': 0, 'surge': 1}),
                
              'yellow': ({'hearts': 0, 'range': 1, 'surge': 1},
                         {'hearts': 1, 'range': 1, 'surge': 0},
                         {'hearts': 1, 'range': 2, 'surge': 0},
                         {'hearts': 1, 'range': 0, 'surge': 1},
                         {'hearts': 2, 'range': 0, 'surge': 0},
                         {'hearts': 2, 'range': 0, 'surge': 1}),
                
              'green':  ({'hearts': 1, 'range': 0, 'surge': 0},
                         {'hearts': 0, 'range': 0, 'surge': 1},
                         {'hearts': 0, 'range': 1, 'surge': 1},
                         {'hearts': 1, 'range': 1, 'surge': 0},
                         {'hearts': 1, 'range': 0, 'surge': 1},
                         {'hearts': 1, 'range': 1, 'surge': 1})}

defenseDice = {'brown': (0, 0, 0, 1, 1, 2),
               'gray':  (0, 1, 1, 1, 2, 3),
               'black': (0, 2, 2, 2, 3, 4)}


class Die:
    '''
    An instance of a die.
    Parameters: color
    '''
    
    def __init__(self, color):
        self.color = color
        self.side = 0
        if self.color in ('blue', 'red', 'yellow', 'green'):
            self.sides = attackDice[color]
        else:
            self.sides = defenseDice[color]
            
    def increment(self):
        '''
        Increments the side index by 1.
        '''
        if self.side == 5:
            self.side = 0
        else:
            self.side += 1
            
    def get_side_index(self):
        return self.side
            
    def get_side_icons(self, theSide=-1):
        '''
        Returns the contents of the current side, or the specified side.
        Parameters: theSide
        Returns . (dict)
        '''
        if theSide == -1:
            return self.sides[self.side]
        else:
            return self.sides[theSide]
        

class Dice:
    '''
    A group of Die objects with supporting functions.
    Parameters: dice (a list/tuple of Die objects)
    '''
    def __init__(self, dice):
        self.dice = dice

    def all_done(self):
        '''
        Returns True if all dice in <self.dice> are on side 5. Else returns False.
        Requires: self.dice
        Returns: . (boolean)
        '''
        for die in self.dice:
            if die.get_side_index() != 5: return False
        return True
    
    def get_all_side_icons(self):
        '''
        Combines the icons of the current faces of <self.dice>.
        Requires: self.dice
        Returns: . (dict)
        '''
        totals = {'hearts': 0, 'range': 0, 'surge': 0}
        for die in self.dice:
            current = die.get_side_icons()
            if current == 'X':
                return {'hearts': 0, 'range': 0, 'surge': 0}
            totals = {x: totals[x] + current[x] for x in set(totals).union(current)}
        return totals
    
    def incrementer(self, index=-1):
        '''
        Recursively increments <self.dice> starting with the die at <index>.
        If the die at <index> was on side 5, also increment the die at <index> - 1.
        If <index> = -1 (omitted), start with the last die.
        Parameters: index
        Requires: self.dice
        '''
        if index == -1:
            index = len(self.dice) - 1
        
        die = self.dice[index]
        
        if index == 0:
            die.increment()
            return
        
        if die.get_side_index() == 5:
            self.incrementer(index - 1)
            
        die.increment()
        
            

attack = ['blue', 'red', 'yellow']
defense = []


if __name__ == '__main__':
        
    Attackers = Dice([Die(q) for q in attack])
    Defenders = Dice([Die(q) for q in defense])
        
    raw = []
    
    raw.append(Attackers.get_all_side_icons())
    while True:   
        Attackers.incrementer()     
        raw.append(Attackers.get_all_side_icons())        
        if Attackers.all_done() and Defenders.all_done(): break
        
        
    print ('Average hearts: {}'.format(round(sum([q['hearts'] for q in raw]) / len(raw), 2)))
    print ('Average range: {}'.format(round(sum([q['range'] for q in raw]) / len(raw), 2)))
    print ('Average surge: {}'.format(round(sum([q['surge'] for q in raw]) / len(raw), 2)))
    

            
        




