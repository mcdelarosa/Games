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
        self.table = [0, 0, 0],[0, 0, 0], [0, 0, 0]

    def ask(self, value):
        coordinates = input('Enter your coordinates: ').upper()
        self.reader(coordinates, value)
        self.drawer(self.p1.symbol, self.p2.symbol)

    def reader(self, coordinates, value):
        x, y = None, None
        for c in coordinates:
            c = str(c)
            try:
                if c in self.x_map:
                    x = self.x_map[c]
                    print(x)
                    self.check_in_table(x, y, value)

                elif c in self.y_map:
                    y = self.y_map[c]
                    print(y)
                    self.check_in_table(x, y, value)
            except:
                print('out of range...')
    
    def check_in_table(self, x, y, value):
        if x is not None and y is not None:
            if self.table[x][y] == 0:
                self.table[x][y] = value
            else:
                print('this coordinates have been already picked...')
            
    def start(self):
        self.winner = None
        self.name1 = input('Name of Player 1: ')
        self.symbol1 = input('P1 put your symbol (only one): ')
        
        self.name2 = input('Name of Player 2: ')
        self.symbol2 = input('P2 put your symbol (only one): ')
    
        self.p1 = Player(self.name1, self.symbol1, 1)
        self.p2 = Player(self.name2, self.symbol2, 2)
        
        self.reset()

        while self.winner == None:
            self.play()
        print(f'The winner is {self.winner}!')

    def play(self):
        self.ask(self.p1.value)
        self.ask(self.p2.value)
    
    #functions for checking for the winner
    def check_win(self):
        if self.calculate_row() == 6 or self.calculate_column() == 6 or self.calculate_diagonal() == 6:
            self.winner = 'P1'
        elif self.calculate_row() == 9 or self.calculate_column() == 9 or self.calculate_diagonal() == 9:
            self.winner = 'P2'
        
    def calculate_row(self):
        for x in range(3):
            result = 0
            for y in range(3):
                result = result + self.table[y][x]
            if result == 9 or result == 6:
                return result
                
    def calculate_column(self):
        for y in range(3):
            result = 0
            for x in range(3):
                result = result + self.table[y][x]
            if result == 9 or result == 6:
                return result
            
    def calculate_diagonal(self):
        if self.calculate_to_r() == 6 or self.calculate_to_l() == 6:
            return 6
        elif self.calculate_to_r() == 9 or self.calculate_to_l() == 9:
            return 9
            
    def calculate_to_r(self):
        result = 0
        for i in range(3):
            result = result + self.table[i][i]
        return result
        
    def calculate_to_l(self):
        result = 0
        for i in range(3):
            result = result + self.table[i][2-i]
        return result
    
    def drawer(self, symbol1, symbol2):
        print(' A|B|C')
        for y in range(len(self.table)):
            print('')
            print(f"{(y + 1)}|", end='')
            for x in range(len(self.table[y])):
                if self.table[x][y] == 1:
                    print(symbol1, end='|')
                elif self.table[x][y] == 2:
                    print(symbol2,end='|')
                else:
                    print(' ', end='|')
            print('')
tictactoe = Game()
