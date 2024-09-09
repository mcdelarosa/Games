import re

class Player:
    def __init__(self, name, symbol, value):
        self.name = name
        self.wins = 0
        self.symbol = symbol #input(f'{name} put your symbol (only one): ')
        self.value = value
class Game:
    def __init__(self):
        
        self.winner = None
        
        self.x_map = {'A':0, 'B':1, 'C':2}
        self.y_map = {'1':0, '2':1, '3':2}
        self.length = [0, 1, 2]
        self.start()
        

    def reset(self):
        self.table = [0, 0, 0],[0, 0, 0], [0, 0, 0]     # y and x are inverted!
        self.drawer()

    def ask(self, value):
        if self.winner is None:

            coordinates =  None
            pattern = "^\w{1}\d+|^\d+\w{1}"     # from re library. This does filter the input.
            while ((coordinates is None or len(coordinates) == 0) or
                  (coordinates is not None and not re.match(pattern, coordinates))):

                coordinates = input(f'{value} :: Enter your coordinates [1-Letter+Number]:').upper()
            coor_x, coor_y = self.validate(coordinates)
            if coor_x is not None and coor_y is not None:
                if not self.table[coor_y][coor_x] == 0:
                    print('this coordinates have been already picked...')
                    self.ask(value)
                else:
                    self.assign(coor_x, coor_y, value)
                    self.drawer()
                    self.check_win()


    def validate(self, coordinates):
        x, y = None, None
        try:
            for c in coordinates:
                c = str(c)
                if c in self.x_map:
                    x = self.x_map[c]

                elif c in self.y_map:
                    y = self.y_map[c]
        except:
            print('out of range...')
            return [ None, None ]

        return [ x, y ]

    def assign(self,x,y,value):
        self.table[y][x] = value

            
    def start(self):
        self.winner = None
        name1 = input('Name of Player 1: ')
        symbol1 = input('P1 put your symbol (only one): ')
        
        name2 = input('Name of Player 2: ')
        symbol2 = input('P2 put your symbol (only one): ')
    
        self.p1 = Player(name1, symbol1, 1)
        self.p2 = Player(name2, symbol2, 4) # the value is 4 because then there is no problem by checking who the winner is
        self.reset()

        while self.winner is None:
            self.ask(self.p1.value)
            self.ask(self.p2.value)
        print(f'The winner is {self.winner}!')

    #functions to check for the winner
    def check_win(self):
        if self.calculate_row() == 3 or self.calculate_column() == 3 or self.calculate_to_l() == 3 or self.calculate_to_r() == 3:
            self.winner = 'P1'
        elif self.calculate_row() == 12 or self.calculate_column() == 12 or self.calculate_to_l() == 12 or self.calculate_to_r() == 12:
            self.winner = 'P2'

    def calculate_column(self):
        for x in range(len(self.table[0])):
            result = 0
            for y in range(len(self.table)):
                result = result + self.table[y][x]
            if result == 3 or result == 12:
                return result

    def calculate_row(self):
        for y in range(len(self.table)):
            result = 0
            for x in range(len(self.table[0])):
                result = result + self.table[y][x]
            if result == 3 or result == 12:
                return result

    # calculate in diagonal:

    def calculate_to_r(self):
        result = 0
        for i in range(len(self.table)):
            result = result + self.table[i][i]
        return result
        
    def calculate_to_l(self):
        result = 0
        for i in range(len(self.table)):
            result = result + self.table[i][2-i]
        return result
    
    def drawer(self):     #when incorrect insert, two prints...
        print(' A|B|C')
        for y in range(len(self.table)):
            print(f"{(y + 1)}|", end='')
            for x in range(len(self.table[0])):
                if self.table[y][x] == 1:
                    print(self.p1.symbol, end='|')
                elif self.table[y][x] == 4:
                    print(self.p2.symbol,end='|')
                else:
                    print(' ', end='|')
            print('')
tictactoe = Game()
