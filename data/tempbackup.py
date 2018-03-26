import json

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

    
# with open('data/games_rules.json', 'w') as q:
#     json.dump({'Dice': {'Attack': attackDice, 'Defense': defenseDice}}, q)