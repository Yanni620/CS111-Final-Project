#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: A'Yanna Rouse
# email: yanni620@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        
        for x in range(9):
            
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                self.tiles[r][c] = digitstr[3 * r + c]
                
                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c
                
    ### Add your other method definitions below. ###
    def __repr__(self):
        """ returns a string representation of a Board object
        """
        s = ''
        
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                
                if self.tiles[r][c] == '0':
                    s += '_' + ' '
                
                else:
                    s += self.tiles[r][c] + ' '
                
            s += '\n' 
        
        return s
    
    def move_blank(self, direction):
        """ takes as input a string direction that specifies the direction in 
        which the blank should move, and that attempts to modify the contents 
        of the called Board object accordingly
        """
        if direction == 'up':
            
            newr = self.blank_r - 1
            newc = self.blank_c
                
            if 0 <= newr <= len(self.tiles) - 1:
                    
                self.tiles[self.blank_r][self.blank_c] = self.tiles[newr][newc]
                self.tiles[newr][newc] = '0'
                self.blank_r = newr
                return True 
            
            else:
                return False
                        
        elif direction == 'down':
            
            newr = self.blank_r + 1
            newc = self.blank_c 
                
            if 0 <= newr <= len(self.tiles) - 1:
                    
                self.tiles[self.blank_r][self.blank_c] = self.tiles[newr][newc]
                self.tiles[newr][newc] = '0'
                self.blank_r = newr
                return True 
            
            else:
                return False
                        
        
        elif direction == 'left':
            newr = self.blank_r 
            newc = self.blank_c - 1
                
            if 0 <= newc <= len(self.tiles) - 1:
                    
                self.tiles[self.blank_r][self.blank_c] = self.tiles[newr][newc]
                self.tiles[newr][newc] = '0'
                self.blank_c = newc
                return True 
            
            else:
                return False
            
        elif direction == 'right':
            
            newr = self.blank_r 
            newc = self.blank_c + 1
                
            if 0 <= newc <= len(self.tiles) - 1:
                    
                self.tiles[self.blank_r][self.blank_c] = self.tiles[newr][newc]
                self.tiles[newr][newc] = '0'
                self.blank_c = newc
                return True 
            
            else:
                return False
                
        else:
            return False
        
    def digit_string(self):
        """ creates and returns a string of digits that corresponds to the 
        current contents of the called Board object’s tiles attribute
        """
        digit = ''
        
        for i in range(len(self.tiles)):
            for k in range(len(self.tiles[0])):
                digit += self.tiles[i][k]
            
        return digit
    
    def copy(self):
        """ returns a newly-constructed Board object that is a deep copy of 
        the called object
        """
        
        newcopy = Board(self.digit_string())
        return newcopy
        
    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board object 
        that are not where they should be in the goal state
        """
        misplaced = 0 
        
        for i in range(len(GOAL_TILES)):
            for k in range(len(GOAL_TILES[0])):
                
                if self.tiles[i][k] != '0':
                    if self.tiles[i][k] != GOAL_TILES[i][k]:
                        misplaced += 1
                    
        return misplaced
    
    def num_misplace_rows(self):
        """ divides and return the # of tiles that are in the wrong row
        """
        
        moves = 0 
        
        for i in range(len(GOAL_TILES)):
            for k in range(len(GOAL_TILES[0])):
                
                if self.tiles[i][k] != '0':
                    
                    mis = int(self.tiles[i][k]) // 3
                    
                    if mis != i:
                        moves += 1
        return moves
    
    def num_misplace_cols(self):
        """ uses % and return the # of tiles that are in the wrong column
        """
        
        moves = 0 
        
        for i in range(len(GOAL_TILES)):
            for k in range(len(GOAL_TILES[0])):
                
                if self.tiles[i][k] != '0':
                    
                    mis = int(self.tiles[i][k]) % 3
                    
                    if mis != k:
                        moves += 1
                        
        return moves
    
    def not_equal(self):
        """ returns the # of misplaced tiles that are in the wrong row or column
        """
        
        equal = self.num_misplace_rows() + self.num_misplace_cols()
        return equal
    
    
    def __eq__(self, other):
        """ returns True if the called object (self) and the argument (other) 
        have the same values for the tiles attribute, and False otherwise
        """
        if self.tiles == other.tiles:
            return True
        
        else:
            return False