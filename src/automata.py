import itertools
import random    

class Automata:
    def __init__(self, rule, radix, limit):
        """

        Parameters
        ----------
        rule: String
            Set of output values which tells how the automata is going to evolve.

        radix: int
            The numeral system.

        limit: int
            The limit width of the automata (max and min number of cells).

        Returns
        -------
        None.

        """
        transitions = {}
        self.rule = rule
        self.radix = radix
        self.limit = limit

    def init_automata(self):
        """
        Initializes the automata by assigning a transitions table using the radix, rule and limit.

        Parameters
        ----------

        Returns
        -------
        None.

        """
        iter = [i for i in range(self.radix)]
        if self.rule is None: #If the initial rule is None (it wasn't assigned by user), then assigns a random rule
            self.rule = [random.randint(0, len(iter)-1) for i in range(0, self.limit)]
        states = itertools.product(iter, repeat=3) #Does all combinations for every possible state 
        states = set()
        self.transitions = dict(zip(sorted(states), self.rule))

    def get_next_state(self, ladj, act, radj):
        """
        Gets the following state by looking up in the transitions table where (ladj, act, radj) is
        the key in tuple form.

        Parameters
        ----------
        ladj: int
            Left adjacent of the actual state.

        act: int
            Actual state.

        radj: int
            Right adjacent of the actual state.

        Returns
        -------
        int
            The next state

        """
        next_state = self.transitions[(ladj, act, radj)]
        return next_state
