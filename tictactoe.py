

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
        self.table = [0, 0, 1],[0, 1, 0], [0, 0, 0]     # y and x are inverted!
        self.drawer(self.symbol1, self.symbol2)

    def ask(self, value):
        if self.winner is None:

            coordinates = input('Enter your coordinates [1-Letter+Number]: ').upper()
            self.reader(coordinates, value)
            self.drawer(self.p1.symbol, self.p2.symbol)
            self.check_win()


    def reader(self, coordinates, value):       #when the input is enter nothing happens
        x, y = None, None
        for c in coordinates:
            c = str(c)
            try:
                if c in self.x_map:
                    x = self.x_map[c]
                    self.check_in_table(x, y, value)

                elif c in self.y_map:
                    y = self.y_map[c]
                    self.check_in_table(x, y, value)
            except:
                print('out of range...')
    
    def check_in_table(self, x, y, value):
        if x is not None and y is not None:
            if self.table[y][x] == 0:
                self.table[y][x] = value
            else:
                print('this coordinates have been already picked...')
                self.ask(value)

            
    def start(self):
        self.winner = None
        self.name1 = input('Name of Player 1: ')
        self.symbol1 = input('P1 put your symbol (only one): ')
        
        self.name2 = input('Name of Player 2: ')
        self.symbol2 = input('P2 put your symbol (only one): ')
    
        self.p1 = Player(self.name1, self.symbol1, 1)
        self.p2 = Player(self.name2, self.symbol2, 4) # the value is 4 because then there is no problem by checking who the winner is
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
    
    def drawer(self, symbol1, symbol2):     #when incorrect insert, two prints...
        print(' A|B|C')
        for y in range(len(self.table)):
            print('')
            print(f"{(y + 1)}|", end='')
            for x in range(len(self.table[0])):
                if self.table[y][x] == 1:
                    print(symbol1, end='|')
                elif self.table[y][x] == 4:
                    print(symbol2,end='|')
                else:
                    print(' ', end='|')
            print('')
tictactoe = Game()
