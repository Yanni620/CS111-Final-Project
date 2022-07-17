#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: A'Yanna Rouse
# email: yanni620@bu.ed
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    
    def  __init__(self, depth_limit):
        """ constructs a new Searcher object
        """
        
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        
    def add_state(self, new_state):
        """ takes a single State object called new_state and adds it to the 
        Searcher‘s list of untested states.
        """
        self.states += [new_state]
        
    def should_add(self, state):
        """ takes a State object called state and returns True if the called 
        Searcher should add state to its list of untested states, and False 
        otherwise.
        """

        if self.depth_limit != -1:
            
            if state.num_moves > self.depth_limit:
                return False

        if state.creates_cycle():
            return False
        
        else:
            return True
        
    def add_states(self, new_states):
        """ takes a list State objects called new_states, and that processes 
        the elements of new_states one at a time
        """
        
        for x in new_states:
            
            if self.should_add(x) == True:
                self.add_state(x) 
    
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
                
    def find_solution(self, init_state):
        """ performs a full state-space search that begins at the specified initial 
        state init_state and ends when the goal state is found or when the Searcher 
        runs out of untested states
        """
        
        self.add_state(init_state)
        
        while len(self.states) > 0:
        
            s = self.next_state()
            self.num_tested += 1
            
            if s.is_goal() == True:
                return s
            
            else:
                self.add_states(s.generate_successors())
                
        return None
            
    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s

### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    """ A class for objects that perform breadth-first search (BFS)
    """

    def next_state(self):
        """ follows FIFO (first-in first-out) ordering – choosing the state that 
        has been in the list the longest.
        """
        
        for i in range(len(self.states)):
            
            s = self.states[i]
            self.states.remove(s)
            return s
        
class DFSearcher(Searcher):
    """ A class for objects that perform depth-first search (DFS)
    """
    def next_state(self):
        """ follow LIFO (last-in first-out) ordering – choosing the state that 
        was most recently added to the list.
        """
        
        for i in range(len(self.states)):
            
            s = self.states[-i-1]
            self.states.remove(s)
            return s
       
def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###
def h1(state):
    """ computes and returns an estimate of how many additional moves are 
        needed to get from state to the goal state
    """
    
    moves = state.board.num_misplaced()
    return moves

def h2(state):
    """ computes and returns the # of misplaced tiles in the state
    """
    
    notequal = state.board.not_equal()
    return notequal
    
class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, heuristic):
        """ constructs a new GreedySearcher object
        """
       
        super().__init__(-1)
        
        self.heuristic = heuristic
        
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
    
        return -1 * self.heuristic(state)
    
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def add_state(self, state):
        """ overrides the add_state method that is inherited from Searcher to 
        pair each state with its priority will allow a GreedySearcher to choose 
        its next state based on the priorities of the states.
        """
        
        priority = self.priority(state)
        
        self.states += [[priority, state]] 
        
    def next_state(self):
        """ overrides the next_state method that is inherited from Searcher to 
        choose one of the states with the highest priority.
        """

        s = max(self.states)
        self.states.remove(s)
        return s[1]

### Add your AStarSeacher class definition below. ###
class AStarSearcher(GreedySearcher):
    """ A class that perform A* search
    """
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        num_moves = state.num_moves
        return -1 * (self.heuristic(state) + num_moves)
    

