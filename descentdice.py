import json, pandas


with open('data/games_rules.json', 'r') as q:
    gameRules = json.load(q)
    

    

class Die:
    '''
    A die with 6 sides, which are defined by its color.
    Parameters: color
    '''
    
    def __init__(self, color):
        self.color = color
        self.side = 0
        if self.color in ('blue', 'red', 'yellow', 'green'):
            self.sides = gameRules['Dice']['Attack'][color]
        else:
            self.sides = gameRules['Dice']['Defense'][color]
            
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
        Returns . (dict or string)
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
            
            #The blue die's X
            if current == 'X':
                return {'hearts': 0, 'range': 0, 'surge': 0}
            
            #Attack die
            if die.color in ['blue', 'red', 'yellow', 'green']:
                #Combine the hearts, range, and surge values of totals and current
                totals = {x: totals[x] + current[x] for x in set(totals).union(current)}
                
            #Defense die
            if die.color in ['brown', 'gray', 'grey', 'black']:
                totals['hearts'] -= current
        
        
        g = {x: max(0, totals[x]) for x in totals}
        return g
    
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
        
            

attack = ['blue', 'red']
defense = ['brown']
# defense = []


if __name__ == '__main__':
        
    theDice = Dice([Die(q) for q in attack] + [Die(w) for w in defense])
         
    raw = []
     
    raw.append(theDice.get_all_side_icons())
    while True:
        theDice.incrementer()
        raw.append(theDice.get_all_side_icons())
        if theDice.all_done(): break
    
    print ('Average hearts: {}'.format(round(sum([q['hearts'] for q in raw]) / len(raw), 2)))
    print ('Average range: {}'.format(round(sum([q['range'] for q in raw]) / len(raw), 2)))
    print ('Average surge: {}'.format(round(sum([q['surge'] for q in raw]) / len(raw), 2)))
    
    df = pandas.DataFrame(raw)
    
    df.to_csv('data/testcsv.csv')
    



